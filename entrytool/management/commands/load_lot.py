import csv
from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from opal.models import Patient
from entrytool import episode_categories
from entrytool.models import (
    Regimen, StopReason, AEList, AdverseEvent, Response, SCT
)
from entrytool.management.commands.load_utils import (
    translate_date, get_and_check, get_and_check_ll, int_or_non
)


def get_severity(some_value):
    some_value = some_value.strip()
    if not some_value:
        return
    options = [i[0] for i in AdverseEvent.SEV_CHOICES]
    return options[int(some_value)-1]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", help="Specify import file")

    @transaction.atomic()
    def handle(self, *args, **options):
        by_lot = defaultdict(list)
        with open(options["file_name"], encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
            for row in rows:
                # skip empty rows
                if not(any(row.values())):
                    continue

                hn = row["Hospital_patient_ID"].strip()
                lot_number = row["LOT"].strip()
                if not hn or not lot_number:
                    raise ValueError('hospital number and lot number are required')

                by_lot[(hn, lot_number,)].append(row)

        for key, treatment_lots in by_lot.items():
            hn = key[0]
            patient = Patient.objects.get(
                demographics__hospital_number=hn
            )
            episode = patient.episode_set.create(
                category_name=episode_categories.LineOfTreatmentEpisode.display_name
            )
            for treatment_lot in treatment_lots:
                regimen_fields = {
                    "regimen": get_and_check(
                        treatment_lot["Regimen"], Regimen.REGIMEN_TYPES
                    ),
                    "start_date": translate_date(treatment_lot["Start_date"]),
                    "end_date": translate_date(treatment_lot["end_date"]),
                    "cycles": int_or_non(treatment_lot["cycles"]),
                    "stop_reason": get_and_check_ll(treatment_lot["stop_reason"], StopReason),
                }
                if any(regimen_fields.values()):
                    regimen = Regimen(episode=episode)
                    for k, v in regimen_fields.items():
                        setattr(regimen, k, v)
                    regimen.set_consistency_token()
                    regimen.save()

                response_fields = {
                    "response_date": translate_date(treatment_lot["response_date"]),
                    "response": get_and_check(treatment_lot["response"], Response.responses)
                }
                if any(response_fields.values()):
                    response = Response(episode=episode)
                    for k, v in response_fields.items():
                        setattr(response, k, v)
                    response.set_consistency_token()
                    response.save()

                ae_fields = {
                    "adverse_event": get_and_check_ll(treatment_lot["AE"], AEList),
                    "ae_date": translate_date(treatment_lot["AE_date"]),
                    "severity": get_severity(treatment_lot["AE_severity"])
                }

                if any(ae_fields.values()):
                    ae = AdverseEvent(episode=episode)
                    for k, v in ae_fields.items():
                        setattr(ae, k, v)
                    ae.set_consistency_token()
                    ae.save()

                sct_fields = {
                    "sct_date": translate_date(treatment_lot["SCT_date"]),
                    "sct_type": get_and_check(treatment_lot["SCT_type"], SCT.SCT_TYPES)
                }
                if any(sct_fields.values()):
                    sct = SCT(episode=episode)
                    for k, v in sct_fields.items():
                        setattr(sct, k, v)
                    sct.set_consistency_token()
                    sct.save()

