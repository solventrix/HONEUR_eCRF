import datetime
from django.core.management.base import BaseCommand
from opal.models import Patient


def new_patient_and_episode_please():
    patient = Patient.objects.create()
    patient.patientload_set.update(
        source="Loaded From File",
    )
    episode = patient.episode_set.create(
        category_name="MM"
    )
    return patient, episode


def create_perfect_patient():
    patient, episode = new_patient_and_episode_please()
    today = datetime.date.today()
    demographics = patient.demographics_set.get()
    demographics.hospital_number = "1231231"
    demographics.date_of_birth = datetime.date(1993, 2, 4)
    demographics.consistency_token = "1231123"
    demographics.sex = "Male"
    demographics.save()

    diagnosis_details = episode.mmdiagnosisdetails_set.get()
    diagnosis_details.diag_date = today - datetime.timedelta(140)
    diagnosis_details.heavy_chain_type = "IgG"
    diagnosis_details.light_chain_type = 'Kappa'
    diagnosis_details.iss_stage = "Stage II"
    diagnosis_details.consistency_token = "1231123"
    diagnosis_details.save()


def create_no_gender():
    patient, episode = new_patient_and_episode_please()
    today = datetime.date.today()
    demographics = patient.demographics_set.get()
    demographics.hospital_number = "234059098"
    demographics.date_of_birth = datetime.date(1993, 2, 4)
    demographics.consistency_token = "1231123"
    demographics.save()

    diagnosis_details = episode.mmdiagnosisdetails_set.get()
    diagnosis_details.diag_date = today - datetime.timedelta(140)
    diagnosis_details.heavy_chain_type = "IgG"
    diagnosis_details.light_chain_type = 'Kappa'
    diagnosis_details.iss_stage = "Stage II"
    diagnosis_details.consistency_token = "1231123"
    diagnosis_details.save()

    patient_status = patient.patientstatus_set.get()
    patient_status.deceased = True
    patient_status.death_date = today - datetime.timedelta(5)
    patient_status.death_cause = "Disease"
    patient_status.consistency_token = "1231123"
    patient_status.save()

    lot_episode = patient.create_episode(category_name="Treatment Line")

    mm_regimen = lot_episode.mmregimen_set.create()
    mm_regimen.hospital = "MVZ Koln"
    mm_regimen.start_date = today - datetime.timedelta(100)
    mm_regimen.regimen_type = "Induction"
    mm_regimen.regimen = "Vincristine"
    mm_regimen.nbCycles = 4
    mm_regimen.consistency_token = "1231123"
    mm_regimen.save()

    response = lot_episode.mmresponse_set.create()
    response.response_date = today - datetime.timedelta(40)
    response.response = "Partial response"
    response.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(100)
    lab_test.kappa_light_chain_count = 19.8
    lab_test.lambda_light_chain_count = 10.2
    lab_test.kappa_lambda_ratio = 1.94
    lab_test.iga_count = 228
    lab_test.igg_count = 1124
    lab_test.igm_count = 132
    lab_test.igd_count = 70
    lab_test.ige_count = 193
    lab_test.creatinine = 1.9
    lab_test.mprotein_24h = 133
    lab_test.calcium = 14.3
    lab_test.beta2m = 1.77
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(86)
    lab_test.kappa_light_chain_count = 20.1
    lab_test.lambda_light_chain_count = 13.2
    lab_test.kappa_lambda_ratio = 2.04
    lab_test.iga_count = 212
    lab_test.igg_count = 987
    lab_test.igm_count = 121
    lab_test.igd_count = 65
    lab_test.ige_count = 187
    lab_test.creatinine = 1.2
    lab_test.mprotein_24h = 124
    lab_test.calcium = 12.3
    lab_test.beta2m = 1.75
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(72)
    lab_test.kappa_light_chain_count = 17
    lab_test.lambda_light_chain_count = 11.2
    lab_test.kappa_lambda_ratio = 1.92
    lab_test.iga_count = 218
    lab_test.igg_count = 1324
    lab_test.igm_count = 112
    lab_test.igd_count = 50
    lab_test.ige_count = 143
    lab_test.creatinine = 1.2
    lab_test.mprotein_24h = 153
    lab_test.calcium = 9.3
    lab_test.beta2m = 1.37
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(58)
    lab_test.kappa_light_chain_count = 21
    lab_test.lambda_light_chain_count = 9
    lab_test.kappa_lambda_ratio = 2.3
    lab_test.iga_count = 218
    lab_test.igg_count = 1174
    lab_test.igm_count = 112
    lab_test.igd_count = 74
    lab_test.ige_count = 199
    lab_test.creatinine = 2
    lab_test.mprotein_24h = 133
    lab_test.calcium = 40
    lab_test.beta2m = 1.77
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(44)
    lab_test.kappa_light_chain_count = 22.1
    lab_test.lambda_light_chain_count = 13.2
    lab_test.kappa_lambda_ratio = 2.14
    lab_test.iga_count = 213
    lab_test.igg_count = 997
    lab_test.igm_count = 125
    lab_test.igd_count = 69
    lab_test.ige_count = 197
    lab_test.creatinine = 1.7
    lab_test.mprotein_24h = 134
    lab_test.calcium = 9
    lab_test.beta2m = 1.25
    lab_test.consistency_token = "1231123"
    lab_test.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(100)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Negative"
    cytogenetics.del11q = "Negative"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(100)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Negative"
    cytogenetics.del11q = "Negative"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(100)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Negative"
    cytogenetics.del11q = "Negative"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()


def create_open_regimen():
    patient, episode = new_patient_and_episode_please()
    today = datetime.date.today()
    demographics = patient.demographics_set.get()
    demographics.hospital_number = "234059098"
    demographics.date_of_birth = datetime.date(1993, 2, 4)
    demographics.consistency_token = "1231123"
    demographics.sex = "Male"
    demographics.save()

    diagnosis_details = episode.mmdiagnosisdetails_set.get()
    diagnosis_details.diag_date = today - datetime.timedelta(140)
    diagnosis_details.heavy_chain_type = "IgG"
    diagnosis_details.light_chain_type = 'Kappa'
    diagnosis_details.iss_stage = "Stage II"
    diagnosis_details.consistency_token = "1231123"
    diagnosis_details.save()

    patient_status = patient.patientstatus_set.get()
    patient_status.deceased = True
    patient_status.death_date = today - datetime.timedelta(5)
    patient_status.death_cause = "Disease"
    patient_status.consistency_token = "1231123"
    patient_status.save()

    lot_episode = patient.create_episode(category_name="Treatment Line")

    mm_regimen = lot_episode.mmregimen_set.create()
    mm_regimen.hospital = "MVZ Koln"
    mm_regimen.start_date = today - datetime.timedelta(40)
    mm_regimen.regimen_type = "Induction"
    mm_regimen.regimen = "Vincristine"
    mm_regimen.nbCycles = 4
    mm_regimen.consistency_token = "1231123"
    mm_regimen.save()

    mm_regimen = lot_episode.mmregimen_set.create()
    mm_regimen.hospital = "MVZ Koln"
    mm_regimen.start_date = today - datetime.timedelta(60)
    mm_regimen.regimen_type = "Maintenance"
    mm_regimen.regimen = "Bendamustine.Dexamethason"
    mm_regimen.nbCycles = 4
    mm_regimen.consistency_token = "1231123"
    mm_regimen.save()

    response = lot_episode.mmresponse_set.create()
    response.response_date = today - datetime.timedelta(60)
    response.response = "Complete response"
    response.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(100)
    lab_test.kappa_light_chain_count = 19.8
    lab_test.lambda_light_chain_count = 10.2
    lab_test.kappa_lambda_ratio = 1.94
    lab_test.iga_count = 228
    lab_test.igg_count = 1124
    lab_test.igm_count = 132
    lab_test.igd_count = 70
    lab_test.ige_count = 193
    lab_test.creatinine = 1.9
    lab_test.mprotein_24h = 133
    lab_test.calcium = 14.3
    lab_test.beta2m = 1.77
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(86)
    lab_test.kappa_light_chain_count = 20.1
    lab_test.lambda_light_chain_count = 13.2
    lab_test.kappa_lambda_ratio = 2.04
    lab_test.iga_count = 212
    lab_test.igg_count = 987
    lab_test.igm_count = 121
    lab_test.igd_count = 65
    lab_test.ige_count = 187
    lab_test.creatinine = 1.2
    lab_test.mprotein_24h = 124
    lab_test.calcium = 12.3
    lab_test.beta2m = 1.75
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(76)
    lab_test.kappa_light_chain_count = 17
    lab_test.lambda_light_chain_count = 11.2
    lab_test.kappa_lambda_ratio = 1.92
    lab_test.iga_count = 218
    lab_test.igg_count = 1324
    lab_test.igm_count = 112
    lab_test.igd_count = 50
    lab_test.ige_count = 143
    lab_test.creatinine = 1.2
    lab_test.mprotein_24h = 153
    lab_test.calcium = 9.3
    lab_test.beta2m = 1.37
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(34)
    lab_test.kappa_light_chain_count = 22.1
    lab_test.lambda_light_chain_count = 13.2
    lab_test.kappa_lambda_ratio = 2.14
    lab_test.iga_count = 213
    lab_test.igg_count = 997
    lab_test.igm_count = 125
    lab_test.igd_count = 69
    lab_test.ige_count = 197
    lab_test.creatinine = 1.7
    lab_test.mprotein_24h = 134
    lab_test.calcium = 9
    lab_test.beta2m = 1.25
    lab_test.consistency_token = "1231123"
    lab_test.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(90)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Negative"
    cytogenetics.del11q = "Negative"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(95)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Negative"
    cytogenetics.del11q = "Negative"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(10)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Negative"
    cytogenetics.del11q = "Negative"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()



class Command(BaseCommand):
    def handle(self, *args, **options):
        Patient.objects.all().delete()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_no_gender()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_perfect_patient()
        create_open_regimen()
