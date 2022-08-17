import csv
import os
from plugins.data_load.load_utils import (
    cast_date, match_to_choice_if_possible, get_from_ll
)
from opal.models import Patient
from entrytool.models import Demographics
from opal.core.fields import ForeignKeyOrFreeText
import traceback


class Loader():
    def __init__(self, file_name):
        self.file_name = file_name
        self.errors = []
        self.idx = 1
        self.row = None

    def load_rows(self):
        with open(self.file_name, encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
            for idx, row in enumerate(rows):
                self.idx += 1
                self.row = row
                self.load_row(row)
        return self.errors

    def check_and_get_date(self, column):
        value = self.row[column]
        some_dt = None
        try:
            some_dt = cast_date(value)
        except Exception as err:
            self.errors.append(dict(
                file=self.file_name,
                row=self.idx,
                value=value,
                column=column,
                exception=err
            ))
        return some_dt

    def _check_fk_or_ft(self, model, field_name, value):
        field = getattr(model, field_name)
        result = get_from_ll(value, field.foreign_model)
        if result:
            return result
        if not result:
            field = model._get_field(f"{field_name}_ft")
            max_length = field.max_length
            if len(value) > max_length:
                raise ValueError(
                    f'Field is {len(value)} long and should be less than {max_length}'
                )
        return value

    def check_and_get_string(self, model, field_name, column):
        value = self.row[column]
        result = None
        if not value:
            return ""
        try:
            field = getattr(model, field_name)
            if isinstance(field, ForeignKeyOrFreeText):
                result = self._check_fk_or_ft(model, field_name, value)
                result = get_from_ll(value, field.foreign_model)
            else:
                field = model._meta.get_field(field_name)
                if field.choices:
                    result = match_to_choice_if_possible(value, field.choices)
            if not result:
                result = value
                max_length = field.max_length
                if len(result) > max_length:
                    raise ValueError(
                        f'Field is {len(value)} long and should be less than {max_length}'
                    )

        except Exception as err:
            self.errors.append(dict(
                file=self.file_name,
                row=self.idx,
                column=column,
                value=value,
                exception=err
            ))
        return result

    def check_and_get_patient_from_external_identifier(self, column):
        value = self.row[column]
        try:
            if not value:
                raise ValueError(
                    f"No external identifier found"
                )
        except Exception as err:
            self.errors.append(dict(
                file=self.file_name,
                row=self.idx,
                column=column,
                value=value,
                exception=err
            ))
            return
        hospital_number = self.check_and_get_string(
            Demographics, 'hospital_number', column
        )
        patient = None
        try:
            patient = Patient.objects.get(
                demographics__hospital_number=hospital_number
            )
        except Exception as err:
            self.errors.append(dict(
                file=self.file_name,
                row=self.idx,
                column=column,
                value=value,
                exception=err
            ))
        return patient

    def check_and_get_float(self, column):
        value = self.row[column]
        result = None
        try:
            result = float(value)
        except Exception as err:
            self.errors.append(dict(
                file=self.file_name,
                row=self.idx,
                column=column,
                value=value,
                exception=err
            ))
        return result

    def parse_errors(self):
        result = []
        for error in self.errors:
            result.append(dict(
                file=os.path.basename(error["file"]),
                row=error["row"],
                column=error["column"],
                value=error["value"],
                short_description=str(error["exception"]),
                traceback=traceback.format_tb(
                    error["exception"].__traceback__, limit=10
                )
            ))
        return result

    def load_row(self, row):
        raise NotImplementedError('Please implement this')
