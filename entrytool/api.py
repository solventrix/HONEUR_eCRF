from rest_framework import status
from plugins.data_load import load_data
from opal.core.api import LoginRequiredViewset
from opal.models import Patient, Episode
from opal.core.api import OPALRouter, patient_from_pk, episode_from_pk
from opal.core.views import json_response
from entrytool import models
from entrytool.episode_categories import LineOfTreatmentEpisode


class NewLineOfTreatmentEpisode(LoginRequiredViewset):
    model = Patient
    basename = "new_line_of_treatment_episode"

    @patient_from_pk
    def update(self, request, patient):
        profile = request.user.profile
        if profile.readonly:
            return json_response(
                {'error': 'User is read only'},
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        patient.episode_set.create(category_name=LineOfTreatmentEpisode.display_name)
        return json_response(True)


class DeleteLineOfTreatmentEpisode(LoginRequiredViewset):
    model = Episode
    basename = "delete_line_of_treatment_episode"

    @episode_from_pk
    def destroy(self, request, episode):
        profile = request.user.profile
        if profile.readonly:
            return json_response(
                {'error': 'User is read only'},
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        if not episode.category_name == LineOfTreatmentEpisode.display_name:
            return json_response(
                {'error': 'Unable to delete episode'},
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        episode.delete()
        return json_response(True)


class UnvalidatedPatients(LoginRequiredViewset):
    basename = "unvalidated_patients"

    def list(self, request):
        return json_response(list(Patient.objects.filter(
            patientload__validated=False,
            patientload__source=models.PatientLoad.LOADED_FROM_FILE
        ).values_list('id', flat=True)))


class PatientsWithErrors(LoginRequiredViewset):
    basename = "patients_with_errors"

    def list(self, request):
        return json_response(list(Patient.objects.filter(
            patientload__validated=True,
            patientload__has_errors=True,
            patientload__source=models.PatientLoad.LOADED_FROM_FILE
        ).values_list('id', flat=True)))


class UploadFromFilePath(LoginRequiredViewset):
    basename = "upload_from_file_path"

    def create(self, request):
        folder = request.FILES.get('folder')
        errors = load_data.load_data(folder)
        return json_response(errors)


entrytool_router = OPALRouter()
entrytool_router.register(
    NewLineOfTreatmentEpisode.basename, NewLineOfTreatmentEpisode
)
entrytool_router.register(
    DeleteLineOfTreatmentEpisode.basename, DeleteLineOfTreatmentEpisode
)
entrytool_router.register(
    UnvalidatedPatients.basename, UnvalidatedPatients
)
entrytool_router.register(
    PatientsWithErrors.basename, PatientsWithErrors
)
entrytool_router.register(
    UploadFromFilePath.basename, UploadFromFilePath
)
