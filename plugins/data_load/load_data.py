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
                raise LoadError("rolling back transaction")
    except LoadError:
        pass
    return errors


def _load_data(folder):
    if not os.path.exists(folder):
        return [
            dict(
                file="N/A",
                row="N/A",
                column="N/A",
                value=folder,
                short_description="Unable to find folder on disk",
                traceback=["Please enter a file path to a folder on disk"],
            )
        ]
    files = os.listdir(folder)

    unable_to_find_file_errors = []
    for file_name in ["demographics.csv", "lot.csv", "follow_ups.csv"]:
        if file_name not in files:
            file_path = os.path.join(folder, file_name)
            unable_to_find_file_errors.append(dict(
                file="N/A",
                row="N/A",
                column="N/A",
                value=file_name,
                short_description=f"Unable to find a file on disk at {file_path}",
                traceback=[f"{file_name} must already exist on disk"],
            ))
    if len(unable_to_find_file_errors):
        return unable_to_find_file_errors

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
