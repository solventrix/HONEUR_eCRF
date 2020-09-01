from opal.core.pathway import PagePathway
from entrytool import models

from django.utils.translation import gettext_lazy as _


class AddPatient(PagePathway):
    display_name = _("Add Patient")
    slug = "add_patient"
    icon = "fa-plus"

    steps = [
        models.Demographics,
        models.PatientDetails
        # models.TreatmentLine
    ]
