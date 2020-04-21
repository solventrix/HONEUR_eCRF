"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from entrytool import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.PatientDetails
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()

class RegimenList(core.patient_lists.PatientList):
    display_name = "All Regimens"

    schema = [
        models.Demographics,
        models.Regimen,
        models.AdverseEvent,
        models.Response
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()

class FollowUpVisitList(core.patient_lists.PatientList):
    display_name = "Follow Up Visits"

    schema = [
        models.Demographics,
        models.FollowUp
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()