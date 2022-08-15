import csv
from collections import defaultdict
from opal.models import Patient
from entrytool import episode_categories
from entrytool.models import SCT
from plugins.conditions.cll import models as cll_models
from plugins.data_load.load_utils import (
    cast_date,
    get_and_check,
    get_and_check_ll,
)


# db field -> csv column title mapping
field_map = dict(
    # lot number, not stored in our db just used as a grouping identifier
    lot="LOT",
    # Demographics fields
    external_identifier="Hospital_patient_ID",
    # CLLRegimen fields
    regimen="Regimen",
    category="category",
    start_date="Start_date",
    end_date="end_date",
    cycles="cycles",
    stop_reason="stop_reason",
    # BestResponse fields
    response_date="response_date",
    response="response",
    # SCT fields
    sct_date="SCT_date",
    sct_type="SCT_type",
)


def load_data(file_name):
    by_lot = defaultdict(list)
    with open(file_name, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
        for row in rows:
            # skip empty rows
            if not (any(row.values())):
                continue

            hn = row[field_map["external_identifier"]].strip()
            lot_number = row[field_map["lot"]].strip()
            if not hn or not lot_number:
                raise ValueError("hospital number and lot number are required")

            by_lot[
                (
                    hn,
                    lot_number,
                )
            ].append(row)
    regimen_saved = 0
    response_saved = 0
    sct_saved = 0

    for key, treatment_lots in by_lot.items():
        hn = key[0]
        patient = Patient.objects.get(demographics__external_identifier=hn)
        episode = patient.episode_set.create(
            category_name=episode_categories.LineOfTreatmentEpisode.display_name
        )

        for treatment_lot in treatment_lots:
            regimen_fields = {
                "regimen": get_and_check_ll(
                    treatment_lot[field_map["regimen"]], cll_models.CLLRegimenList
                ),
                # "category": get_and_check(
                #     treatment_lot[field_map["category"]],
                #     Regimen.REGIMEN_TYPES
                # ),
                "start_date": cast_date(treatment_lot[field_map["start_date"]]),
                "end_date": cast_date(treatment_lot[field_map["end_date"]]),
                # "nbCycles": int_or_none(treatment_lot[field_map["cycles"]]),
                # "stop_reason": get_and_check_ll(
                #     treatment_lot[field_map["stop_reason"]], StopReason
                # ),
            }
            if any(regimen_fields.values()):
                regimen = cll_models.CLLRegimen(episode=episode)
                for k, v in regimen_fields.items():
                    setattr(regimen, k, v)
                regimen.set_consistency_token()
                regimen.save()
                regimen_saved += 1

            response_fields = {
                "response_date": cast_date(treatment_lot[field_map["response_date"]]),
                "response": get_and_check(
                    treatment_lot[field_map["response"]],
                    cll_models.BestResponse.RESPONSES_IWCLL,
                ),
            }
            if any(response_fields.values()):
                response = cll_models.BestResponse(episode=episode)
                for k, v in response_fields.items():
                    setattr(response, k, v)
                response.set_consistency_token()
                response.save()
                response_saved += 1

            sct_fields = {
                "sct_date": cast_date(treatment_lot[field_map["sct_date"]]),
                "sct_type": get_and_check(
                    treatment_lot[field_map["sct_type"]], SCT.SCT_TYPES
                ),
            }
            if any(sct_fields.values()):
                sct = SCT(episode=episode)
                for k, v in sct_fields.items():
                    setattr(sct, k, v)
                sct.set_consistency_token()
                sct.save()
                sct_saved += 1
