from entrytool.models import FollowUp
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

        follow_up = FollowUp(patient=patient)
        follow_up.follow_up_date = self.check_and_get_date("followup_date")
        follow_up.LDH = self.check_and_get_float("LDH")
        follow_up.beta2m = self.check_and_get_float("beta2m")
        follow_up.albumin = self.check_and_get_float("albumin")
        follow_up.set_consistency_token()
        follow_up.save()
