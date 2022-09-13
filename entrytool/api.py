from rest_framework import status, pagination, generics
from rest_framework.parsers import FileUploadParser
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


class PatientsWithErrorsPaginator(pagination.PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        # This get's used by the opal js Paginator service
        # that expects total_count, total_pages and page_number
        return json_response({
            'total_count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'results': data
        })


class PatientsWithErrors(LoginRequiredViewset, generics.GenericAPIView):
    basename = "patients_with_errors"
    pagination_class = PatientsWithErrorsPaginator

    def get_queryset(self):
        return Patient.objects.filter(
            patientload__validated=True,
            patientload__has_errors=True,
            patientload__source=models.PatientLoad.LOADED_FROM_FILE
        )

    def list(self, request):
        qs = self.get_queryset()
        sorted_by_newest = models.sort_by_newest_to_oldest(qs)
        # Not actually a queryset but DRF also accepts a list
        page = self.paginate_queryset(sorted_by_newest)
        data = [i.id for i in page]
        return self.get_paginated_response(data)


class UploadFromZip(LoginRequiredViewset):
    parser_classes = [FileUploadParser]
    basename = "upload_from_zip"

    def create(self, request):
        zipfile = request.FILES.get('file')
        errors = load_data.load_data(zipfile)
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
    UploadFromZip.basename, UploadFromZip
)
