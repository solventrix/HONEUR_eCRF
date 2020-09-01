from opal.core.pathway import PagePathway
from entrytool import models

from opal import models as opal_models

from django.utils.translation import gettext_lazy as _

from django.db import transaction


class AddPatient(PagePathway):
    display_name = _("Add Patient")
    slug = "add_patient"
    icon = "fa-plus"

    steps = [
        models.Demographics,
        models.PatientDetails
        # models.TreatmentLine
    ]
