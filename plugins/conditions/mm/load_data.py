import io
import datetime
from django.utils.translation import gettext as _
from opal.models import Patient
from entrytool.models import Demographics
from plugins.data_load.base_loader import Loader as BaseLoader
from django.db import transaction
from plugins.data_load.load_data import LoadError
from plugins.conditions.mm import episode_categories


class CologneLoader(BaseLoader):
    def get_and_check_external_identifier(self, column):
        value = self.row[column]
        try:
            if not value:
                raise ValueError(
                    _("No external identifier found for %s") % value
                )
            if value:
                patients = Patient.objects.filter(
                    demographics__hospital_number=value
                )
                if patients.exists():
                    raise ValueError(_("Patient %s already exists") % value)
        except Exception as err:
            self.add_error(column, value, str(err))
            return ""

        return self.check_and_get_string(Demographics, "hospital_number", column)

    def check_and_get_date(self, column):
        value = self.row[column]
        some_dt = None
        try:
            some_dt = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except Exception:
            description = _("Unable to parse %s into a date with the formats dd/mm/yyyy or yyyy-mm-dd") % value
            self.add_error(column, value, description)
        return some_dt

    def load_row(self, data):
        hospital_number = self.get_and_check_external_identifier("patienten-nr.")
        if not hospital_number:
            return
        date_of_birth = self.check_and_get_date('geburtsdatum')
        gender_string = data["geschlecht"]
        gender = None
        if gender_string == "w":
            gender = "Female"
        elif gender_string == "m":
            gender = "Male"
        patient = Patient.objects.create()
        demographics = patient.demographics_set.get()
        demographics.hospital_number = hospital_number
        demographics.date_of_birth = date_of_birth
        demographics.sex = gender
        demographics.save()
        patient.episode_set.create(
            category_name=episode_categories.MM.display_name
        )


def _load_data(csv_file):
    if not csv_file.name.endswith('.csv'):
        return {
            "top_level_errors": [_('Please upload a csv file')],
            "row_errors": []
        }
    loader = CologneLoader(csv_file.name)
    file = csv_file.read().decode('utf-8')
    errors = loader.load_rows(io.StringIO(file))
    return {
        "top_level_errors": [],
        "row_errors": errors
    }


def load_data(csv_file):
    errors = {}
    try:
        with transaction.atomic():
            errors = _load_data(csv_file)
            if errors["top_level_errors"] or errors["row_errors"]:
                raise LoadError("rolling back transaction")
    except LoadError:
        pass
    return errors
