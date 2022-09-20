from plugins.conditions.mm.load_data import treatment_populated

from django.core.management.base import BaseCommand
from plugins.conditions.mm import load_data


class Command(BaseCommand):
    help = "Load in the zaragosa data directory"

    def add_arguments(self, parser):
        parser.add_argument("file_directory")

    def handle(self, *args, **options):
        file_directory = options["file_directory"]
        load_data.load_data(file_directory)
