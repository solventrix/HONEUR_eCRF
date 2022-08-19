import os
import zipfile
from io import TextIOWrapper

from django.db import transaction
from plugins.data_load import load_demographics, load_followup, load_lot
from plugins.conditions.cll import episode_categories


class LoadError(Exception):
    pass


def load_data(folder):
    errors = []
    if not zipfile.is_zipfile(folder):
        raise ValueError(f'{folder} is not a zip file')
    try:
        with transaction.atomic():
            errors = _load_data(folder)
            if errors:
                raise LoadError("rolling back transaction")
    except LoadError:
        pass
    return errors


def _load_data(folder):
    if not zipfile.is_zipfile(folder):
        raise ValueError(f'{folder} is not a zip file')

    expected_file_names = [
        "demographics.csv", "lot.csv", "follow_ups.csv"
    ]

    with zipfile.ZipFile(folder) as zipped_folder:
        name_list = zipped_folder.namelist()
        # zipping a file can the file in with the folder path
        # ie the dummydata folder zipped, would have the
        # internal demographics.csv named dummydata/demographics.csv
        # so we just get the file from the basename.
        file_map = {}
        for expected_file_name in expected_file_names:
            found_files = [
                i for i in name_list if os.path.basename(i) == expected_file_name
            ]
            if not found_files:
                raise ValueError(
                    f'Unable to find {expected_file_name} in {folder}'
                )
            else:
                file_map[expected_file_name] = found_files[0]

        with zipped_folder.open(file_map["demographics.csv"]) as ftl:
            demographics_loader = load_demographics.DemographicsLoader(
                "demographics.csv", category=episode_categories.CLLCondition,
            )
            demographics_loader.load_rows(TextIOWrapper(ftl, "utf-8-sig"))
        with zipped_folder.open(file_map["lot.csv"]) as ftl:
            load_lot_loader = load_lot.LOTLoader("lot.csv")
            load_lot_loader.load_rows(TextIOWrapper(ftl, "utf-8-sig"))
        with zipped_folder.open(file_map["follow_ups.csv"]) as ftl:
            load_followup_loader = load_followup.FollowUpLoader("follow_ups.csv")
            load_followup_loader.load_rows(TextIOWrapper(ftl, "utf-8-sig"))

    return (
        demographics_loader.parse_errors()
        + load_lot_loader.parse_errors()
        + load_followup_loader.parse_errors()
    )
