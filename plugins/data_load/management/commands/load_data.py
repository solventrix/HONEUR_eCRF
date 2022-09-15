from django.core.management.base import BaseCommand
from django.db import transaction
from plugins.data_load import load_data


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
        errors = load_data.load_data(folder)

        if errors:
            if "top_level_errors" in errors:
                for error in errors["top_level_errors"]:
                    self.stderr.write(error)
            for error in errors.get("row_errors", []):
                self.stderr.write("Error")
                for title, value in error.items():
                    if title == "traceback":
                        if not options["verbose"]:
                            continue
                        else:
                            self.stderr.write("Traceback")
                            for row in value:
                                for line in row.split("\n"):
                                    self.stderr.write(line)
                    else:
                        self.stderr.write(f"{title.title()}: {value}")
                self.stderr.write("")
            raise ValueError("Unable to process files, rolling back the transaction")
