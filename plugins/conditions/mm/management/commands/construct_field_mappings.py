import csv
from django.core.management.base import BaseCommand
import pprint
from opal.core import subrecords

FILE_LOCATION = "/Users/fredkingham/Documents/field_translations/zaragosa_scan_with_notes_2/Field Overview-Table 1.csv"

TO_SKIP = set([
    "LabTest.date, MProteinMesurements.date",
    "PatientStatus.response_at_last_visit",
    'Imaging.date, Review.date',
    'Map out of treatment into LOT.MProteinMesurements',
])


def is_fk_or_ft(model, field_name):
    if hasattr(model, f"{field_name}_fk_id") and hasattr(model, f"{field_name}_ft"):
        return True
    return False


def read_file():
    with open(FILE_LOCATION) as f:
        result = list(csv.DictReader(f))
    return result


def create_tuples():
    file_data = read_file()
    result = {}
    for row in file_data:
        if not row["Ignore"] and row["Table"]:
            result[(row["Table"], row["Field"],)] = tuple(row["Field mapping"].split("."))
    formatted = pprint.pformat(result)
    with open("field_mapping.py", "w") as f:
        f.write(formatted)


def create_translations():
    file_data = read_file()
    result = set()
    for row in file_data:
        if not row["Ignore"] and row["Table"]:
            if row["Field mapping"].strip() in TO_SKIP:
                continue

            if not len(row["Field mapping"].split(".")) == 2:
                import ipdb; ipdb.set_trace()
            our_model_name, our_field = row["Field mapping"].split(".")
            our_field = our_field.strip()
            our_model_name = our_model_name.strip()
            try:
                subrecord = subrecords.get_subrecord_from_model_name(our_model_name)
            except:
                import ipdb; ipdb.set_trace()
                raise
            if is_fk_or_ft(subrecord, our_field):
                continue
            try:
                our_field = subrecord._meta.get_field(our_field)
            except:
                import ipdb; ipdb.set_trace()
                raise

            for choice in our_field.choices:
                result.add(("", choice[0],))
    formatted = pprint.pformat(sorted(list(result), key=lambda x: x[1]))
    with open("translations.py", "w") as f:
        f.write(formatted)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_translations()
        # create_tuples()
