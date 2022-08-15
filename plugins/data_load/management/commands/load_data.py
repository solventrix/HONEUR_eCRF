import os
from django.core.management.base import BaseCommand
from django.db import transaction
from plugins.data_load import load_demographics, load_followup, load_lot

LOAD_MAPPING = {
    "demographics.csv": load_demographics.load_data,
    "lot.csv": load_lot.load_data,
    "follow_ups.csv": load_followup.load_data,
}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "folder",
            help="Specify a folder with a demographics.csv, follow_ups.csv and lot.csv",
        )

    @transaction.atomic()
    def handle(self, *args, **options):
        provided_files = os.listdir(options["folder"])

        for file_name in LOAD_MAPPING.keys():
            if file_name not in provided_files:
                raise ValueError(f'Unable to find {file_name} in {options["folder"]}')

        for file_name, loader in LOAD_MAPPING.items():
            full_file_path = os.path.join(options["folder"], file_name)
            loader(full_file_path)
