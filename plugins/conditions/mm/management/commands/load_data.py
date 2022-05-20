import datetime
import csv
from re import I
from django.db import transaction
from django.db.models import DateField, FloatField
from plugins.conditions.mm import episode_categories
from entrytool import episode_categories as lot_episode_categories
from django.core.management.base import BaseCommand
from plugins.conditions.mm import models
from entrytool import models as entrytool_models
from .field_mapping import FIELD_MAPPING
from .translations import TRANSLATIONS
from opal.models import Patient
import os



def check_files(file_directory):
    """
    Check that we (case insensitively) have all the files
    that we need to load in the provided directory
    """
    expected_files = set([i[0].lower() for i in FIELD_MAPPING])
    found_files = set([i.lower() for i in os.listdir(file_directory)])
    missing_files = expected_files - found_files
    if len(missing_files):
        missing_files = sorted(list(missing_files))
        raise ValueError(f"{file_directory} does not contain {missing_files}")


def create_patient_episode(patient_number):
    patient = Patient.objects.create()
    patient.demographics().hospital_number = patient_number
    mm_episode = patient.episode_set.create(
        category_name=episode_categories.MM.display_name
    )
    return patient, mm_episode


def get_field_mapping(file_name, file_name_field):
    field_mapping = {(k[0].lower(), k[1].lower()): v for k, v in FIELD_MAPPING.items()}
    file_name = file_name.lower()
    file_name_field = file_name_field.lower()
    return field_mapping.get((file_name, file_name_field))


def is_date(subrecord, field_name):
    if not hasattr(subrecord, f"{field_name}_fk_id"):
        field = type(subrecord._meta.get_field(field_name))
        return field == DateField
    return False


def is_float(subrecord, field_name):
    if not hasattr(subrecord, f"{field_name}_fk_id"):
        field = type(subrecord._meta.get_field(field_name))
        return field == FloatField
    return False


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


def set_field(subrecord, field, value):
    if not value:
        return
    value = get_translation(value)
    if value.lower() == "y":
        value = "Yes"
    elif value.lower() == "n":
        value = "No"

    if is_date(subrecord, field):
        value = translate_date(value)
    elif is_float(subrecord, field):
        # floats are comma seperated e.g. 1,2 rather than 1.2
        splitted = value.split(",")
        if len(splitted) == 2:
            value = float(f"{splitted[0]}{splitted[1]}")
        else:
            value = float(splitted[0])

    if value:
        setattr(subrecord, field, value)


def create_datos_demographics(patient, episode, demographics_data):
    demographics = patient.demographics_set.all()[0]
    diagnosis_details = episode.mmdiagnosisdetails_set.all()[0]
    past_medical_history = patient.mmpastmedicalhistory_set.all()[0]
    for key, data in demographics_data.items():
        subrecord_name_and_field = get_field_mapping("datos demograficos.csv", key)
        if not subrecord_name_and_field:
            print(f"skipping datos demogrpahics {key}")
            continue
        subrecord_name, field = subrecord_name_and_field
        if subrecord_name == "MMDiagnosisDetails":
            set_field(diagnosis_details, field, data)
        elif subrecord_name == "MMPastMedicalHistory":
            set_field(past_medical_history, field, data)
        elif subrecord_name == "Demographics":
            set_field(demographics, field, data)
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


def set_subliassification(diagnosis_details, subclassification):
    """
    Takes in sublassification and sets heavy_chain_type and light_chain_type

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
    heavy_chain_type, light_chain_type = mapping[subclassification]
    diagnosis_details.heavy_chain_type = heavy_chain_type
    diagnosis_details.light_chain_type = light_chain_type


def create_datos_enfermedad(episode, file_name, data, clinical_date, lab_test_date):
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
            print(f"skipping datos enfermedad {key}")
            continue
        subrecord_name, field = subrecord_name_and_field
        if subrecord_name == "MMDiagnosisDetails":
            if field == 'subclassification':
                set_subliassification(diagnosis_details, value)
            else:
                set_field(diagnosis_details, field, value)
        elif subrecord_name == "ClinicalPresentation":
            set_field(clinical_presentation, field, value)
            clinical_presentation_populated = True
        elif subrecord_name == "LabTest" and value:
            set_field(lab_test, field, value)
            lab_test_populated = True
        elif subrecord_name == "Cytogenetics" and value:
            set_field(cytogenetics, field, value)
            cytogenetics_populated = True
        elif subrecord_name == "Imaging" and value:
            set_field(imaging, field, value)
            imaging_populated = True
        elif subrecord_name == "MProteinMesurements" and value:
            set_field(mproteinmesurements, field, value)
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


def create_situation_actual(episode, data):
    patient_status = episode.patient.mmpatientstatus_set.all()[0]
    file_name = "Situacion actual.csv"
    for key, value in data.items():
        subrecord_name_and_field = get_field_mapping(file_name, key)
        if not subrecord_name_and_field:
            print(f"skipping datos situation actual {key}")
            continue
        _, field = subrecord_name_and_field
        set_field(patient_status, field, value)
    patient_status.set_consistency_token()
    patient_status.save()


def populate_fields_on_model(model, file_name, upstream_fields, data):
    """
    For a list of upstream field names, iterate through the data
    find out what out field name is and set that field on the
    model provided, then save the model.
    """
    for upstream_field in upstream_fields:
        if (file_name, upstream_field) in FIELD_MAPPING:
            our_field = FIELD_MAPPING[(file_name, upstream_field)][1]
            set_field(model, our_field, data.get(upstream_field))
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
        if our_field_mapping[0] == 'MProteinMesurements':
            continue
        file_name = their_field_mapping[0]
        if file_name.lower() == file.lower():
            treatment_fields.append(their_field_mapping[1])
    populated = {
        i: row.get(i, "") for i in treatment_fields if not row.get(i, "") == '0'
    }
    # import ipdb; ipdb.set_trace()
    return any(
        row.get(i, "").strip() for i in treatment_fields if not row.get(i, "") == '0'
    )


def create_tratiemento(episode, iterator, data):
    file_name = f"tratamiento {iterator}.csv".lower()
    stuff = []

    eligible_for_stem_cell_transplant = [
        f"candidato_transplante_{iterator}",
    ]
    stuff.extend(eligible_for_stem_cell_transplant)
    alotph_fields = [
        f"acondicionamiento_alotph_{iterator}",
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
    if any([data.get(i) for i in alotph_fields if not data.get(i) == '0']):
        sct = entrytool_models.SCT(episode=episode, sct_type='Allogenic')
        populate_fields_on_model(sct, file_name, alotph_fields, data)

    # ALOTPH MMResponse
    if any([data.get(i) for i in alotph_reponse]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, alotph_reponse, data)

    # ATSP SCT
    if any([data.get(i) for i in atsp_fields if not data.get(i) == '0']):
        sct = entrytool_models.SCT(episode=episode, sct_type='Autologous')
        populate_fields_on_model(sct, file_name, atsp_fields, data)

    # ATSP MMResponse
    if any([data.get(i) for i in atsp_response]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, atsp_response, data)

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
        populate_fields_on_model(regimen, file_name, maintentance_regimen, data)

    # Maintenance response
    maintenance_response = [
        f"tecnica_emr2_{iterator}",  # i am inferring this belongs here based on its position in the filed
        f"negativizacion_emr_mantenimiento_{iterator}",
        f"negativizacion_emr_mantenimiento_fecha_{iterator}",
        f"mantenimiento_progresion_fecha_{iterator}",
        f"respuesta_despues_mantenimiento_{iterator}",
        f"respuesta_despues_mantenimiento_fecha_{iterator}",
    ]
    if any([data.get(i) for i in maintenance_response]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, maintenance_response, data)

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
        populate_fields_on_model(regimen, file_name, consolitation_regimen, data)

    # Consolidation response
    consolitation_response = [
        f"respuesta_despues_consolidacion_{iterator}",
        f"respuesta_despues_consolidacion_fecha_{iterator}",
        f"tecnica_emr_consolidacion_{iterator}",
        f"negativizacion_emr_consolidacion_fecha_{iterator}",
        f"negativizacion_emr_consolidacion_{iterator}",
    ]
    if any([data.get(i) for i in consolitation_response]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, consolitation_response, data)

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
        populate_fields_on_model(regimen, file_name, induction_regimen, data)

    induction_response = [
        f"tecnica_emr_induccion_{iterator}",
        f"fecha_progresion_induccion_{iterator}",
        f"negativizacion_emr_induccion_{iterator}",
        f"negativizacion_emr_induccion_fecha_{iterator}",
        f"respuesta_despues_induccion_{iterator}",
        f"respuesta_despues_induccion_fecha_{iterator}",
    ]

    if any(data.get(i) for i in induction_response):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, induction_response, data)

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
        populate_fields_on_model(regimen, file_name, treatment_relapse_regimen, data)

    treatment_relapse_response = [
        f"tratamiento_recaida_negativizacion_emr_{iterator}",
        f"tratamiento_recaida_respuesta_{iterator}",
        f"tratamiento_recaida_respuesta_fecha_{iterator}",
        f"tratamiento_recaida_progresion_fecha_{iterator}",
    ]
    if any([data.get(i) for i in treatment_relapse_response]):
        response = models.MMResponse(episode=episode)
        populate_fields_on_model(response, file_name, treatment_relapse_response, data)

    if data.get(f"fiebre_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Fever")
        populate_fields_on_model(
            comorbidity, file_name, ["fiebre_comentarios_induccion_{iterator}"], data
        )
    if data.get(f"fiebre_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Fever")
        populate_fields_on_model(
            comorbidity, file_name, ["fiebre_comentarios_toxicidades_{iterator}"], data
        )

    if data.get(f"insuficiencia_renal_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Renal Failure")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["insuficiencia_renal_comentarios_induccion_{iterator}"],
            data,
        )
    if data.get(f"insuficiencia_renal_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Renal Failure")
        populate_fields_on_model(
            comorbidity, file_name, ["Insuficiencia_renal_comentarios_{iterator}"], data
        )

    if data.get(f"hemorragias_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Hemorrhage")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["hemorragias_comentarios_induccion_{iterator}"],
            data,
        )

    if data.get(f"hemorragias_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Hemorrhage")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["hemorragias_comentarios_toxicidades_{iterator}"],
            data,
        )

    if data.get(f"neuropatia_induccion_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Neuropathy")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["neuropatia_comentarios_induccion_{iterator}"],
            data,
        )
    if data.get(f"neuropatia_toxicidades_{iterator}"):
        comorbidity = models.Comorbidity(episode=episode, condition="Neuropathy")
        populate_fields_on_model(
            comorbidity,
            file_name,
            ["neuropatia_comentarios_toxicidades_{iterator}"],
            data,
        )

    infection_comorbidity = [
        f"tipo_infeccion_induccion_{iterator}",
        f"tipo_infeccion_comentarios_induccion_{iterator}",
        f"tipo_infeccion_documentada_foco_induccion_{iterator}",
        f"tipo_infeccion_documentada_microorganismo_induccion_{iterator}",
    ]
    if any([data.get(i) for i in infection_comorbidity]):
        comorbidity = models.Comorbidity(episode=episode, condition="Infection")
        populate_fields_on_model(comorbidity, file_name, infection_comorbidity, data)

    other_toxicities_induction_comorbidity = [
        f"otras_toxicidades_induccion_{iterator}",
        f"otras_toxicidades_comentarios_induccion_{iterator}",
        f"otras_toxicidades_especificar_induccion_{iterator}",
    ]
    if any([data.get(i) for i in other_toxicities_induction_comorbidity]):
        comorbidity = models.Comorbidity(episode=episode, condition="Other")
        populate_fields_on_model(
            comorbidity, file_name, other_toxicities_induction_comorbidity, data
        )

    other_toxicities_toxicites_comorbidity = [
        f"otras_toxicidades_toxicidades_{iterator}",
        f"otras_toxicidades_comentarios_toxicidades_{iterator}",
        f"otras_toxicidades_especificar_toxicidades_{iterator}",
    ]
    if any([data.get(i) for i in other_toxicities_toxicites_comorbidity]):
        comorbidity = models.Comorbidity(episode=episode, condition="Other")
        populate_fields_on_model(
            comorbidity, file_name, other_toxicities_toxicites_comorbidity, data
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
    if any([data.get(i) for i in bone_disease_fields if not data.get(i) == '0']):
        treatment_type = None
        if data.get(
            f'tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_{iterator}'
        ):
            treatment_type = "Vertebroplasty Induction"
        elif data.get(
            f'tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_{iterator}'
        ):
            treatment_type = "Bisphosphonates Induction"
        elif data.get(
            f'tipo_tratamiento_enfermedad_osea_denosumab_induccion_{iterator}'
        ):
            treatment_type = "Denosumab"
        elif data.get(
            f'tipo_tratamiento_enfermedad_osea_nodisponible_induccion_{iterator}'
        ):
            treatment_type = "Not Available"
        elif data.get(
            f'tipo_tratamiento_enfermedad_osea_otros_induccion_{iterator}'
        ):
            treatment_type = "Other Induction"
        bone_disease = models.BoneDisease(
            episode=episode, treatment_type=treatment_type
        )
        populate_fields_on_model(bone_disease, file_name, bone_disease_fields[5:], data)

    radiotherapy_fields = [
        f"radioterapia_induccion_fecha_fin_{iterator}",
        f"radioterapia_induccion_fecha_inicio_{iterator}",
    ]
    if any([data.get(i) for i in radiotherapy_fields]):
        radiotherapy = models.RadiotherapyInduction(episode=episode)
        populate_fields_on_model(radiotherapy, file_name, radiotherapy_fields, data)


def populate_mprotein_measurements_from_treatment(episode, file_name, iterator, data):
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
        populate_fields_on_model(m_protein, file_name, m_protein_mesurements, data)


class Command(BaseCommand):
    help = "Load in the zaragosa data directory"

    def add_arguments(self, parser):
        parser.add_argument("file_directory")

    def get_data(self, file_name):
        with open(os.path.join(self.file_directory, file_name), encoding='utf-8') as f:
            rows = list(csv.DictReader(f))
        return rows

    def get_patient_data_from_file(self, file_name, patient_number):
        all_rows = self.get_data(file_name)
        if "c�digo de paciente" in all_rows[0]:
            patient_number_field = "c�digo de paciente"
        else:
            patient_number_field = "C�digo de Paciente"
        rows = [row for row in all_rows if row[patient_number_field] == patient_number]
        return {k.lower(): v for k, v in rows[0].items()}

    @transaction.atomic
    def handle(self, *args, **options):
        file_directory = options["file_directory"]
        check_files(file_directory)
        self.file_directory = file_directory
        demographics_rows = self.get_data("datos demograficos.csv")
        for row in demographics_rows:
            patient_number = row["c�digo de paciente"]
            patient, mm_episode = create_patient_episode(patient_number)
            create_datos_demographics(patient, mm_episode, row)
            enfermedad_1_data = self.get_patient_data_from_file(
                "datos enfermedad 1.csv", patient_number
            )
            create_datos_enfermedad(
                mm_episode,
                "datos enfermedad 1.csv",
                enfermedad_1_data,
                lab_test_date=translate_date(enfermedad_1_data["fecha_diagnostico_1"]),
                clinical_date=translate_date(enfermedad_1_data["fecha_diagnostico_1"]),
            )
            for i in range(2, 7):
                enfermedad_data = self.get_patient_data_from_file(
                    f"datos enfermedad {i}.csv", patient_number
                )
                create_datos_enfermedad(
                    mm_episode,
                    f"datos enfermedad {i}.csv",
                    enfermedad_data,
                    lab_test_date=translate_date(
                        enfermedad_data[f"recaida_biologica_fecha_{i}"]
                    ),
                    clinical_date=translate_date(
                        enfermedad_data[f"recaida_clinica_fecha_{i}"]
                    ),
                )
            actual_data = self.get_patient_data_from_file(
                "situacion actual.csv", patient_number
            )
            create_situation_actual(mm_episode, actual_data)
            for iterator in range(1, 7):
                file_name = f"tratamiento {iterator}.csv"
                tratamiento = self.get_patient_data_from_file(file_name, patient_number)
                if treatment_populated(file_name, tratamiento):
                    lot_episode = patient.episode_set.create(
                        category_name=lot_episode_categories.LineOfTreatmentEpisode.display_name
                    )
                    create_tratiemento(lot_episode, iterator, tratamiento)
                populate_mprotein_measurements_from_treatment(
                    mm_episode, file_name, iterator, tratamiento
                )
