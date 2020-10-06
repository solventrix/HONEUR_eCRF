import csv
from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from opal.models import Patient
from entrytool.models import FollowUp, Hospital
from entrytool.load_utils import (
    translate_date, float_or_none, get_and_check_ll
)

# field -> csv column title mapping
field_map = dict(

    # Demographics fields
    hospital_number="Hospital_patient_ID",

    # Follow up fields
    follow_up_date="followup_date",
    LDH="LDH",
    beta2m="beta2m",
    albumin="albumin",
    creatinin="creatinin",
    MCV="MCV",
    Hb="Hb",
    kappa_lambda_ratio="kappa_lambda_ratio",
    bone_lesions="bone_lesions",
    hospital="hospital"
)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", help="Specify import file")

    @transaction.atomic()
    def handle(self, *args, **options):
        by_hospital_number = defaultdict(list)
        saved = 0
        with open(options["file_name"], encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
            for row in rows:
                # empty row, skip it
                if not any(row.values()):
                    continue
                hn = row[field_map["hospital_number"]].strip()
                if not hn:
                    raise ValueError('hospital number is required for the follow up load')
                by_hospital_number[hn].append(row)

        for hn, followups in by_hospital_number.items():
            for follow_up_row in followups:
                patient = Patient.objects.get(
                    demographics__hospital_number=hn
                )
                follow_up = FollowUp(patient=patient)
                followup_fields = {
                    "follow_up_date": translate_date(follow_up_row[field_map["follow_up_date"]]),
                    "LDH": float_or_none(follow_up_row[field_map["LDH"]]),
                    "beta2m": float_or_none(follow_up_row[field_map["beta2m"]]),
                    "albumin": float_or_none(follow_up_row[field_map["albumin"]]),
                    "creatinin": float_or_none(follow_up_row[field_map["creatinin"]]),
                    "MCV": float_or_none(follow_up_row[field_map["MCV"]]),
                    "Hb": float_or_none(follow_up_row[field_map["Hb"]]),
                    "kappa_lambda_ratio": float_or_none(follow_up_row[field_map["kappa_lambda_ratio"]]),
                    "bone_lesions": float_or_none(follow_up_row[field_map["bone_lesions"]]),
                    "hospital": get_and_check_ll(row[field_map["hospital"]], Hospital),
                }
                for k, v in followup_fields.items():
                    setattr(follow_up, k, v)
                follow_up.set_consistency_token()
                follow_up.save()
                saved += 1
        self.stdout.write(self.style.SUCCESS("Imported {} follow ups".format(saved)))



