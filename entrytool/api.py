from rest_framework import status
from opal.core.api import LoginRequiredViewset
from opal.models import Patient, Episode
from opal.core.api import OPALRouter, patient_from_pk, episode_from_pk
from opal.core.views import json_response
from entrytool import models
from entrytool.episode_categories import LineOfTreatmentEpisode


class NewLineOfTreatmentEpisode(LoginRequiredViewset):
    model = Patient
    base_name = "new_line_of_treatment_episode"

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
    base_name = "delete_line_of_treatment_episode"

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
    base_name = "unvalidated_patients"

    def list(self, request):
        return json_response(list(Patient.objects.filter(
            patientload__validated=False,
            patientload__source=models.PatientLoad.LOADED_FROM_FILE
        ).values_list('id', flat=True)))


class PatientsWithErrors(LoginRequiredViewset):
    base_name = "patients_with_errors"

    def list(self, request):
        return json_response(list(Patient.objects.filter(
            patientload__validated=True,
            patientload__has_errors=True,
            patientload__source=models.PatientLoad.LOADED_FROM_FILE
        ).values_list('id', flat=True)))


entrytool_router = OPALRouter()
entrytool_router.register(
    NewLineOfTreatmentEpisode.base_name, NewLineOfTreatmentEpisode
)
entrytool_router.register(
    DeleteLineOfTreatmentEpisode.base_name, DeleteLineOfTreatmentEpisode
)
entrytool_router.register(
    UnvalidatedPatients.base_name, UnvalidatedPatients
)
entrytool_router.register(
    PatientsWithErrors.base_name, PatientsWithErrors
)
