import datetime
from django.core.management.base import BaseCommand
from opal.models import Patient
from entrytool.models import PatientLoad


class Command(BaseCommand):
    def handle(self, *args, **options):
        Patient.objects.all().delete()
        count = 400
        modulo = 5
        dob_start = datetime.date(1956, 1, 2)
        yesterday = datetime.date.today() - datetime.timedelta(1)
        two_days_ago = yesterday - datetime.timedelta(1)
        for i in range(count):
            patient = Patient.objects.create()
            patient.patientload_set.update(
                source=PatientLoad.LOADED_FROM_FILE,
            )
            patient.demographics_set.update(
                hospital_number=i*1563,
                date_of_birth=dob_start + datetime.timedelta(200*i)
            )

            patient.episode_set.create(
                category_name="MM"
            )

            if not i % modulo:
                episode = patient.episode_set.get()
                episode.mmdiagnosisdetails_set.update(
                    diag_date=yesterday,
                    heavy_chain_type='IgG',
                    light_chain_type='Lambda',
                    iss_stage='Stage II',
                    consistency_token='111'
                )
                lot_episode = patient.episode_set.create(
                    category_name="Treatment Line"
                )
                regimen = lot_episode.mmregimen_set.create(
                    start_date=two_days_ago,
                    consistency_token='111',
                    nbCycles=2
                )
                regimen.regimen = 'Induction'
                regimen.hospital = 'MVZ Koln'
                regimen.save()
                print(f'error patient {patient.id}')
