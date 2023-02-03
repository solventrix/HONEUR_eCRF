from django.core.management.base import BaseCommand
from django.db import transaction
from plugins.data_load import load_data
import logging
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
        logger = logging.getLogger(__name__)
        file = options["file"]
        errors = load_data.load_data(file)

        if errors:
            if "top_level_errors" in errors:
                for error in errors["top_level_errors"]:
                    logger.error(error)
            for error in errors.get("row_errors", []):
                logger.error("Error")
                for title, value in error.items():
                    if title == "traceback":
                        if not options["verbose"]:
                            continue
                        else:
                            logger.error("Traceback")
                            for row in value:
                                for line in row.split("\n"):
                                    logger.error(line)
                    else:
                        logger.error(f"{title.title()}: {value}")
                logger.error("")
            raise ValueError("Unable to process files, rolling back the transaction")
