import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from entrytool.load_utils import (
    cast_date, get_and_check, no_yes_unknown, get_and_check_ll
)
from entrytool.models import PatientDetails, Hospital
from opal.models import Patient, Gender


# field -> csv column title mapping
field_map = dict(

    # Demographics fields
    date_of_birth="date_of_birth",
    external_identifier="Hospital_patient_ID",
    sex="Gender",

    # Patient Detail fields
    status="status",
    hospital="Hospital",
    diag_date="date_of_diagnosis",
    smm_history="SMM_history",
    smm_history_date="SMM_History_date",
    mgus_history="MGUS_history",
    mgus_history_date="MGUS_history_date",
    iss_stage="ISS_stage",
    ds_stage="Durie_Salmon_Stage",
    pp_type="PP_type",
    del_17p="del17p",
    t4_14="t(4;14)(p16;q32)",
    t4_16="t_4_16",
    del_13="del13",
    death_date="date_of_death",
    death_cause="cause_of_death"
)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", help="Specify import file")

    @transaction.atomic()
    def handle(self, *args, **options):
        with open(options["file_name"], encoding="utf-8-sig") as f:
            demographics_saved = 0
            rows = list(csv.DictReader(f))
            for row in rows:
                # skip empty rows
                if not any(row.values()):
                    continue
                external_identifier = row[field_map["external_identifier"]].strip()
                if external_identifier:
                    patients = Patient.objects.filter(
                        demographics__external_identifier=external_identifier
                    )
                    if patients.exists():
                        raise ValueError(
                            "Patient {} already exists".format(external_identifier)
                        )
                date_of_birth = cast_date(row[field_map["date_of_birth"]])
                sex = get_and_check_ll(row[field_map["sex"]], Gender)

                patient_details = {
                    # "hospital": get_and_check_ll(row[field_map["hospital"]], Hospital),
                    "diag_date": cast_date(row[field_map["diag_date"]]),
                    "status": get_and_check(
                        row[field_map["status"]], PatientDetails.STATUSES
                    ),
                    # "smm_history": no_yes_unknown(row[field_map["smm_history"]]),
                    # "smm_history_date": cast_date(row[field_map["smm_history_date"]]),
                    # "mgus_history": no_yes_unknown(row[field_map["mgus_history"]]),
                    # "mgus_history_date": cast_date(row[field_map["mgus_history_date"]]),
                    "iss_stage": get_and_check(
                        row[field_map["iss_stage"]], PatientDetails.R_ISS_STAGES
                    ),
                    "ds_stage": get_and_check(
                        row[field_map["ds_stage"]], PatientDetails.R_ISS_STAGES
                    ),
                    # "pp_type": get_and_check(
                    #     row[field_map["pp_type"]], PatientDetails.PP_TYPE_CHOICES
                    # ),
                    "del_17p": no_yes_unknown(row[field_map["del_17p"]],),
                    "del_13": no_yes_unknown(row[field_map["del_13"]],),
                    "t4_14": no_yes_unknown(row[field_map["t4_14"]],),
                    # "t4_16": no_yes_unknown(row[field_map["t4_16"]],),
                    "death_date": cast_date(row[field_map["death_date"]]),
                    # "death_cause": get_and_check(
                    #     row[field_map["death_cause"]], PatientDetails.DEATH_CAUSES
                    # ),
                }
                patient = Patient.objects.create()
                patient.create_episode()
                patient_detail = patient.patientdetails_set.get()
                for i, v in patient_details.items():
                    setattr(patient_detail, i, v)
                patient_detail.set_consistency_token()
                patient_detail.save()
                demographics = patient.demographics()
                demographics.date_of_birth = date_of_birth
                demographics.external_identifier = external_identifier
                demographics.sex = sex
                demographics.set_consistency_token()
                demographics.save()
                demographics_saved += 1
            self.stdout.write(self.style.SUCCESS("Imported {} demographics".format(demographics_saved)))
