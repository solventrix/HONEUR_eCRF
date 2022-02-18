from django.db import transaction
from opal.core.pathway import PagePathway
from opal.core.pathway.steps import Step
from entrytool import models
from django.utils.translation import gettext_lazy as _


class AddPatient(PagePathway):
    display_name = _("Add Patient")
    slug = "add_patient"
    finish_button_text = _("Save")
#    icon = "fa-plus"

    steps = [
        Step(model=models.Demographics, base_template='pathway/no_header_step.html'),
        Step(
            display_name='Category select',
            template='pathway/category_select.html',
            base_template='pathway/no_header_step.html'
        ),
    ]

    @transaction.atomic
    def save(self, data, user, patient=None, episode=None):
        """
            If the patient already exists and has an infectious service
            episode. Update that episode.

            Else if the patient already exists, create a new episode.

            Else if the patient doesn't exist load in the patient.
        """
        episode_category = data.pop('episode_category')
        saved_patient, saved_episode = super().save(
            data, user=user, patient=patient, episode=episode
        )
        saved_episode.category_name = episode_category[0]
        saved_episode.save()
        return saved_patient, saved_episode
