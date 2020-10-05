import csv
from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from opal.models import Patient
from entrytool.models import FollowUp
from entrytool.management.commands.load_utils import (
    translate_date, int_or_non
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
                hn = row["Hospital_patient_ID"].strip()
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
                    "follow_up_date": translate_date(follow_up_row["followup_date"]),
                    "LDH": int_or_non(follow_up_row["measurement1"]),
                    "beta2m": int_or_non(follow_up_row["measurement2"]),
                    "albumin": int_or_non(follow_up_row["measurement3"]),
                    "creatinin": int_or_non(follow_up_row["measurement4"]),
                    "MCV": int_or_non(follow_up_row["measurement5"]),
                }
                for k, v in followup_fields.items():
                    setattr(follow_up, k, v)
                follow_up.set_consistency_token()
                follow_up.save()
                saved += 1
        self.stdout.write(self.style.SUCCESS("Imported {} follow ups".format(saved)))



