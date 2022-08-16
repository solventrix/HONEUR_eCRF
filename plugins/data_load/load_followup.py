from unicodedata import category
from plugins.conditions.cll.models import AdditionalCharacteristics
from plugins.conditions.cll import episode_categories
from plugins.data_load import base_loader


class FollowUpLoader(base_loader.Loader):
    def load_row(self, row):
        if not (any(row.values())):
            return

        patient = self.check_and_get_patient_from_external_identifier(
            "Hospital_patient_ID"
        )
        if not patient:
            return

        episode = patient.episode_set.get(
            category_name=episode_categories.CLLCondition.display_name
        )
        additional_characteristics = AdditionalCharacteristics(episode=episode)
        additional_characteristics.characteristic_date = self.check_and_get_date(
            "followup_date"
        )
        additional_characteristics.LDH = self.check_and_get_float("LDH")
        additional_characteristics.beta2m = self.check_and_get_float("beta2m")
        additional_characteristics.set_consistency_token()
        additional_characteristics.save()
