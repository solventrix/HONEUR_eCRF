from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.db import models as fields
from opal.core.fields import ForeignKeyOrFreeText
from opal.core import lookuplists
from opal import models
from entrytool.models import Hospital

HEAVY_CHAIN_OPTIONS = (
    ("IgG", _("IgG"),),
    ("IgD", _("IgD"),),
    ("IgA", _("IgA"),),
    ("IgM", _("IgM"),),
    ("IgE", _("IgE"),),
    ("No Heavy Chain", _("No Heavy Chain"),),
    ("Other", _("Other"),),
)

LIGHT_CHAIN_OPTIONS = (
    ('Kappa', _('Kappa')),
    ('Lambda', _('Lambda')),
    ('Non-Secretory', _('Non-Secretory')),
    ('No Light Chain', _('No Light Chain'))
)


class MMRegimenList(lookuplists.LookupList):
    class Meta:
        verbose_name = _("MM Regimen List")
        verbose_name_plural = _("MM Regimen List")


class MMStopReason(lookuplists.LookupList):
    class Meta:
        verbose_name = _("MM Stop Reason List")
        verbose_name_plural = _("MM Stop Reason List")


# Setup
class MMDiagnosisDetails(models.EpisodeSubrecord):
    _is_singleton = True  # One entry per patient that is updated

    class Meta:
        verbose_name = _("Diagnosis Details")
        verbose_name_plural = _("Diagnosis Details")

    CHOICES = (("Yes", _("Yes")), ("No", _("No")),)

    DIAGNOSIS_OPTIONS = (
        ("Solitary Bone Plasmacytoma", _("Solitary Bone Plasmacytoma")),
        ("Symptomatic Multiple Myeloma", _("Symptomatic Multiple Myeloma")),
        ("Plasmatic Celiac Leukemia", _("Plasmatic Celiac Leukemia")),
        ("Primary Amylodosis", _("Primary Amylodosis")),
        ("Asymptomatic MM", _("Asymptomatic MM")),
    )

    ECOG_CHOICES = (
        ("Asymptomatic", _("Asymptomatic"),),
        ("Symptomatic", _("Symptomatic"),),
        ("Very Symptomatic", _("Very Symptomatic"),),
    )

    diag_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of Diagnosis")
    )
    date_of_first_centre_visit = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of First Centre Visit")
    )

    referred = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Referred")
    )
    previous_hospital = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Previous Hospital")
    )

    diagnosis = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=DIAGNOSIS_OPTIONS,
        verbose_name=_("Diagnosis")
    )
    heavy_chain_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=HEAVY_CHAIN_OPTIONS,
        verbose_name=_("Heavy chain type")
    )
    light_chain_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=LIGHT_CHAIN_OPTIONS,
        verbose_name=_("Light chain type")
    )
    epidemiological_register = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Epidemiological Register")
    )

    # GAH Score 0 to 94
    gah_score = fields.IntegerField(
        blank=True, null=True, verbose_name=_("GAH Score")
    )
    # IMWG Scale 1 to 8
    imwg_scale = fields.IntegerField(
        blank=True, null=True, verbose_name=_("IMWG Scale")
    )
    # ICC scale 0 to 31
    icc_scale = fields.IntegerField(blank=True, null=True, verbose_name=_("ICC Scale"))

    # these fields are what the spread sheet call generics, putting them
    # here for want of a better place.
    height = fields.IntegerField(blank=True, null=True, verbose_name=_("Height"))

    # kg
    weight = fields.FloatField(blank=True, null=True, max_length=256, verbose_name=_("Weight"))

    ecog = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=ECOG_CHOICES,
        verbose_name=_("ECOG")
    )


class MMPatientStatus(models.PatientSubrecord):
    _is_singleton = True

    class Meta:
        verbose_name = _('Patient Status')
        verbose_name_plural = _('Patient Statuses')

    CAUSE_OF_DEATH = (
        ("Multiple Myeloma", _("Multiple Myeloma"),),
        ("Infection", _("Infection"),),
        ("Thrombosis", _("Thrombosis"),),
        ("Not Disease Related", _("Not Disease Related"),),
        ("Not Available", _("not available"),),
        ("Other", _("Other")),
    )
    STATUS_CHOICES = (
        ("Dead", _("Dead"),),
        ("Lost", _("Lost"),),
        ("Alive", _("Alive"),),
    )
    last_seen = fields.DateField(
        blank=True, null=True, verbose_name=_("Last Seen")
    )
    status = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=STATUS_CHOICES,
        verbose_name=_("Status")
    )
    date_of_death = fields.DateField(blank=True, null=True, verbose_name=_("Date Of Death"))
    comments = fields.TextField(
        blank=True,
        null=True,
        verbose_name=_("Comments")
    )
    cause_of_death = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CAUSE_OF_DEATH,
        verbose_name=_("Cause Of Death")
    )
    cause_of_death_other = fields.TextField(
        blank=True, default="", verbose_name=_("Death details")
    )


class MMPastMedicalHistory(models.PatientSubrecord):
    _is_singleton = True

    class Meta:
        verbose_name = _("Past Medical History")
        verbose_name_plural = _("Past Medical Histories")

    CHOICES = (("Yes", _("Yes")), ("No", _("No")),)

    previous_neoplasm = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Previous Neoplasm")
    )
    previous_neoplasm_date_of_diagnosis = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of Diagnosis")
    )
    previous_neoplasm_details = fields.TextField(
        blank=True, default="", verbose_name=_("Details")
    )

    chronic_renal_insufficiency = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Chronic Renal Insufficiency")
    )
    chronic_renal_insufficiency_diagnosis_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Insufficiency Date")
    )

    # TODO Can we check this should not be a select field
    monoclonal_pathology = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Monoclonal Pathology")
    )
    symtomatic_multiple_myeloma = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Symtomatic Multiple Myeloma")
    )

    asymtomatic_multiple_myeloma = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Asymtomatic Multiple Myeloma")
    )

    monoclonal_pathology_of_uncertain_meaning = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Monoclonal Pathology Of Uncertain Meaning")
    )
    # TODO I am not sure this is correct
    monoclonal_pathology_of_uncertain_meaning_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Diagnosis Date")
    )

    external_pasmocytoma = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("External Pasmocytoma")
    )
    gmp_comments = fields.TextField(blank=True, default="", verbose_name=_("GMP Comments"))


# LOT
class Comorbidity(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _('Comorbidities')
        verbose_name_plural = _('Comorbidities')

    INFECTION_TYPES = (
        ("Undocumented Preinfection", _("Undocumented Preinfection"),),
        ("Microbiologically Documented Without Bacteremia", _("Microbiologically Documented Without Bacteremia"),),
        ("Microbiologically Documented With Bacteremia", _("Microbiologically Documented With Bacteremia"),),
        ("Clinically Documented", _("Clinically Documented"),),
    )

    CONDITION_TYPES = (
        ("Renal Failure", _("Renal Failure"),),
        ("Neuropathy", _("Neuropathy"),),
        ("Hemorrhage", _("Hemorrhage"),),
        ("Fever", _("Fever"),),
        ("Infection", _("Infection"),),
        ("Other", _("Other"),),
    )
    condition = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CONDITION_TYPES,
        verbose_name=_("Condition")
    )

    # if condition == infection
    infection_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=INFECTION_TYPES,
        verbose_name=_("Infection Type")
    )
    type_of_microorganism_infection = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Type Of Microorganism Infection")
    )
    infection_source = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Infection Source")
    )

    # if condition == other
    other_condition_name = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Condition Name")
    )

    details = fields.TextField(
        blank=True, default="", verbose_name=_("Details")
    )


class MMRegimen(models.EpisodeSubrecord):
    _sort = "start_date"
    order_by = "-start_date"

    REGIMEN_TYPES = (
        ("Induction", _("Induction")),
        ("Maintenance", _("Maintenance")),
        ("Consolidation", _("Consolidation")),
        ("Relapse", _("Relapse")),
        ("Watch and wait", _("Watch and wait")),
        ("Other", _("Other")),
    )

    YES_NO = (
        ("Yes", _("Yes"),),
        ("No", _("No"),)
    )

    START_REASON = (
        ("Progression", _("Progression")),
        ("Clinical Relapse", _("Clinical Relapse")),
        ("Biological Relapse", _("Biological Relapse")),
        ("Other", _("Other")),
    )

    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    nbCycles = fields.IntegerField(
        verbose_name=_("Number of Cycles"),
        null=True,
        blank=True,
    )
    start_date = fields.DateField(
        verbose_name=_("Start Date"),
        blank=True,
        null=True
    )
    end_date = fields.DateField(
        verbose_name=_("End Date"), blank=True, null=True
    )
    regimen = ForeignKeyOrFreeText(MMRegimenList, verbose_name=_("Regimen"))
    regimen_details = fields.TextField(
        blank=True, default="", verbose_name=_("Regimen Details")
    )
    category = fields.CharField(
        max_length=40, choices=REGIMEN_TYPES, verbose_name=_("Regimen Type")
    )
    start_reason = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=START_REASON,
        verbose_name=_("Start Reason")
    )
    stop_reason = ForeignKeyOrFreeText(
        MMStopReason, verbose_name=_("Reason for Regimen Stop")
    )
    stop_reason_details = fields.TextField(
        blank=True, default="", verbose_name=_("Stop Reason Details")
    )
    comments = fields.TextField(blank=True, default="", verbose_name=_("Comments"))

    class Meta:
        verbose_name = _("Regimen")
        verbose_name_plural = _("Regimens")


class BoneDisease(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _("Bone Disease Treatment")
        verbose_name_plural = _("Bone Disease Treatments")

    TREATMENT_TYPES = (
        ("Denosumab", _("Denosumab"),),
        ("Bisphosphonates Induction", _("Bisphosphonates Induction"),),
        ("Vertebroplasty Induction", _("Vertebroplasty Induction"),),
        ("Other Induction", _("Other Induction"),),
        ("Not Available", _("Not Available"),),
    )
    treatment_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=TREATMENT_TYPES,
        verbose_name=_("Treatment Type")
    )
    treatment_details = fields.TextField(
        blank=True,
        null=True,
        default="",
        verbose_name=_("Treatment Details")
    )

    # only for treatment type Bisphosphonates
    bisphosphonate_treatment = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Bisphosphonate Treatment")
    )
    nb_cycles = fields.IntegerField(
        verbose_name=_("Number of Cycles"),
        null=True,
        blank=True,
    )
    start_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Start Date")
    )
    end_date = fields.DateField(
        blank=True, null=True, verbose_name=_("End Date")
    )
    vertebroplasty_kyphoplasty_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Vertebroplasty Kyphoplasty Date")
    )
    vertebroplasty_kyphoplasty_description = fields.TextField(
        blank=True, default="", verbose_name=_("Vertebroplasty Kyphoplasty Description")
    )


class MMResponse(models.EpisodeSubrecord):
    _sort = "response_date"
    order_by = "-response_date"

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")

    YES_NO = (
        ("Yes", _("Yes"),),
        ("No", _("No"),)
    )

    RESPONSES = (
        ("Minimal response", _("Minimal response")),
        ("Partial response", _("Partial response")),
        ("Very good partial response", _("Very good partial response")),
        ("Complete response", _("Complete response")),
        ("Stringent complete response", _("Stringent complete response")),
        ("Near complete response", _("Near complete response")),
        ("Immunophenotypic complete response", _("Immunophenotypic complete response")),
        ("Stable disease", _("Stable disease")),
        ("Progressive disease", _("Progressive disease")),
        ("Response unknown/NA", _("Response unknown/NA")),
    )

    MRD_TECHNIQUE_OPTIONS = (
        ("NGS", _("NGS"),),
        ("FC (Flow Cytometry)", _("FC (Flow Cytometry)")),
        ("Both", _("Both")),
    )
    # TODO This is only a thing for
    progression_date = fields.DateField(blank=True, null=True, verbose_name=_("Progression Date"))
    response_date = fields.DateField(blank=True, null=True, verbose_name=_("Response Date"))
    negative_mrd = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=YES_NO,
        verbose_name=_("Negative MRD")
    )
    negative_mrd_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Negative MRD Date")
    )

    mrd_technique = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=MRD_TECHNIQUE_OPTIONS,
        verbose_name=_("MRD Technique")
    )
    response = fields.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=RESPONSES,
        verbose_name=_("Response")
    )


class RadiotherapyInduction(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _("Radiotherapy Induction")
        verbose_name_plural = _("Radiotherapy Inductions")

    start_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Start Date")
    )
    end_date = fields.DateField(
        blank=True, null=True, verbose_name=_("End Date")
    )


class MMFollowUp(models.EpisodeSubrecord):
    _sort = "followup_date"
    _icon = "fa fa-stethoscope"
    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    follow_up_date = fields.DateField(
        verbose_name=_("Visit date"), blank=True, null=True
    )

    LDH = fields.FloatField(blank=True, null=True, verbose_name=_("LDH"))
    beta2m = fields.FloatField(blank=True, null=True, verbose_name=_("beta2m"))
    albumin = fields.FloatField(blank=True, null=True, verbose_name=_("Albumin"))
    mprotein_urine = fields.FloatField(
        blank=True, null=True, verbose_name=_("MProtein Urine")
    )
    mprotein_serum = fields.FloatField(
        blank=True, null=True, verbose_name=_("MProtein Serum")
    )
    mprotein_24h = fields.FloatField(
        blank=True, null=True, verbose_name=_("Mprotein In 24 Hour Urine")
    )

    class Meta:
        verbose_name = _("Follow-up")
        verbose_name_plural = _("Follow-ups")


class MMStemCellTransplantEligibility(models.EpisodeSubrecord):
    _is_singleton = True
    eligible_for_stem_cell_transplant = fields.BooleanField(
        default=False, verbose_name=_("Eligible For Stem Cell Transplant")
    )

    class Meta:
        verbose_name = _("Stem Cell Transplant Eligibility")
        verbose_name_plural = _("Stem Cell Transplant Eligibilities")


def delete_stem_cells(sender, instance, **kwargs):
    instance.episode.sct_set.all().delete()


post_save.connect(
    delete_stem_cells, sender=MMStemCellTransplantEligibility
)


# Follow ups
class LabTest(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _("Lab Tests")
        verbose_name_plural = _("Lab Tests")

    date = fields.DateField(blank=True, null=True, verbose_name=_("Date"))

    # BLOOD COUNT

    # g/dl
    hemoglobin = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Hemoglobin")
    )

    # 10^3 /mm^3 min 1 max 100
    leucocytes = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Leucocytes")
    )

    # 10^3 /mm^3
    neutrophils = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Neutrophils")
    )

    # 10^3 /mm^3
    lymphocytes = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Lymphocytes")
    )

    # 10^3 /mm^3
    platelets = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Platelets")
    )

    ### BIOCHEMISTRY

    # mg/dL, min 0.5, max 20
    creatinine = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Creatinine")
    )

    # g/dL
    total_proteins = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Total proteins")
    )

    # g/dL min 1 max 5.5
    albumin = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Albumin")
    )

    # U/L
    alkaline_phosphatase = fields.FloatField(
        blank=True,
        null=True,
        verbose_name=_("Alkaline Phosphatase")
    )

    # U/L
    ldh = fields.IntegerField(
        blank=True, null=True, verbose_name=_("LDH")
    )

    # mg/dL, min 6.5, max 25
    calcium = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Calcium")
    )

    # mg/L min 3 max 30
    pcr = fields.FloatField(blank=True, null=True, verbose_name=_("PCR"))

    # Troponine I, ng/L, min 0 max 350
    troponine = fields.FloatField(blank=True, null=True, verbose_name=_("Troponine"))

    # ng/L
    nt_pro_bnp = fields.IntegerField(
        blank=True, null=True, verbose_name=_("NT-proBNP")
    )

    # mL/min, min 5 max 102
    glomerular_filtration = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Glomerular Filtration")
    )

    ### Immunology

    # mg/L min 1.5 max 20
    beta_2_microglobulin = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Beta 2 Microglobulin")
    )

    ### Urine
    # mg/dl
    proteinuria = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Proteinuria")
    )
    # g/24h
    proteinuria_g24 = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Proteinuria gr/24")
    )


class Imaging(models.EpisodeSubrecord):

    class Meta:
        verbose_name = _('Imaging')
        verbose_name_plural = _('Imaging')

    BONE_SERIES_TEST_IMAGE_OPTIONS = (
        ("Zero", _("Zero")),
        ("One", _("One")),
        ("Two", _("Two")),
        ("Three", _("Three")),
    )

    YES_NO = (
        ("Yes", _("Yes"),),
        ("No", _("No"),)
    )

    SCAN_OPTIONS = (
        ("Negative", _("Negative")),
        ("Positive", _("Positive")),
        ("Not Done", _("Not Done")),
    )

    date = fields.DateField(blank=True, null=True, verbose_name=_("Date"))
    bone_series_test_image = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=BONE_SERIES_TEST_IMAGE_OPTIONS,
        verbose_name=_("Bone Series Test Image")
    )
    # this has never been used
    bone_series_description = fields.TextField(
        blank=True, default="", verbose_name=_("Bone Series Description")
    )
    ct_scan = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SCAN_OPTIONS,
        verbose_name=_("CT Scan")
    )
    ct_scan_description = fields.TextField(
        blank=True, default="", verbose_name=_("CT Scan Description")
    )

    resonance = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SCAN_OPTIONS,
        verbose_name=_("Resonance")
    )
    resonance_description = fields.TextField(
        blank=True, default="", verbose_name=_("Resonance description")
    )

    pet_scan = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SCAN_OPTIONS,
        verbose_name=_("PET scan")
    )
    pet_scan_description = fields.TextField(
        blank=True, default="", verbose_name=_("PET scan description")
    )

    other_imaging_test = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=YES_NO,
        verbose_name=_("Other Imaging Test")
    )
    other_imaging_test_description = fields.TextField(
        blank=True, default="", verbose_name=_("Other Imaging Test Description")
    )


class MProteinMesurements(models.EpisodeSubrecord):
    # g/dL
    serum_amount = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Monoclonal serum amount")
    )

    lambda_light_chain_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Lambda Light Chain Count")
    )
    kappa_light_chain_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Kappa Light Chain Count")
    )
    kappa_lambda_ratio = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Kappa Lambda Ratio")
    )

    # In urine
    urinary_monoclonal_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Urinary Monoclonal Count gr/24")
    )

    # In bone marrow
    plasma_cells_in_bone_marrow = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Plasma Cells In Bone Marrow")
    )


class Immunofixation(models.EpisodeSubrecord):
    date = fields.DateField(blank=True, null=True, verbose_name=_("Date"))
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    IMMUNOFIXATION_CHOICES = (
        (POSITIVE, _('Positive'),),
        (NEGATIVE, _('Negative'),),
        ("Unrealized", _('Unrealized'),),
    )
    monoclonal_ig_g_protein_serum = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=IMMUNOFIXATION_CHOICES,
        verbose_name="Monoclonal IgG Protein (Serum)"
    )
    monoclonal_ig_a_protein_serum = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=IMMUNOFIXATION_CHOICES,
        verbose_name="Monoclonal IgA Protein (Serum)"
    )
    monoclonal_ig_m_protein_serum = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=IMMUNOFIXATION_CHOICES,
        verbose_name="Monoclonal IgM Protein (Serum)"
    )
    monoclonal_kappa_chain_serum = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=IMMUNOFIXATION_CHOICES,
        verbose_name="Monoclonal Kappa chain (Serum)"
    )
    monoclonal_lambda_chain_serum = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=IMMUNOFIXATION_CHOICES,
        verbose_name="Monoclonal Lambda chain (Serum)"
    )
    immunifixaction_profile_serum = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Immunifixaction Profile (Serum)"
    )
    immunifixaction_profile_urine = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Immunifixaction Profile (Urine)"
    )


class ClinicalPresentation(models.EpisodeSubrecord):
    CHOICES = (("Yes", _("Yes")), ("No", _("No")),)

    INFECTION_TYPE_CHOICES = (
        ("Clinically Documented Infection", _("Clinically Documented Infection")),
        ("Undocumented Infection", _("Undocumented Infection")),
        (
            "Microbiologically Documented Without Bacteremia",
            _("Microbiologically Documented Without Bacteremia")
        ),
        (
            "Microbiologically Documented With Bacteremia",
            _("Microbiologically Documented With Bacteremia")
        ),
        (
            "Other Microbiologic Documented Infection",
            _("Other Microbiologic Documented Infection"),
        )
    )

    ISS_OPTIONS = (
        ("One", _("One")),
        ("Two", _("Two")),
        ("Three", _("Three")),
    )

    R_ISS_OPTIONS = (
        ("Stage I", _("Stage I")),
        ("Stage II", _("Stage II")),
        ("Stage III", _("Stage III")),
        ("Unknown", _("Unknown")),
    )

    date = fields.DateField(blank=True, null=True, verbose_name=_("Date"))
    infection_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=INFECTION_TYPE_CHOICES,
        verbose_name=_("Infection_Type")
    )

    # the name of the micro organism
    microorganism = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Microorganism")
    )

    microorganism_source = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name="Microorganism source"
    )

    renal_failure = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Renal Failure")
    )
    hypercalcemia = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Hypercalcemia")
    )
    fever = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Fever")
    )
    anemia = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Anemia")
    )
    dialysis = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Dialysis")
    )
    bone_pain = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Bone Pain")
    )

    extramedullary_plasmacytomas = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Extramedullary plasmacytomas")
    )

    # International Staging System
    iss = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=ISS_OPTIONS,
        verbose_name=_("ISS")
    )

    # Revised ISS
    riss = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=R_ISS_OPTIONS,
        verbose_name=_("R-ISS")
    )

    details = fields.TextField(
        blank=True, default="", verbose_name=_("Details")
    )


class Cytogenetics(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _("Cytogenetics")
        verbose_name_plural = _("Cytogenetics")

    CHOICES = CHOICES = (("Yes", _("Yes")), ("No", _("No")), ("Unknown", _("Unknown")),)

    date = fields.DateField(blank=True, null=True, verbose_name=_("Date"))
    t4_14_not_effected = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("t(4;14) Not Effected")
    )
    t4_14_haploid_karyotype = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("t(4;14) Haploid Karyotype")
    )
    t4_14 = fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=CHOICES,
        verbose_name=_("t(4;14)")
    )
    t4_14_16 = fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=CHOICES,
        verbose_name=_("t(14;16)")
    )
    t11_14 = fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=CHOICES,
        verbose_name=_("t(11;14)")
    )
    # TODO check thisis the same as del 14, as we require this for data to be a superser
    # of the default MM
    del1p = fields.CharField(
        max_length=10, choices=CHOICES, verbose_name=_("del 1p")
    )

    del_17p = fields.CharField(
        max_length=10, choices=CHOICES, verbose_name=_("del(17)p")
    )

    # TODO I can't find a reference to this so I'm not sure the display name
    # is correct
    gan1q = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("gan 1q")
    )

    chromosome_alterations = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Chromosome Alterations")
    )

    normal_study = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Normal Study")
    )
    details = fields.TextField(blank=True, default="", verbose_name=_("Details"))
    other_study = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Other study")
    )
