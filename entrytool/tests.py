"""
Unittests for entrytool
"""
from django.urls import reverse
from entrytool.episode_categories import LineOfTreatmentEpisode
from opal.core.test import OpalTestCase


class CreateNewTestCase(OpalTestCase):
    def setUp(self):
        super().setUp()
        self.patient, _ = self.new_patient_and_episode_please()

    def test_create_new_lot(self):
        url = reverse(
            "new_line_of_treatment_episode-detail",
            kwargs={"pk": self.patient.pk}
        )
        self.assertTrue(
            self.client.login(
                username=self.user.username, password=self.PASSWORD
            )
        )
        response = self.client.put(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.patient.episode_set.all().count(), 2
        )
        self.assertEqual(
            self.patient.episode_set.last().category_name,
            LineOfTreatmentEpisode.display_name
        )