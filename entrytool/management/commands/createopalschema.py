import os, psycopg2, logging

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            connection = self.get_opal_db_connection()
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("CREATE SCHEMA IF NOT EXISTS opal;")
        except (Exception, psycopg2.Error) as error:
            logging.error("Opal schema could not be created", error)

    def get_opal_db_connection(self):
        return psycopg2.connect(
            user=os.environ['OPAL_DB_USER'],
            password=os.environ['OPAL_DB_PASSWORD'],
            host=os.environ['OPAL_DB_HOST'],
            port=os.environ['OPAL_DB_PORT'],
            database=os.environ['OPAL_DB_NAME'])
