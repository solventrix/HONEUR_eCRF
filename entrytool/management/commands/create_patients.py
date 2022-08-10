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
    diagnosis_details.heavy_chain_type = "IgD"
    diagnosis_details.light_chain_type = 'Non-Secretory'
    diagnosis_details.iss_stage = "Stage I"
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
    diagnosis_details.heavy_chain_type = "No Heavy Chain"
    diagnosis_details.light_chain_type = 'Kappa'
    diagnosis_details.iss_stage = "Unknown"
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
    mm_regimen.regimen = "Chlorambucil.Obinotuzumab"
    mm_regimen.nbCycles = 4
    mm_regimen.consistency_token = "1231123"
    mm_regimen.save()

    response = lot_episode.mmresponse_set.create()
    response.response_date = today - datetime.timedelta(40)
    response.response = "Partial response"
    response.consistency_token = "1231123"
    response.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(100)
    # normal range 3.3 to 19.4
    lab_test.kappa_light_chain_count = 19.8
    # 5.71 to 26.3
    lab_test.lambda_light_chain_count = 10.2
    # 0.26 to 1.65
    lab_test.kappa_lambda_ratio = 1.94
    # 80 – 350
    lab_test.iga_count = 228
    # 6.0 - 16.0
    lab_test.igg_count = 1124
    # 40 – 250
    lab_test.igm_count = 132
    # 14 to 85
    lab_test.igd_count = 70

    # 1.5-144
    lab_test.ige_count = 193
    # 1.65 to 2.33
    lab_test.creatinine = 1.9

    # 0.7 to 1.3
    lab_test.mprotein_24h = 133

    # 8.5 to 10.5
    lab_test.calcium = 14.3

    #  0.8-2.5
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
    cytogenetics.date = today - datetime.timedelta(80)
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
    diagnosis_details.heavy_chain_type = "IgA"
    diagnosis_details.light_chain_type = 'Lambda'
    diagnosis_details.iss_stage = "Stage I"
    diagnosis_details.consistency_token = "1231123"
    diagnosis_details.save()

    lot_episode = patient.create_episode(category_name="Treatment Line")

    mm_regimen = lot_episode.mmregimen_set.create()
    mm_regimen.hospital = "MVZ Koln"
    mm_regimen.start_date = today - datetime.timedelta(40)
    mm_regimen.end_date = today - datetime.timedelta(45)
    mm_regimen.regimen_type = "Conditioning"
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
    response.consistency_token = "1231123"
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
    lab_test.kappa_light_chain_count = 21.1
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


def future_cytogenetics():
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

    lot_episode = patient.create_episode(category_name="Treatment Line")

    mm_regimen = lot_episode.mmregimen_set.create()
    mm_regimen.hospital = "MVZ Koln"
    mm_regimen.start_date = today - datetime.timedelta(100)
    mm_regimen.regimen_type = "Induction"
    mm_regimen.regimen = "Rituximab Erhaltung"
    mm_regimen.nbCycles = 4
    mm_regimen.consistency_token = "1231123"
    mm_regimen.save()

    response = lot_episode.mmresponse_set.create()
    response.response_date = today - datetime.timedelta(40)
    response.response = "Complete respons"
    response.consistency_token = "1231123"
    response.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(60)
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

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(50)
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
    cytogenetics.date = today + datetime.timedelta(43)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Negative"
    cytogenetics.del11q = "Negative"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()


def response_before_diagnosis_date():
    patient, episode = new_patient_and_episode_please()
    today = datetime.date.today()
    demographics = patient.demographics_set.get()
    demographics.hospital_number = "234059098"
    demographics.date_of_birth = datetime.date(1993, 2, 4)
    demographics.consistency_token = "1231123"
    demographics.sex = "Female"
    demographics.save()

    diagnosis_details = episode.mmdiagnosisdetails_set.get()
    diagnosis_details.diag_date = today - datetime.timedelta(140)
    diagnosis_details.heavy_chain_type = "IgE"
    diagnosis_details.light_chain_type = 'Kappa'
    diagnosis_details.iss_stage = "Stage I"
    diagnosis_details.consistency_token = "1231123"
    diagnosis_details.save()

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
    response.response_date = today - datetime.timedelta(145)
    response.response = "Near complete response"
    response.consistency_token = "1231123"
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
    lab_test.calcium = 10.2
    lab_test.beta2m = 1.77
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(44)
    lab_test.kappa_light_chain_count = 22.4
    lab_test.lambda_light_chain_count = 13.5
    lab_test.kappa_lambda_ratio = 2.15
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
    cytogenetics.date = today - datetime.timedelta(60)
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
    cytogenetics.date = today - datetime.timedelta(80)
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


def future_death():
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
    patient_status.death_date = today + datetime.timedelta(5)
    patient_status.death_cause = "Disease"
    patient_status.consistency_token = "1231123"
    patient_status.save()

    lot_episode = patient.create_episode(category_name="Treatment Line")

    mm_regimen = lot_episode.mmregimen_set.create()
    mm_regimen.hospital = "MVZ Koln"
    mm_regimen.start_date = today - datetime.timedelta(100)
    mm_regimen.regimen_type = "Induction"
    mm_regimen.regimen = "Bendamustine.Vincristine.Prednison"
    mm_regimen.nbCycles = 4
    mm_regimen.consistency_token = "1231123"
    mm_regimen.save()

    response = lot_episode.mmresponse_set.create()
    response.response_date = today - datetime.timedelta(40)
    response.response = "Stable disease"
    response.consistency_token = "1231123"
    response.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(100)
    lab_test.kappa_light_chain_count = 17.8
    lab_test.lambda_light_chain_count = 12.2
    lab_test.kappa_lambda_ratio = 1.03
    lab_test.iga_count = 148
    lab_test.igg_count = 1024
    lab_test.igm_count = 102
    lab_test.igd_count = 90
    lab_test.ige_count = 133
    lab_test.creatinine = 3.1
    lab_test.mprotein_24h = 103
    lab_test.calcium = 16.2
    lab_test.beta2m = 1.86
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(100)
    lab_test.kappa_light_chain_count = 16.8
    lab_test.lambda_light_chain_count = 11.6
    lab_test.kappa_lambda_ratio = 1.12
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
    lab_test.date = today - datetime.timedelta(100)
    lab_test.kappa_light_chain_count = 17.2
    lab_test.lambda_light_chain_count = 14.1
    lab_test.kappa_lambda_ratio = 1.53
    lab_test.iga_count = 198
    lab_test.igg_count = 1234
    lab_test.igm_count = 114
    lab_test.igd_count = 53
    lab_test.ige_count = 163
    lab_test.creatinine = 2.4
    lab_test.mprotein_24h = 132
    lab_test.calcium = 15.4
    lab_test.beta2m = 1.89
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(100)
    lab_test.kappa_light_chain_count = 21.8
    lab_test.lambda_light_chain_count = 15.5
    lab_test.kappa_lambda_ratio = 2.12
    lab_test.iga_count = 216
    lab_test.igg_count = 1054
    lab_test.igm_count = 112
    lab_test.igd_count = 69
    lab_test.ige_count = 187
    lab_test.creatinine = 1.3
    lab_test.mprotein_24h = 126
    lab_test.calcium = 15.2
    lab_test.beta2m = 1.78
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(100)
    lab_test.kappa_light_chain_count = 17
    lab_test.lambda_light_chain_count = 11.3
    lab_test.kappa_lambda_ratio = 2.34
    lab_test.iga_count = 212
    lab_test.igg_count = 956
    lab_test.igm_count = 121
    lab_test.igd_count = 67
    lab_test.ige_count = 201
    lab_test.creatinine = 1.6
    lab_test.mprotein_24h = 145
    lab_test.calcium = 16.2
    lab_test.beta2m = 1.82
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(86)
    lab_test.kappa_light_chain_count = 18.4
    lab_test.lambda_light_chain_count = 12.2
    lab_test.kappa_lambda_ratio = 2.34
    lab_test.iga_count = 192
    lab_test.igg_count = 897
    lab_test.igm_count = 145
    lab_test.igd_count = 67
    lab_test.ige_count = 179
    lab_test.creatinine = 1.1
    lab_test.mprotein_24h = 123
    lab_test.calcium = 11.6
    lab_test.beta2m = 1.85
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(72)
    lab_test.kappa_light_chain_count = 16
    lab_test.lambda_light_chain_count = 13.2
    lab_test.kappa_lambda_ratio = 1.99
    lab_test.iga_count = 204
    lab_test.igg_count = 1124
    lab_test.igm_count = 142
    lab_test.igd_count = 49
    lab_test.ige_count = 145
    lab_test.creatinine = 1.6
    lab_test.mprotein_24h = 162
    lab_test.calcium = 8.7
    lab_test.beta2m = 1.23
    lab_test.consistency_token = "1231123"
    lab_test.save()

    lab_test = episode.labtest_set.create()
    lab_test.hospital = "MVZ Koln"
    lab_test.date = today - datetime.timedelta(44)
    lab_test.kappa_light_chain_count = 21.1
    lab_test.lambda_light_chain_count = 16.2
    lab_test.kappa_lambda_ratio = 2.44
    lab_test.iga_count = 234
    lab_test.igg_count = 1100
    lab_test.igm_count = 135
    lab_test.igd_count = 79
    lab_test.ige_count = 178
    lab_test.creatinine = 1.5
    lab_test.mprotein_24h = 124
    lab_test.calcium = 8
    lab_test.beta2m = 1.15
    lab_test.consistency_token = "1231123"
    lab_test.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(80)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Positive"
    cytogenetics.del11q = "Positive"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(90)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Positive"
    cytogenetics.del11q = "Positive"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()

    cytogenetics = episode.mmcytogenetics_set.create()
    cytogenetics.date = today - datetime.timedelta(100)
    cytogenetics.hospital = "MVZ Koln"
    cytogenetics.tp_53 = "Negative"
    cytogenetics.del_17p = "Positive"
    cytogenetics.del11q = "Positive"
    cytogenetics.t4_14 = "Negative"
    cytogenetics.t4_14_16 = "Negative"
    cytogenetics.ighv = "Negative"
    cytogenetics.consistency_token = "1231123"
    cytogenetics.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        Patient.objects.all().delete()
        for i in range(10):
            create_perfect_patient()
        create_no_gender()
        for i in range(10):
            create_perfect_patient()
        create_open_regimen()
        for i in range(10):
            create_perfect_patient()
        future_cytogenetics()
        for i in range(10):
            create_perfect_patient()
        response_before_diagnosis_date()
        for i in range(20):
            create_perfect_patient
        future_death()
