from entrytool import episode_categories
from entrytool.models import SCT
from plugins.data_load import base_loader


class LOTLoader(base_loader.Loader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patient_id_and_lot_number_to_episode = {}

    def check_lot_is_populated(self, column):
        try:
            result = self.row[column]
            if not result:
                raise ValueError("LOT number is not populated")
        except Exception as err:
            self.errors.append(
                dict(
                    file=self.file_name,
                    row=self.idx,
                    column=column,
                    value=result,
                    exception=err
                )
            )
        return result

    def load_row(self, row):
        if not (any(row.values())):
            return

        patient = self.check_and_get_patient_from_external_identifier(
            "Hospital_patient_ID"
        )
        if not patient:
            return
        lot_number = self.check_lot_is_populated("LOT")
        if not lot_number:
            return
        if (patient.id, lot_number) in self.patient_id_and_lot_number_to_episode:
            episode = self.patient_id_and_lot_number_to_episode[
                (
                    patient.id,
                    lot_number,
                )
            ]
        else:
            episode = patient.episode_set.create(
                category_name=episode_categories.LineOfTreatmentEpisode.display_name
            )
            self.patient_id_and_lot_number_to_episode[
                (
                    patient.id,
                    lot_number,
                )
            ] = episode

        if self.row["SCT_date"] or self.row["SCT_type"]:
            sct = SCT(episode=episode)
            sct.sct_date = self.check_and_get_date("SCT_date")
            sct.sct_type = self.check_and_get_string(SCT, "sct_type", "SCT_type")
            sct.set_consistency_token()
            sct.save()
