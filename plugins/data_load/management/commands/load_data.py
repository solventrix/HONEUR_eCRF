import os
import traceback
from django.core.management.base import BaseCommand
from django.db import transaction
from plugins.data_load import load_demographics, load_followup, load_lot
from plugins.conditions.cll import episode_categories


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "folder",
            help="Specify a folder with a demographics.csv, follow_ups.csv and lot.csv",
        )
        parser.add_argument(
            '--verbose',
            help="Print the full stack trace of the errors",
            action="store_true",
            dest="verbose"
        )

    @transaction.atomic()
    def handle(self, *args, **options):
        folder = options["folder"]
        files = os.listdir(options["folder"])

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

        if errors:
            for error in errors:
                to_print = error
                if not options["verbose"]:
                    to_print = {i: v for i, v in error.items() if not i == "traceback"}
                else:
                    self.stderr.write(str(to_print))
            raise ValueError("Unable to process files, rolling back the transaction")
