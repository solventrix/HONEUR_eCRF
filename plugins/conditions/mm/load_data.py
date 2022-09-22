import datetime
import csv
import tempfile
import shutil
from operator import indexOf
import zipfile as zipfile_py
import chardet
from django.utils.translation import gettext as _
from django.db.models import DateField, FloatField, CharField, IntegerField, BigIntegerField
from django.db import transaction
from plugins.conditions.mm import episode_categories
from entrytool import episode_categories as lot_episode_categories
from plugins.conditions.mm import models
from entrytool import models as entrytool_models
from opal.core.fields import ForeignKeyOrFreeText
from plugins.data_load.base_loader import Loader
from plugins.data_load.load_utils import match_to_choice_if_possible, get_from_ll
from plugins.data_load.load_data import LoadError
from plugins.conditions.mm.management.commands.field_mapping import FIELD_MAPPING
from plugins.conditions.mm.management.commands.translations import TRANSLATIONS
from opal.models import Patient
import os


def cast_date(value):
    value = value.strip()
    if value:
        return datetime.datetime.strptime(value, "%d/%m/%Y").date()


def is_utf8(file_name):
    is_utf8 = False
    with open(file_name, mode='rb') as f:
        detect_report = chardet.detect(f.read())
        encoding = detect_report['encoding']
        if encoding.lower() == 'utf-8' or encoding.lower() == 'utf-8-sig':
            if detect_report['confidence'] >= 0.95:
                is_utf8 = True
    return is_utf8


def is_field_type(subrecord, field_name, field_type):
    # An isinstance for django fields
    if field_type == ForeignKeyOrFreeText:
        if isinstance(getattr(subrecord.__class__, field_name), ForeignKeyOrFreeText):
            return True
    else:
        if hasattr(subrecord, f"{field_name}_fk_id"):
            return False

        if not isinstance(field_type, tuple):
            field_type = (field_type,)
        field = type(subrecord._meta.get_field(field_name))
        return field in field_type


class ZaragosaLoader(Loader):
    def __init__(self):
        self.errors = []

    def check_and_get_date(self, value, column):
        some_dt = None
        try:
            some_dt = cast_date(value)
        except Exception:
            description = (
                _(
                    "Unable to parse %s into a date with the formats dd/mm/yyyy or yyyy-mm-dd"
                )
                % value
            )
            self.add_error(column, value, description)
        return some_dt

    def check_and_get_float(self, value, column):
        result = None
        splitted = value.split(",")
        if len(splitted) == 2:
            value = f"{splitted[0]}.{splitted[1]}"
        try:
            result = float(value)
        except Exception:
            self.add_error(column, value, _("Unable to parse %s to a float") % value)
        return result

    def check_and_get_fk_or_ft(self, model, field_name, value, column):
        field = getattr(model.__class__, field_name)
        result = get_from_ll(value, field.foreign_model)
        if result:
            return result
        if not result:
            field = model._get_field(f"{field_name}_ft")
            max_length = field.max_length
            if len(value) > max_length:
                try:
                    raise ValueError(
                        _(
                            "Field is %(len_value)d long and should be less than %(max_length)d"
                            % {"len_value": len(value), "max_length": max_length}
                        )
                    )
                except Exception as err:
                    self.add_error(column, value, str(err))
        return value

    def check_and_get_string(self, subrecord, field_name, value, column):
        result = None
        if not value:
            return ""
        try:
            field = subrecord._meta.get_field(field_name)
            if field.choices:
                result = match_to_choice_if_possible(value, field.choices)
            if not result:
                result = value
                max_length = field.max_length
                if len(result) > max_length:
                    raise ValueError(
                        _(
                            "Field is %(len_value)d long and should be less than %(max_length)d"
                        )
                        % {"len_value": len(result), "max_length": max_length}
                    )

        except Exception as err:
            self.add_error(column, value, str(err))
        return result


    def check_and_get_hospital_number(self, row, column, file_name, idx):
        value = row[column]
        if entrytool_models.Demographics.objects.filter(hospital_number=value).exists():
            self.file_name = file_name
            self.idx = idx
            try:
                raise ValueError(_("Patient %s already exists") % value)
            except Exception as err:
                self.add_error(column, value, str(err))
                return ""
        return value


    def check_and_set_field(self, subrecord, field, value, column, file_name, idx):
        if not value:
            return
        self.file_name = file_name
        self.idx = idx
        value = get_translation(value)
        if value.lower() == "y":
            value = "Yes"
        elif value.lower() == "n":
            value = "No"
        if is_field_type(subrecord, field, DateField):
            some_dt = self.check_and_get_date(value, column)
            setattr(subrecord, field, some_dt)
        elif is_field_type(
            subrecord,
            field,
            (
                FloatField,
                IntegerField,
                BigIntegerField,
            ),
        ):
            some_float = self.check_and_get_float(value, column)
            setattr(subrecord, field, some_float)
        elif is_field_type(subrecord, field, ForeignKeyOrFreeText):
            value = self.check_and_get_fk_or_ft(subrecord, field, value, column)
            setattr(subrecord, field, value)
        elif is_field_type(subrecord, field, CharField):
            value = self.check_and_get_string(subrecord, field, value, column)
        else:
            setattr(subrecord, field, value)


def check_files(tmpDirectory, zip_file_name):
    """
    Check that we (case insensitively) have all the files
    that we need to load in the provided zip file.

    Returns the error structure if the file is found to be
    incomplete.
    """

    expected_file_names = set([i[0].lower() for i in FIELD_MAPPING])
    found_names = set(os.listdir(tmpDirectory))
    missing_names = list(expected_file_names - found_names)
    top_level_errors = []
    if len(missing_names) > 0:
        for missing_name in missing_names:
            top_level_errors.append(
                _('Unable to find %(expected_file_name)s in %(zipfile)s') % {
                    'expected_file_name': missing_name, 'zipfile': zip_file_name
                }
            )
    for found_name in found_names:
        if not is_utf8(os.path.join(tmpDirectory, found_name)):
            top_level_errors.append(
                _('%s is not utf-8 encoded' % found_name)
            )
    return top_level_errors


def create_patient_episode(patient_number):
    patient = Patient.objects.create()
    patient.demographics_set.update(hospital_number=patient_number)
    mm_episode = patient.episode_set.create(
        category_name=episode_categories.MM.display_name
    )
    return patient, mm_episode


def get_field_mapping(file_name, file_name_field):
    field_mapping = {(k[0].lower(), k[1].lower()): v for k, v in FIELD_MAPPING.items()}
    file_name = file_name.lower()
    file_name_field = file_name_field.lower()
    return field_mapping.get((file_name, file_name_field))


def translate_date(value):
    value = value.strip()
    if value:
        return datetime.datetime.strptime(value, "%d/%m/%Y").date()


def get_translation(value):
    if value:
        for from_value, to_value in TRANSLATIONS:
            if from_value.lower() == value.lower():
                return to_value
    return value


def create_datos_demographics(patient, episode, demographics_data, row_idx, loader):
    demographics = patient.demographics_set.all()[0]
    diagnosis_details = episode.mmdiagnosisdetails_set.all()[0]
    past_medical_history = patient.mmpastmedicalhistory_set.all()[0]
    for key, data in demographics_data.items():
        subrecord_name_and_field = get_field_mapping("datos demograficos.csv", key)
        if not subrecord_name_and_field:
            continue
        subrecord_name, field = subrecord_name_and_field
        if subrecord_name == "MMDiagnosisDetails":
            loader.check_and_set_field(
                diagnosis_details, field, data, key, "datos demograficos.csv", row_idx
            )
        elif subrecord_name == "MMPastMedicalHistory":
            loader.check_and_set_field(
                past_medical_history,
                field,
                data,
                key,
                "datos demograficos.csv",
                row_idx,
            )
        elif subrecord_name == "Demographics":
            loader.check_and_set_field(
                demographics, field, data, key, "datos demograficos.csv", row_idx
            )
        else:
            raise ValueError(
                f"Unexpected subrecord {subrecord_name} found in datos demographics"
            )
    diagnosis_details.set_consistency_token()
    diagnosis_details.save()
    past_medical_history.set_consistency_token()
    past_medical_history.save()
    demographics.set_consistency_token()
    demographics.save()


def get_sub_classification(subclassification):
    """
    Takes in sub classification and sets heavy_chain_type and light_chain_type

    Usually of the form MM{heavy chain type}{light chain type} e.g.  MMIgGKappa
    """
    mapping = {
        "": (None, None),
        "MMIgAlambda": ("IgA", "Lambda"),
        "MMIgGlambda": ("IgG", "Lambda"),
        "MMLightChainkappa": (None, "Kappa"),
        "MMIgAkappa": ("IgA", "Kappa"),
        "MMIgGkappa": ("IgG", "Kappa"),
        "MMIgDlambda": ("IgD", "Lambda"),
        "MMnonSecretory": (None, "Non-Secretory"),
        "other": ("Other", None),
        "MMIgMlambda": ("IgM", "Lambda"),
    }
    return mapping[subclassification]


def create_datos_enfermedad(
    episode, file_name, data, loader, idx, clinical_date, lab_test_date
):
    """
    Creates all the models from the datos enfermedad files.

    for later files there is a clinical date and a lab test date
    in the first file we only have the diagnosis date which will be
    used for both.
    """
    diagnosis_details = episode.mmdiagnosisdetails_set.get()
    clinical_presentation = models.ClinicalPresentation(
        episode=episode, date=clinical_date
    )
    clinical_presentation_populated = False
    lab_test = models.LabTest(episode=episode, date=lab_test_date)
    lab_test.set_consistency_token()
    lab_test_populated = False
    cytogenetics = models.Cytogenetics(episode=episode, date=lab_test_date)
    cytogenetics.set_consistency_token()
    cytogenetics_populated = False
    imaging = models.Imaging(episode=episode, date=clinical_date)
    imaging.set_consistency_token()
    imaging_populated = False
    mproteinmesurements = models.MProteinMesurements(
        episode=episode, date=lab_test_date
    )
    mproteinmesurements.set_consistency_token()
    mproteinmesurements_populated = False

    for key, value in data.items():
        subrecord_name_and_field = get_field_mapping(file_name, key)
        if not subrecord_name_and_field:
            continue
        subrecord_name, field = subrecord_name_and_field
        if subrecord_name == "MMDiagnosisDetails":
            if field == "subclassification":
                heavy_chain_type, light_chain_type = get_sub_classification(value)
                loader.check_and_set_field(
                    diagnosis_details,
                    "heavy_chain_type",
                    heavy_chain_type,
                    key,
                    file_name,
                    idx,
                )
                loader.check_and_set_field(
                    diagnosis_details,
                    "light_chain_type",
                    light_chain_type,
                    key,
                    file_name,
                    idx,
                )
            else:
                loader.check_and_set_field(
                    diagnosis_details, field, value, key, file_name, idx
                )
        elif subrecord_name == "ClinicalPresentation":
            loader.check_and_set_field(
                clinical_presentation, field, value, key, file_name, idx
            )
            clinical_presentation_populated = True
        elif subrecord_name == "LabTest" and value:
            loader.check_and_set_field(lab_test, field, value, key, file_name, idx)
            lab_test_populated = True
        elif subrecord_name == "Cytogenetics" and value:
            loader.check_and_set_field(cytogenetics, field, value, key, file_name, idx)
            cytogenetics_populated = True
        elif subrecord_name == "Imaging" and value:
            loader.check_and_set_field(imaging, field, value, key, file_name, idx)
            imaging_populated = True
        elif subrecord_name == "MProteinMesurements" and value:
            loader.check_and_set_field(
                mproteinmesurements, field, value, key, file_name, idx
            )
            mproteinmesurements_populated = True
        elif value:
            raise ValueError(
                f"Unexpected subrecord {subrecord_name} found in datos enfermidad"
            )
    diagnosis_details.save()
    if clinical_presentation_populated:
        clinical_presentation.save()
    if lab_test_populated:
        lab_test.save()
    if cytogenetics_populated:
        cytogenetics.save()
    if imaging_populated:
        imaging.save()
    if mproteinmesurements_populated:
        mproteinmesurements.save()


def create_situation_actual(episode, data, loader, idx):
    patient_status = episode.patient.mmpatientstatus_set.all()[0]
    file_name = "Situacion actual.csv"
    for key, value in data.items():
        subrecord_name_and_field = get_field_mapping(file_name, key)
        if not subrecord_name_and_field:
            continue
        _, field = subrecord_name_and_field
        loader.check_and_set_field(patient_status, field, value, key, file_name, idx)
    patient_status.set_consistency_token()
    patient_status.save()


def populate_fields_on_model(model, file_name, upstream_fields, data, loader, idx):
    """
    For a list of upstream field names, iterate through the data
    find out what out field name is and set that field on the
    model provided, then save the model.

    Don't save the '0' in response. This is not a real response
    but a happenstance of the old system.

    Only save the model if at least one field is populated.
    """
    populated = False
    for upstream_field in upstream_fields:
        if (file_name, upstream_field) in FIELD_MAPPING:
            our_field = FIELD_MAPPING[(file_name, upstream_field)][1]
            value = data.get(upstream_field)
            if value == "0":
                if model.__class__.__name__ == "MMResponse" and our_field == "response":
                    continue
            if value is not None and not value == "":
                populated = True
            loader.check_and_set_field(
                model,
                our_field,
                data.get(upstream_field),
                upstream_field,
                file_name,
                idx,
            )
    if populated:
        model.set_consistency_token()
        model.save()


def treatment_populated(file, row):
    """
    for a file e.g. Tratamiento 6.csv return if any of the fields
    that we would save are populated.

    Some fields are defaulted to 0 so ignore those if there
    are no other measurements.

    Ignore MProteinMesurements as these do not determine
    whether we create a LOT as they are stored on the MM Episode
    """
    treatment_fields = []
    for their_field_mapping, our_field_mapping in FIELD_MAPPING.items():
        if our_field_mapping[0] == "MProteinMesurements":
            continue
        file_name = their_field_mapping[0]
        if file_name.lower() == file.lower():
            treatment_fields.append(their_field_mapping[1])
    return any(
        row.get(i, "").strip() for i in treatment_fields if not row.get(i, "") == "0"
    )


def create_tratiemento(episode, iterator, data, loader, idx):
    file_name = f"tratamiento {iterator}.csv".lower()
    stuff = []

    eligible_for_stem_cell_transplant = [
        f"candidato_transplante_{iterator}",
    ]
    stuff.extend(eligible_for_stem_cell_transplant)
    alotph_fields = [
        f"fuente_alopth_{iterator}",
        f"tipo_trasplante_alotph_{iterator}",
        f"trasplante_alogenico_alotph_fecha_{iterator}",
        f"trasplante_numero_de_celulas_infundias_{iterator}",
    ]
    stuff.extend(alotph_fields)

    alotph_reponse = [
        f"tecnica_emr_alotph_{iterator}",
        f"negativizacion_emr_alotph_{iterator}",
        f"negativizacion_emr_alotph_fecha_{iterator}",
        f"respuesta_despues_trasplante_alotph_{iterator}",
    ]

    stuff.extend(alotph_reponse)
    atsp_fields = [
        f"trasplante_autologo_atsp_fecha_{iterator}",
        f"acondicionamiento_atsp_{iterator}",
        f"trasplante_tandem_atsp_{iterator}",
    ]

    atsp_response = [
        f"tecnica_emr_atsp_{iterator}",
        f"negativizacion_emr_atsp_{iterator}",
        f"negativizacion_emr_atsp_fecha_{iterator}",
        f"resp_despues_trasplante_atsp_fecha_{iterator}",
        f"estatus_trasplante_tandem_atsp_{iterator}",
        f"respuesta_despues_trasplante_atsp_{iterator}",
    ]

    stem_cell_fields = eligible_for_stem_cell_transplant + alotph_fields + atsp_fields

    # if we have an stem cell details populated or if stem cell elibility is true
    # then set the episode transplant elibility to true
    if any([data.get(i) for i in stem_cell_fields]):
        episode.mmstemcelltransplanteligibility_set.update(
            eligible_for_stem_cell_transplant=True
        )

    # ALOTPH SCT
    if any([data.get(i) for i in alotph_fields if not data.get(i) == "0"]):
        sct = entrytool_models.SCT(episode=episode, sct_type="Allogenic")
        populate_fields_on_model(sct, file_name, alotph_fields, data, loader, idx)

    # ALOTPH MMResponse
    if any([data.get(i) for i in alotph_reponse if not data.get(i) == "0"]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, alotph_reponse, data, loader, idx)

    # ATSP SCT
    if any([data.get(i) for i in atsp_fields if not data.get(i) == "0"]):
        sct = entrytool_models.SCT(episode=episode, sct_type="Autologous")
        populate_fields_on_model(sct, file_name, atsp_fields, data, loader, idx)

    # ATSP MMResponse
    if any([data.get(i) for i in atsp_response if not data.get(i) == "0"]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, atsp_response, data, loader, idx)

    # Maintenance regimen
    maintentance_regimen = [
        f"esquema_mantenimiento_{iterator}",
        f"esquema_mantenimiento_describir_{iterator}",
        f"comentarios_mantenimiento_{iterator}",
        f"manteniniemto_motivo_discontinuacion_describir_{iterator}",
        f"manteniniemto_motivo_discontinuacion_{iterator}",
        f"tratamiento_mantenimiento_fecha_fin_{iterator}",
        f"tratamiento_mantenimiento_fecha_inicio_{iterator}",
        f"tratamiento_mantenimiento_numero_ciclos_{iterator}",
    ]
    if any(
        data.get(i)
        for i in maintentance_regimen
        if not i == f"tratamiento_mantenimiento_numero_ciclos_{iterator}"
    ):
        regimen = models.MMRegimen(episode=episode, category="Maintenance")
        populate_fields_on_model(
            regimen, file_name, maintentance_regimen, data, loader, idx
        )

    # Maintenance response
    maintenance_response = [
        f"tecnica_emr2_{iterator}",  # i am inferring this belongs here based on its position in the filed
        f"negativizacion_emr_mantenimiento_{iterator}",
        f"negativizacion_emr_mantenimiento_fecha_{iterator}",
        f"mantenimiento_progresion_fecha_{iterator}",
        f"respuesta_despues_mantenimiento_{iterator}",
        f"respuesta_despues_mantenimiento_fecha_{iterator}",
    ]
    if any([data.get(i) for i in maintenance_response if not data.get(i) == "0"]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(
            response, file_name, maintenance_response, data, loader, idx
        )

    # Consolidation regimen
    consolitation_regimen = [
        f"esquema_consolidacion_{iterator}",
        f"esquema_consolidacion_otros_{iterator}",
        f"tratamiento_consolidacion_fecha_fin_{iterator}",
        f"tratamiento_consolidacion_fecha_inicio_{iterator}",
        f"numero_ciclos_{iterator}",  # inferring this field reference based on its place in the file
    ]
    if any(
        data.get(i)
        for i in consolitation_regimen
        if not i == f"numero_ciclos_{iterator}"
    ):
        regimen = models.MMRegimen(episode=episode, category="Consolidation")
        populate_fields_on_model(
            regimen, file_name, consolitation_regimen, data, loader, idx
        )

    # Consolidation response
    consolitation_response = [
        f"respuesta_despues_consolidacion_{iterator}",
        f"respuesta_despues_consolidacion_fecha_{iterator}",
        f"tecnica_emr_consolidacion_{iterator}",
        f"negativizacion_emr_consolidacion_fecha_{iterator}",
        f"negativizacion_emr_consolidacion_{iterator}",
    ]
    if any([data.get(i) for i in consolitation_response if not data.get(i) == "0"]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(
            response, file_name, consolitation_response, data, loader, idx
        )

    induction_regimen = [
        f"esquema_induccion_{iterator}",
        f"esquema_induccion_describir_{iterator}",
        f"induccion_motivo_discontinuacion_{iterator}",
        f"induccion_motivo_discontinuacion_describir_{iterator}",
        f"tratamiento_induccion_fecha_fin_{iterator}",
        f"tratamiento_induccion_fecha_inicio_{iterator}",
        f"numero_ciclos_induccion_{iterator}",
    ]
    if any(
        data.get(i)
        for i in induction_regimen
        if not i == f"numero_ciclos_induccion_{iterator}"
    ):
        regimen = models.MMRegimen(episode=episode, category="Induction")
        populate_fields_on_model(
            regimen, file_name, induction_regimen, data, loader, idx
        )

    induction_response = [
        f"tecnica_emr_induccion_{iterator}",
        f"fecha_progresion_induccion_{iterator}",
        f"negativizacion_emr_induccion_{iterator}",
        f"negativizacion_emr_induccion_fecha_{iterator}",
        f"respuesta_despues_induccion_{iterator}",
        f"respuesta_despues_induccion_fecha_{iterator}",
    ]

    if any(data.get(i) for i in induction_response if not data.get(i) == "0"):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(
            response, file_name, induction_response, data, loader, idx
        )

    treatment_relapse_regimen = [
        f"esquema_tratamiento_{iterator}",
        f"motivo_inicio_tratamiento_{iterator}",
        f"tratamiento_recaida_fecha_inicio_{iterator}",
        f"tratamiento_recaida_fecha_fin_{iterator}",
        f"esquema_tratamiento_otros_{iterator}",
        f"recaida_motivo_discontinuacion_{iterator}",
        f"recaida_motivo_discontinuacion_describir_{iterator}",
        f"tratamiento_recaida_numero_ciclos__{iterator}",
        f"tratamiento_comentarios_{iterator}",
    ]
    if any(
        [
            data.get(i)
            for i in treatment_relapse_regimen
            if not i == f"tratamiento_recaida_numero_ciclos__{iterator}"
        ]
    ):
        regimen = models.MMRegimen(episode=episode, category="Relapse")
        populate_fields_on_model(
            regimen, file_name, treatment_relapse_regimen, data, loader, idx
        )

    treatment_relapse_response = [
        f"tratamiento_recaida_negativizacion_emr_{iterator}",
        f"tratamiento_recaida_respuesta_{iterator}",
        f"tratamiento_recaida_respuesta_fecha_{iterator}",
        f"tratamiento_recaida_progresion_fecha_{iterator}",
    ]
    if any([data.get(i) for i in treatment_relapse_response if not data.get(i) == "0"]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(
            response, file_name, treatment_relapse_response, data, loader, idx
        )

    if data.get(f"fiebre_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Fever")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["fiebre_comentarios_induccion_{iterator}"],
            data,
            loader,
            idx,
        )
    if data.get(f"fiebre_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Fever")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["fiebre_comentarios_toxicidades_{iterator}"],
            data,
            loader,
            idx,
        )

    if data.get(f"insuficiencia_renal_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Renal Failure")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["insuficiencia_renal_comentarios_induccion_{iterator}"],
            data,
            loader,
            idx,
        )
    if data.get(f"insuficiencia_renal_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Renal Failure")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["Insuficiencia_renal_comentarios_{iterator}"],
            data,
            loader,
            idx,
        )

    if data.get(f"hemorragias_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Hemorrhage")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["hemorragias_comentarios_induccion_{iterator}"],
            data,
            loader,
            idx,
        )

    if data.get(f"hemorragias_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Hemorrhage")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["hemorragias_comentarios_toxicidades_{iterator}"],
            data,
            loader,
            indexOf,
        )

    if data.get(f"neuropatia_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Neuropathy")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["neuropatia_comentarios_induccion_{iterator}"],
            data,
            loader,
            idx,
        )
    if data.get(f"neuropatia_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Neuropathy")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["neuropatia_comentarios_toxicidades_{iterator}"],
            data,
            loader,
            idx,
        )

    infection_comorbidity = [
        f"tipo_infeccion_induccion_{iterator}",
        f"tipo_infeccion_comentarios_induccion_{iterator}",
        f"tipo_infeccion_documentada_foco_induccion_{iterator}",
        f"tipo_infeccion_documentada_microorganismo_induccion_{iterator}",
    ]
    if any([data.get(i) for i in infection_comorbidity]):
        comorbidity = models.Comorbidity(episode=episode, condition="Infection")
        populate_fields_on_model(
            comorbidity, file_name, infection_comorbidity, data, loader, idx
        )

    other_toxicities_induction_comorbidity = [
        f"otras_toxicidades_induccion_{iterator}",
        f"otras_toxicidades_comentarios_induccion_{iterator}",
        f"otras_toxicidades_especificar_induccion_{iterator}",
    ]
    if any([data.get(i) for i in other_toxicities_induction_comorbidity]):
        comorbidity = models.Comorbidity(episode=episode, condition="Other")
        populate_fields_on_model(
            comorbidity,
            file_name,
            other_toxicities_induction_comorbidity,
            data,
            loader,
            idx,
        )

    other_toxicities_toxicites_comorbidity = [
        f"otras_toxicidades_toxicidades_{iterator}",
        f"otras_toxicidades_comentarios_toxicidades_{iterator}",
        f"otras_toxicidades_especificar_toxicidades_{iterator}",
    ]
    if any([data.get(i) for i in other_toxicities_toxicites_comorbidity]):
        comorbidity = models.Comorbidity(episode=episode, condition="Other")
        populate_fields_on_model(
            comorbidity,
            file_name,
            other_toxicities_toxicites_comorbidity,
            data,
            loader,
            idx,
        )

    bone_disease_fields = [
        f"tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_{iterator}",
        f"tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_{iterator}",
        f"tipo_tratamiento_enfermedad_osea_denosumab_induccion_{iterator}",
        f"tipo_tratamiento_enfermedad_osea_nodisponible_induccion_{iterator}",
        f"tipo_tratamiento_enfermedad_osea_otros_induccion_{iterator}",
        f"numero_ciclos_enfermedad_osea_induccion_{iterator}",
        f"indicar_bifosfonato_induccion_{iterator}",
        f"tipo_tratamiento_enfermedad_osea_describir_induccion_{iterator}",
        f"tratamiento_enfermedad_osea_fecha_ifin_induccion_{iterator}",
        f"tratamiento_enfermedad_osea_fecha_fin_induccion_{iterator}",
        f"tratamiento_enfermedad_osea_fecha_inicio_induccion_{iterator}",
        f"vertebroplastia_cifoplastia_comentarios_induccion_{iterator}",
        f"vertebroplastia_cifoplastia_fecha_induccion_{iterator}",
    ]
    if any([data.get(i) for i in bone_disease_fields if not data.get(i) == "0"]):
        treatment_type = None
        if data.get(
            f"tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_{iterator}"
        ):
            treatment_type = "Vertebroplasty Induction"
        elif data.get(
            f"tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_{iterator}"
        ):
            treatment_type = "Bisphosphonates Induction"
        elif data.get(
            f"tipo_tratamiento_enfermedad_osea_denosumab_induccion_{iterator}"
        ):
            treatment_type = "Denosumab"
        elif data.get(
            f"tipo_tratamiento_enfermedad_osea_nodisponible_induccion_{iterator}"
        ):
            treatment_type = "Not Available"
        elif data.get(f"tipo_tratamiento_enfermedad_osea_otros_induccion_{iterator}"):
            treatment_type = "Other Induction"
        bone_disease = models.BoneDisease(
            episode=episode, treatment_type=treatment_type
        )
        populate_fields_on_model(
            bone_disease, file_name, bone_disease_fields[5:], data, loader, idx
        )

    radiotherapy_fields = [
        f"radioterapia_induccion_fecha_fin_{iterator}",
        f"radioterapia_induccion_fecha_inicio_{iterator}",
    ]
    if any([data.get(i) for i in radiotherapy_fields]):
        radiotherapy = models.RadiotherapyInduction(episode=episode)
        populate_fields_on_model(
            radiotherapy, file_name, radiotherapy_fields, data, loader, idx
        )


def populate_mprotein_measurements_from_treatment(episode, file_name, iterator, data, loader, idx):
    m_protein_mesurements = [
        f"cuant_cadena_ligera_lambda_{iterator}",
        f"cociente_kappa_lambda_{iterator}",
        f"tipo_cadena_pesada_{iterator}",
        f"tipo_cadena_pesada_otros_{iterator}",
        f"cuant_cadena_ligera_kappa_{iterator}",
        f"cuant_monoclonal_serico_{iterator}",
        f"tipo_cadena_ligera_{iterator}",
    ]
    if any([data.get(i) for i in m_protein_mesurements if not data.get(i) == "0"]):
        date_fields = [
            "tratamiento_induccion_fecha_inicio_{iterator}",
            "tratamiento_induccion_fecha_fin_{iterator}",
            "radioterapia_induccion_fecha_inicio_{iterator}",
            "radioterapia_induccion_fecha_fin_{iterator}",
            "tratamiento_mantenimiento_fecha_fin_{iterator}",
            "tratamiento_mantenimiento_fecha_inicio_{iterator}",
            "tratamiento_recaida_fecha_inicio_{iterator}",
            "tratamiento_recaida_fecha_fin_{iterator}",
        ]
        # We don't have a date to use so we will use the highest
        # treatment date (start or end) available
        dates = [translate_date(data.get(i)) for i in date_fields if data.get(i)]
        protein_date = None
        if len(dates):
            if len(dates) == 1:
                protein_date = dates[0]
            protein_date = sorted(dates)[-1]
        m_protein = models.MProteinMesurements(
            date=protein_date,
            episode=episode,
        )
        populate_fields_on_model(m_protein, file_name, m_protein_mesurements, data, loader, idx)


def get_data(_file_to_read):
    with open(_file_to_read) as file_to_read:
        rows = rows = list(csv.DictReader(file_to_read))
    return rows


def get_patient_data_from_file(tmp_directory, file_name, patient_number):
    all_rows = get_data(os.path.join(tmp_directory, file_name))
    if "c�digo de paciente" in all_rows[0]:
        patient_number_field = "c�digo de paciente"
    else:
        patient_number_field = "C�digo de Paciente"
    for idx, row in enumerate(all_rows):
        if row[patient_number_field] == patient_number:
            return (
                idx,
                {k.lower(): v for k, v in row.items()},
            )


def extract_files(zipped_folder, tmp_directory):
    """
    Extracts the zipped_folder into the tmp_directory.
    Copies all csvs into the zipped_folder into the top level
    tmp_directory and deletes directories.

    e.g.
    If you were extracting zaragosa.zip which contained
    demographics.csv into tmp directory tmp_dir.
    It would create tmp_dir/zaragosa/demographics.csv
    It would then copy demographics.csv into tmp_dir/demographics.csv
    It would then remove tmp_dir/zargosa
    """
    with zipfile_py.ZipFile(zipped_folder) as zfolder:
        zfolder.extractall(tmp_directory)
        name_list = zfolder.namelist()
        for name in name_list:
            if not name.endswith('.csv'):
                continue
            shutil.copy(
                os.path.join(tmp_directory, name),
                os.path.join(tmp_directory, os.path.basename(name))
            )
        for name in os.listdir(tmp_directory):
            full_name = os.path.join(tmp_directory, name)
            if not full_name.endswith(".csv"):
                shutil.rmtree(full_name)


def _load_data(zipped_folder):
    with tempfile.TemporaryDirectory() as tmp_directory:
        extract_files(zipped_folder, tmp_directory)
        errors = check_files(tmp_directory, zipped_folder)
        if errors:
            return {
                "top_level_errors": errors,
                "row_errors": [],
            }

        demographics_rows = get_data(
            os.path.join(tmp_directory, "datos demograficos.csv")
        )
        loader = ZaragosaLoader()
        for idx, row in enumerate(demographics_rows):
            patient_number = loader.check_and_get_hospital_number(
                row, "c�digo de paciente", "datos demograficos.csv", idx
            )
            if not patient_number:
                continue
            patient, mm_episode = create_patient_episode(patient_number)

            create_datos_demographics(patient, mm_episode, row, idx, loader)
            idx, enfermedad_1_data = get_patient_data_from_file(
                tmp_directory, "datos enfermedad 1.csv", patient_number
            )
            create_datos_enfermedad(
                mm_episode,
                "datos enfermedad 1.csv",
                enfermedad_1_data,
                loader,
                idx,
                lab_test_date=translate_date(enfermedad_1_data["fecha_diagnostico_1"]),
                clinical_date=translate_date(enfermedad_1_data["fecha_diagnostico_1"]),
            )
            for i in range(2, 7):
                idx, enfermedad_data = get_patient_data_from_file(
                    tmp_directory, f"datos enfermedad {i}.csv", patient_number,
                )
                create_datos_enfermedad(
                    mm_episode,
                    f"datos enfermedad {i}.csv",
                    enfermedad_data,
                    loader,
                    idx,
                    lab_test_date=translate_date(
                        enfermedad_data[f"recaida_biologica_fecha_{i}"]
                    ),
                    clinical_date=translate_date(
                        enfermedad_data[f"recaida_clinica_fecha_{i}"]
                    ),
                )
                idx, actual_data = get_patient_data_from_file(
                    tmp_directory, "situacion actual.csv", patient_number
                )
                create_situation_actual(mm_episode, actual_data, loader, idx)
            for iterator in range(1, 7):
                file_name = f"tratamiento {iterator}.csv"
                idx, tratamiento = get_patient_data_from_file(
                    tmp_directory, file_name, patient_number
                )
                if treatment_populated(file_name, tratamiento):
                    lot_episode = patient.episode_set.create(
                        category_name=lot_episode_categories.LineOfTreatmentEpisode.display_name
                    )
                    create_tratiemento(lot_episode, iterator, tratamiento, loader, idx)
                populate_mprotein_measurements_from_treatment(
                    mm_episode, file_name, iterator, tratamiento, loader, idx
                )
    errors = loader.errors
    if errors:
        return {
            "top_level_errors": [],
            "row_errors": errors,
        }
    return {
        "top_level_errors": [],
        "row_errors": []
    }


def load_data(zipfile):
    errors = {}
    try:
        with transaction.atomic():
            errors = _load_data(zipfile)
            if errors["top_level_errors"] or errors["row_errors"]:
                raise LoadError("rolling back transaction")
    except LoadError:
        pass
    return errors
