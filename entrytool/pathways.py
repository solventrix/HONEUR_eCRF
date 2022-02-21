from django.db import transaction
from opal.core.pathway import PagePathway
from opal.core.pathway.steps import Step
from opal.core.episodes import (
    EpisodeCategory, InpatientEpisode
)
from entrytool import models
from entrytool.episode_categories import LineOfTreatmentEpisode
from django.utils.translation import gettext_lazy as _

category_select_step = Step(
    display_name='Category select',
    template='pathway/category_select.html',
    base_template='pathway/no_header_step.html'
)


class AddPatient(PagePathway):
    display_name = _("Add Patient")
    slug = "add_patient"
    finish_button_text = _("Save")
#    icon = "fa-plus"

    steps = [
        Step(model=models.Demographics, base_template='pathway/no_header_step.html'),
    ]

    def get_steps(self, *args, **kwargs):
        """
        If the deployment supports multiple conditions, add the step
        that allows the users to select what episode category to use.
        """
        steps = super().get_steps(*args, **kwargs)
        if self.multiple_conditions:
            steps.append(category_select_step)
        return steps

    @property
    def condition_categories(self):
        """
        This returns all 'condition' categories, e.g. MM or CLL.

        The app assumes that all episode categories appart from LineOfTreatmentEpisode
        are addable and can be added from the category select step.
        """
        non_conditions = (
            LineOfTreatmentEpisode.display_name, InpatientEpisode.display_name,
        )
        return [
            i.display_name for i in EpisodeCategory.list() if i.display_name not in non_conditions
        ]

    @property
    def multiple_conditions(self):
        """
        Returns whether this deployment is configured to allow multiple conditions
        """
        return len(self.condition_categories) > 1

    @transaction.atomic
    def save(self, data, *args, **kwargs):
        """
        If the deployment allows for multiple conditions then the user should
        have selected which condition to use. Otherwise skip this logic and
        let use the defautl episode category as defined by the application
        """
        if not self.multiple_conditions:
            return super().save(data, *args, **kwargs)

        episode_category = data.pop('episode_category')
        saved_patient, saved_episode = super().save(data, *args, **kwargs)
        saved_episode.category_name = episode_category[0]
        saved_episode.save()
        return saved_patient, saved_episode
