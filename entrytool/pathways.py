import datetime
from opal.core.pathway import PagePathway
from opal.core.pathway.steps import Step
from entrytool import models
from django.utils.translation import gettext_lazy as _


class AddPatient(PagePathway):
    display_name = _("Add Patient")
    slug = "add_patient"
    finish_button_text = _("Save")
#    icon = "fa-plus"

    @transaction.atomic
    def save(self, data, user, patient=None, episode=None):
        patient, episode = super.save(data, user, patient, episode)
        episode.start = datetime.date.today()
        episode.save()
        return patient, episode

    steps = [
        Step(model=models.Demographics, base_template='pathway/no_header_step.html')
    ]
