import csv
from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from opal.models import Patient
from entrytool.models import FollowUp
from entrytool.management.commands.load_utils import (
    translate_date, int_or_non
)

# field -> csv column title mapping
field_map = dict(

    # Demographics fields
    hospital_number="Hospital_patient_ID",

    # Follow up fields
    follow_up_date="followup_date",
    LDH="measurement1",
    beta2m="measurement2",
    albumin="measurement3",
    creatinin="measurement4",
    MCV="measurement5",
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
                    "LDH": int_or_non(follow_up_row[field_map["LDH"]]),
                    "beta2m": int_or_non(follow_up_row[field_map["beta2m"]]),
                    "albumin": int_or_non(follow_up_row[field_map["albumin"]]),
                    "creatinin": int_or_non(follow_up_row[field_map["creatinin"]]),
                    "MCV": int_or_non(follow_up_row[field_map["MCV"]]),
                }
                for k, v in followup_fields.items():
                    setattr(follow_up, k, v)
                follow_up.set_consistency_token()
                follow_up.save()
                saved += 1
        self.stdout.write(self.style.SUCCESS("Imported {} follow ups".format(saved)))



