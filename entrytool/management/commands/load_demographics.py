import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from entrytool.management.commands.load_utils import (
    translate_date, get_and_check, no_yes_unknown, get_or_create_ll
)
from entrytool.models import PatientDetails, Hospital
from opal.models import Patient


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
                hospital_number = row["Hospital_patient_ID"].strip()
                if hospital_number:
                    patients = Patient.objects.filter(
                        demographics__hospital_number=hospital_number
                    )
                    if patients.exists():
                        raise ValueError(
                            "Patient {} already exists".format(hospital_number)
                        )
                date_of_birth = translate_date(row["date_of_birth"])

                patient_details = {
                    "hospital": get_or_create_ll(row["Hospital"], Hospital),
                    "diag_date": translate_date(row["date_of_diagnosis"]),
                    "smm_history": no_yes_unknown(row["SMM_history"]),
                    "smm_history_date": translate_date(row["SMM_History_date"]),
                    "mgus_history": no_yes_unknown(row["MGUS_history"]),
                    "mgus_history_date": translate_date(row["MGUS_history_date"]),
                    "r_iss_stage": no_yes_unknown(row["R_ISS_stage"]),
                    "pp_type": get_and_check(
                        row["PP_type"], PatientDetails.PP_TYPE_CHOICES
                    ),
                    "del_17p": no_yes_unknown(row["Del17p"]),
                    "t4_14": no_yes_unknown(row["t_4_14"]),
                    "t4_16": no_yes_unknown(row["t_4_16"]),
                    "death_date": translate_date(row["date_of_death"]),
                    "death_cause": get_and_check(
                        row["cause_of_death"], PatientDetails.DEATH_CAUSES
                    ),
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
                demographics.hospital_number = hospital_number
                demographics.set_consistency_token()
                demographics.save()
                demographics_saved += 1
            self.stdout.write(self.style.SUCCESS("Imported {} demographics".format(demographics_saved)))
