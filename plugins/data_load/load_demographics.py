from opal.models import Patient
from ..conditions.cll.models import CLLDiagnosisDetails
from plugins.data_load import base_loader
from entrytool.models import Demographics, PatientLoad, PatientStatus


class DemographicsLoader(base_loader.Loader):
    def __init__(self, *args, category):
        super().__init__(*args)
        self.category = category

    def get_and_check_external_identifier(self, column):
        value = self.row[column]
        try:
            if not value:
                raise ValueError(f"No external identifier found for {value}")
            if value:
                patients = Patient.objects.filter(
                    demographics__external_identifier=value
                )
                if patients.exists():
                    raise ValueError("Patient {} already exists".format(value))
        except Exception as err:
            self.errors.append(
                dict(
                    file=self.file_name,
                    row=self.idx,
                    column=column,
                    value=value,
                    exception=err,
                )
            )
            return ""
        return self.check_and_get_string(Demographics, "hospital_number", column)

    def load_row(self, row):
        if not (any(row.values())):
            return
        external_identifier = self.get_and_check_external_identifier(
            "Hospital_patient_ID"
        )
        if not external_identifier:
            return
        patient = Patient.objects.create()
        demographics = patient.demographics()
        demographics.date_of_birth = self.check_and_get_date("date_of_birth")
        demographics.hospital_number = external_identifier
        demographics.sex = self.check_and_get_string(Demographics, "sex", "Gender")
        demographics.set_consistency_token()
        demographics.save()

        patient.patientload_set.update(
            source=PatientLoad.LOADED_FROM_FILE
        )
        episode = patient.create_episode(category_name=self.category.display_name)

        patient_status = patient.patientstatus_set.get()
        patient_status.death_date = self.check_and_get_date("date_of_death")
        patient_status.death_cause = self.check_and_get_string(
            PatientStatus, "death_cause", "cause_of_death"
        )
        patient_status.set_consistency_token()
        patient_status.save()

        diagnosis_details = episode.clldiagnosisdetails_set.get()
        diagnosis_details.diag_date = self.check_and_get_date("date_of_diagnosis")
        diagnosis_details.hospital = self.check_and_get_string(
            CLLDiagnosisDetails, "hospital", "Hospital"
        )
        diagnosis_details.set_consistency_token()
        diagnosis_details.save()
