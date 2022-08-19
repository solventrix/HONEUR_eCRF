from django.core.management.base import BaseCommand
from django.db import transaction
from plugins.data_load import load_data


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "zipped_folder",
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
        folder = options["zipped_folder"]
        errors = load_data.load_from_zipfile(folder)

        if errors:
            for error in errors:
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
