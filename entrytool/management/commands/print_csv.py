"""
Example management command - print a CSV the name of which is given on the commandline.
"""
import csv

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    This class must be _named_ Command and inherit from BaseCommand
    Because, Django.
    """

    def add_arguments(self, parser):
        """
        The argument to this method is an argparse argument parser
        You can use it to create or alter commandline arguments for
        this management command.
        """
        parser.add_argument("file_name", help="Specify import file")

    def handle(self, *args, **kwargs):
        """
        The method that will be executed when the command is run
        """
        with open(kwargs["file_name"], encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
            self.process_rows(rows)

    def process_rows(self, rows):
        """
        This method will do the work we would like to perform.

        ROWS is a python list containting dictionaries representing
        one row from our CSV. We can access data using the CSV
        headers as keys.

        In this case we simply print each row.
        """
        for row in rows:
            print(row)
