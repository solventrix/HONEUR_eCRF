from django.core.management.base import BaseCommand
from django.utils.module_loading import import_string
from django.conf import settings
from django.db import transaction


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "file",
            help="Specify a file with the data to load",
        )
        parser.add_argument(
            '--verbose',
            help="Print the full stack trace of the errors",
            action="store_true",
            dest="verbose"
        )

    @transaction.atomic()
    def handle(self, *args, **options):
        file = options["file"]
        load_data = import_string(settings.UPLOAD_FROM_FILE_FUNCTION)
        errors = load_data(file)

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
