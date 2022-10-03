import datetime
from opal.core.test import OpalTestCase
from entrytool import models
from opal.models import Episode
from django.urls import reverse


class ApiTestCase(OpalTestCase):
    def setUp(self):
        self.url = reverse('patients_with_errors-list')

    def test_get(self):
        for i in range(30):
            patient, episode = self.new_patient_and_episode_please()
            episode.sct_set.create(
                sct_date=datetime.date.today() - datetime.timedelta(i)
            )
            patient.patientload_set.update(
                validated=True,
                has_errors=True,
                source=models.PatientLoad.LOADED_FROM_FILE
            )
        self.client.login(
            username=self.user.username, password=self.PASSWORD
        )
        response = self.client.get(self.url)

        most_recent = Episode.objects.order_by('-sct__sct_date')[0]
        self.assertEqual(len(response.json()['results']), 20)
        self.assertEqual(response.json()['results'][0], most_recent.id)
        self.assertEqual(response.json()['page_count'], 2)
