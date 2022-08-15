import csv
from plugins.data_load.load_utils import (
    cast_date, get_and_check, get_and_check_ll
)
from opal.models import Patient, Gender
from plugins.conditions.cll import episode_categories
from entrytool.models import PatientStatus


# field -> csv column title mapping
field_map = dict(
    # Demographics fields
    date_of_birth="date_of_birth",
    external_identifier="Hospital_patient_ID",
    sex="Gender",

    # Patient status fields
    death_date="date_of_death",
    death_cause="cause_of_death",

    # CLL diagnosis details
    hospital="Hospital",
    diag_date="date_of_diagnosis",
)


def load_data(file_name):
    with open(file_name, encoding="utf-8-sig") as f:
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

            patient_status = {
                "death_date": cast_date(row[field_map["death_date"]]),
                "death_cause": get_and_check(
                    row[field_map["death_cause"]], PatientStatus.DEATH_CAUSES
                )
            }
            patient = Patient.objects.create()
            episode = patient.create_episode(
                category_name=episode_categories.CLLCondition.display_name
            )
            patient_detail = patient.patientstatus_set.get()
            for i, v in patient_status.items():
                setattr(patient_detail, i, v)
            patient_detail.set_consistency_token()
            patient_detail.save()

            diagnosis_details = episode.clldiagnosisdetails_set.get()
            diagnosis_details_mapping = {
                "diag_date": cast_date(row[field_map["diag_date"]]),
                "hospital": row[field_map["hospital"]],
            }
            for i, v in diagnosis_details_mapping.items():
                setattr(diagnosis_details, i, v)
            diagnosis_details.set_consistency_token()
            diagnosis_details.save()

            demographics = patient.demographics()
            demographics.date_of_birth = date_of_birth
            demographics.external_identifier = external_identifier
            demographics.sex = sex
            demographics.set_consistency_token()
            demographics.save()
            demographics_saved += 1
