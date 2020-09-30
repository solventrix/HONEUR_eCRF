"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from entrytool import models
from entrytool import episode_categories


class AllPatientsList(core.patient_lists.PatientList):
    display_name = "All Patients"

    schema = [models.Demographics, models.PatientDetails]

    def get_queryset(self, **kwargs):
        return Episode.objects.filter(
            category_name=episode_categories.Default.display_name
        )


class RegimenList(core.patient_lists.PatientList):
    display_name = "All Regimens"

    schema = [models.Demographics, models.Regimen, models.AdverseEvent, models.Response]

    def get_queryset(self, **kwargs):
        patients = set(Episode.objects.filter(
            episode_categories.LineOfTreatmentEpisode.display_name
        ).values_list('patient_id', flat=True))

        return Episode.objects.filter(
            patient__in=patients,
            category_name=episode_categories.Default.display_name
        )


class FollowUpVisitList(core.patient_lists.PatientList):
    display_name = "Follow Up Visits"

    schema = [models.Demographics, models.FollowUp]

    def get_queryset(self, **kwargs):
        return Episode.objects.filter(
            category_name=episode_categories.Default.display_name
        )