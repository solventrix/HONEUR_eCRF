"""
Unittests for entrytool
"""
from django.urls import reverse
from entrytool.episode_categories import (
    LineOfTreatmentEpisode, Default
)
from opal.core.test import OpalTestCase
from opal.models import Episode


class CreateNewLineOfTreatmentTestCase(OpalTestCase):
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

    def test_create_new_lot_read_only(self):
        url = reverse(
            "new_line_of_treatment_episode-detail",
            kwargs={"pk": self.patient.pk}
        )
        read_only = self.make_user("password", username="readonly")
        profile = read_only.profile
        profile.readonly = True
        profile.save()

        self.assertTrue(
            self.client.login(
                username="readonly", password="password"
            )
        )
        response = self.client.put(url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            self.patient.episode_set.all().count(), 1
        )


class DeleteLineOfTreatmentEpisodeTestCase(OpalTestCase):
    def setUp(self):
        super().setUp()
        _, self.episode = self.new_patient_and_episode_please()
        self.episode.category_name = LineOfTreatmentEpisode.display_name
        self.episode.save()
        self.url = reverse(
            "delete_line_of_treatment_episode-detail",
            kwargs={"pk": self.episode.pk}
        )
        self.assertTrue(
            self.client.login(
                username=self.user.username, password=self.PASSWORD
            )
        )

    def test_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Episode.objects.all().exists())

    def test_delete_read_only(self):
        read_only = self.make_user("password", username="readonly")
        profile = read_only.profile
        profile.readonly = True
        profile.save()
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            Episode.objects.all().count(), 1
        )

    def test_delete_different_episode_category(self):
        self.episode.category_name = Default.display_name
        self.episode.save()
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            Episode.objects.all().count(), 1
        )
