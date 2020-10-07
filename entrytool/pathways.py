from opal.core.pathway import PagePathway
from opal.core.pathway.steps import Step
from entrytool import models
from django.utils.translation import gettext_lazy as _


class AddPatient(PagePathway):
    display_name = _("Add Patient")
    slug = "add_patient"
    finish_button_text = _("Save")
    icon = "fa "

    steps = [
        Step(model=models.Demographics, base_template='pathway/no_header_step.html')
    ]
