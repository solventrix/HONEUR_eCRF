import os
import zipfile
import chardet
from django.utils.translation import gettext as _
from io import TextIOWrapper

from django.db import transaction
from plugins.data_load import load_demographics, load_followup, load_lot
from plugins.conditions.cll import episode_categories


class LoadError(Exception):
    pass


def load_data(zipfile):
    errors = {}
    try:
        with transaction.atomic():
            errors = _load_data(zipflie)
            if errors["top_level_errors"] or errors["row_errors"]:
                raise LoadError("rolling back transaction")
    except LoadError:
        pass
    return errors


def is_utf8(zipfile, file_name):
    detect_report = chardet.detect(zipfile.read(file_name))
    encoding = detect_report['encoding']
    if encoding.lower() == 'utf-8' or encoding.lower() == 'utf-8-sig':
        if detect_report['confidence'] >= 0.99:
            return True
    return False


def get_encoding(zipfile, file_name):
    detect_report = chardet.detect(zipfile.read(file_name))
    return detect_report['encoding']


def _load_data(zipfile):

    # These are errors like not being able to read the file
    # or a missing file etc
    top_level_errors = []
    if not zipfile.is_zipfile(zipfile):
        # note f-strings are not yet supported by xgettext
        top_level_errors.append(
            _('%s is not a zip file' % zipfile)
        )
        return {
            "top_level_errors": top_level_errors,
            "row_errors": []
        }

    expected_file_names = [
        "demographics.csv", "lot.csv", "follow_ups.csv"
    ]

    with zipfile.ZipFile(zipfile) as zipped_folder:
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
                top_level_errors.append(
                    _('Unable to find %(expected_file_name)s in %(folder)s' % {
                        'expected_file_name': expected_file_name, 'folder': folder
                    })
                )
            else:
                if not is_utf8(zipped_folder, found_files[0]):
                    top_level_errors.append(
                        _('%s is not utf-8 encoded' % expected_file_name)
                    )
                file_map[expected_file_name] = found_files[0]

        if top_level_errors:
            return {
                "top_level_errors": top_level_errors,
                "row_errors": []
            }

        with zipped_folder.open(file_map["demographics.csv"]) as ftl:
            demographics_loader = load_demographics.DemographicsLoader(
                "demographics.csv", category=episode_categories.CLLCondition,
            )
            demographics_loader.load_rows(
                TextIOWrapper(ftl, get_encoding(
                    zipped_folder, file_map["demographics.csv"])
                )
            )
        with zipped_folder.open(file_map["lot.csv"]) as ftl:
            load_lot_loader = load_lot.LOTLoader("lot.csv")
            load_lot_loader.load_rows(
                TextIOWrapper(ftl, get_encoding(
                    zipped_folder, file_map["lot.csv"])
                )
            )
        with zipped_folder.open(file_map["follow_ups.csv"]) as ftl:
            load_followup_loader = load_followup.FollowUpLoader("follow_ups.csv")
            load_followup_loader.load_rows(
                TextIOWrapper(ftl, get_encoding(
                    zipped_folder, file_map["follow_ups.csv"])
                )
            )

    errors = (
        demographics_loader.errors
        + load_lot_loader.errors
        + load_followup_loader.errors
    )
    if errors:
        return {
            "top_level_errors": [],
            "row_errors": errors,
        }
    return {
        "top_level_errors": [],
        "row_errors": []
    }
