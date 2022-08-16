import os
from django.db import transaction
from plugins.data_load import load_demographics, load_followup, load_lot
from plugins.conditions.cll import episode_categories


class LoadError(Exception):
    pass


def load_data(folder):
    errors = []
    try:
        with transaction.atomic():
            errors = _load_data(folder)
            if errors:
                raise LoadError('rolling back transaction')
    except LoadError:
        pass
    return errors


def _load_data(folder):
    files = os.listdir(folder)

    for file_name in ["demographics.csv", "lot.csv", "follow_ups.csv"]:
        if file_name not in files:
            raise ValueError(f'Unable to find {file_name} in {options["folder"]}')

    demographics_loader = load_demographics.DemographicsLoader(
        os.path.join(folder, "demographics.csv"),
        category=episode_categories.CLLCondition,
    )
    demographics_loader.load_rows()

    load_lot_loader = load_lot.LOTLoader(os.path.join(folder, "lot.csv"))
    load_lot_loader.load_rows()

    load_followup_loader = load_followup.FollowUpLoader(
        os.path.join(folder, "follow_ups.csv")
    )
    load_followup_loader.load_rows()

    errors = (
        demographics_loader.parse_errors()
        + load_lot_loader.parse_errors()
        + load_followup_loader.parse_errors()
    )
    return errors
