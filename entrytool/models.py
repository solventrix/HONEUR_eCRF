"""
entrytool models.
"""
from django.db.models import fields

from opal import models
from opal.core import lookuplists
from opal.core.fields import ForeignKeyOrFreeText
from django.utils.translation import gettext_lazy as _


class Demographics(models.Demographics):
    _icon = ''
    external_identifier = fields.CharField(
        blank=True, null=True, max_length=256, unique=True,
        verbose_name=_("External Identifier")
    )


class Hospital(lookuplists.LookupList):
    class Meta:
        verbose_name = _("Hospital")
        verbose_name_plural = _("Hospitals")


class SCT(models.EpisodeSubrecord):
    SCT_TYPES = (
        ("Allogenic", _("Allogenic")),
        ("Autologous", _("Autologous")),
        ("Unknown", _("Unknown")),
    )
    order_by = "-sct_date"

    sct_date = fields.DateField(verbose_name=_("Date of SCT"))
    hospital = models.ForeignKeyOrFreeText(
        Hospital, verbose_name=_("Hospital")
    )
    sct_type = fields.CharField(
        max_length=12,
        verbose_name=_("Type of SCT"),
        choices=SCT_TYPES,
        null=True
    )

    class Meta:
        verbose_name = _("Stem Cell Transplant")
        verbose_name_plural = _("Stem Cell Transplants")


# Disease specific details
class PatientDetails(models.PatientSubrecord):
    _is_singleton = True  # One entry per patient that is updated

    STATUSES = (
         ("Under Treatment", _("Under Treatment")),
         ("Dead", _("Dead",)),
         ("Lost to Follow-up", _("Lost to Follow-up")),
    )
    hospital = models.ForeignKeyOrFreeText(
        Hospital, verbose_name=_("Hospital")
    )

    CHOICES = (
        ("Yes", _("Yes")),
        ("No", _("No")),
        ("Unknown", _("Unknown"))
    )
    DEATH_CAUSES = (
        ("Disease", _("Disease")),
        ("Complications of Disease", _("Complications of Disease")),
        ("Other", _("Other"))
    )
    R_ISS_STAGES = (
        ("Stage I", _("Stage I")),
        ("Stage II", _("Stage II")),
        ("Stage III", _("Stage III")),
        ("Unknown", _("Unknown"))
    )
    PP_TYPE_CHOICES = (
        ("IgG", _("IgG")),
        ("IgA", _("IgA")),
        ("IgE", _("IgE")),
        ("Light Chain Myeloma", _("Light Chain Myeloma")),
    )
    LIGHT_CHAIN_CHOICES = (
        ("Kappa", _("Kappa")),
        ("Lambda", _("Lambda"))
    )
    RISK_STRATIFICATIONS = (
        ("Standard risk", _("Standard risk")),
        ("Intermediate risk", _("Intermediate risk")),
        ("High risk", _("High risk"))
    )
    status = fields.CharField(
        max_length=100, choices=STATUSES, verbose_name=_("Patient Status")
    )
    diag_date = fields.DateField(
        blank=False, null=True, verbose_name=_("Date of Diagnosis")
    )
    date_of_last_visit = fields.DateField(
        blank = False, null=True, verbose_name=_("Date of last visit")
    )
    iss_stage = fields.CharField(
        max_length=10, choices=R_ISS_STAGES, verbose_name=_("ISS Stage")
    )
    r_iss_stage = fields.CharField(
        max_length=10, choices=R_ISS_STAGES, verbose_name=_("R-ISS Stage")
    )
    ds_stage = fields.CharField(
        max_length=10, choices=R_ISS_STAGES, verbose_name=_("DS Stage")
    )
    pp_type = fields.CharField(
        max_length=50, choices=PP_TYPE_CHOICES, verbose_name=_("PP Type")
    )
    light_chain_type = fields.CharField(
        max_length=25, choices = LIGHT_CHAIN_CHOICES, verbose_name=_("Light Chain Type")
    )
    del_17p = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("del(17)p"))
    del_13 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("del13"))
    t4_14 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("t(4;14)"))
    t4_16 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("t(4;16)"))
    death_date = fields.DateField(
        null=True, verbose_name=_("Date of Death"), blank=True
    )
    death_cause = fields.CharField(
        max_length=100,
        choices=DEATH_CAUSES,
        verbose_name=_("Cause of Death"),
        blank=True,
        null=True,
    )
    lost_to_follow_up_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Lost to Follow-up")
    )
    risk_stratification = fields.CharField(max_length=25, choices = RISK_STRATIFICATIONS, verbose_name = _("Risk stratification"))

    class Meta:
        verbose_name = _("Patient Details")
        verbose_name_plural = _("Patient Details")


class RegimenList(lookuplists.LookupList):
    class Meta:
        verbose_name = _("Regimen List")
        verbose_name_plural = _("Regimen List")


class StopReason(lookuplists.LookupList):
    class Meta:
        verbose_name = _("Stop Reason")
        verbose_name_plural = _("Stop Reason")


# TODO does this need to be kept? Can the line number be an attribute of the episode?
class TreatmentLine(models.EpisodeSubrecord):
    nb = fields.IntegerField(verbose_name=_("Treatment Line"))

    class Meta:
        verbose_name = _("Treatment Line")
        verbose_name_plural = _("Treatment Lines")


class Regimen(models.EpisodeSubrecord):
    _sort = "start_date"
    order_by = "-start_date"

    REGIMEN_TYPES = (
        ("Induction", _("Induction")),
        ("Maintenance", _("Maintenance")),
        ("Conditioning", _("Conditioning")),
        ("Watch and wait", _("Watch and wait")),
    )

    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    nbCycles = fields.IntegerField(
        verbose_name=_("Number of Cycles"),
        null=True,
        blank=True,
    )
    start_date  = fields.DateField(
        verbose_name=_("Start Date"),
    )
    end_date    = fields.DateField(verbose_name=_("End Date"), blank=True, null=True)
    regimen     = ForeignKeyOrFreeText(RegimenList, verbose_name=_("Regimen"))
    category    = fields.CharField(max_length=40, choices=REGIMEN_TYPES, verbose_name=_("Regimen Type"))
    stop_reason = ForeignKeyOrFreeText(
        StopReason, verbose_name=_("Reason for Regimen Stop")
    )

    class Meta:
        verbose_name = _("Regimen")
        verbose_name_plural = _("Regimens")


#  TODO populate list of adverse events
class AEList(lookuplists.LookupList):
    class Meta:
        verbose_name =_ ("AE List")
        verbose_name_plural = _("AE List")
    pass

class Response(models.EpisodeSubrecord):
    _sort = "response_date"
    order_by = "-response_date"
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
        ("Response unknown/NA", _("Response unknown/NA"))
    )
    response_date = fields.DateField(verbose_name=_("Response Date"))
    response = fields.CharField(max_length=50, choices=RESPONSES, verbose_name=_("Response"))

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")

class Progression(models.EpisodeSubrecord):
    _sort = "progression_date"
    order_by = "-progression_date"
    progression_date = fields.DateField(verbose_name=_("Progresion/relapse date"))

class BloodCountFollowUp(models.PatientSubrecord):
    _sort = "followup_date"
    _icon  = "fa fa-stethoscope"
    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name = _("Hospital"))
    followup_date = fields.DateField(verbose_name=_("Visit date"))

    erythrocytes = fields.FloatField(blank = True, null = True, verbose_name = _("erythrocytes"))
    hemoglobin  = fields.FloatField(blank = True, null = True, verbose_name = _("hemoglobin"))
    hematocrit = fields.FloatField(blank = True, null = True, verbose_name = _("hematocrit"))
    mcv = fields.FloatField(blank = True, null = True, verbose_name = _("mcv"))
    mch = fields.FloatField(blank = True, null = True, verbose_name = _("mch"))
    mchc = fields.FloatField(blank = True, null = True, verbose_name = _("mchc"))
    reticulocytes = fields.FloatField(blank = True, null = True, verbose_name = _("reticulocytes"))
    leucocytes = fields.FloatField(blank = True, null = True, verbose_name = _("leucocytes"))
    myeloblasts = fields.FloatField(blank = True, null = True, verbose_name = _("myeloblasts"))
    promyelocytes = fields.FloatField(blank = True, null = True, verbose_name = _("promyelocytes"))
    myelocytes = fields.FloatField(blank = True, null = True, verbose_name = _("myelocytes"))
    eosinophils = fields.FloatField(blank = True, null = True, verbose_name = _("eosinophils"))
    basophils = fields.FloatField(blank = True, null = True, verbose_name = _("basophils"))
    lymphocytes = fields.FloatField(blank = True, null = True, verbose_name = _("lymphocytes"))
    monocytes = fields.FloatField(blank = True, null = True, verbose_name = _("monocytes"))
    plasmablasts = fields.FloatField(blank = True, null = True, verbose_name = _("plasmablasts"))
    plasmacytes = fields.FloatField(blank = True, null = True, verbose_name = _("plasmacytes"))
    platelets = fields.FloatField(blank = True, null = True, verbose_name = _("platelets"))
    b2m = fields.FloatField(blank = True, null = True, verbose_name=_("Beta-2-microglobulin"))
    albumin = fields.FloatField(blank = True, null = True, verbose_name=_("albumin"))
    ldh = fields.FloatField(blank = True, null = True, verbose_name=_("LDH"))
    class Meta:
        verbose_name = _("Blood Count")
        verbose_name_plural = _("Blood Counts")


#TODO fill with correct options
MRD_CHOICES = (
    ("Minimal", _("Minimal")),
    ("Non-minimal", _("Non-minimal"))
)
class IFT(models.PatientSubrecord):
    _sort = "ift_date"
    ift_date = fields.DateField(verbose_name = _("IFT Date"))

    YES_NO = (
        ("Yes", _("Yes")),
        ("No", _("No")),
        ("Unknown", _("Unknown"))
    )

    MRD_status = fields.CharField(max_length = 25, choices = MRD_CHOICES, blank = True, null = True, verbose_name = _("MRD status"))
    percentage_tumor_cells = fields.FloatField(blank = True, null = True, verbose_name = _("Percentage of tumor cells by IFT"))
    #TODO choices or freetext for phenotype? 
    initial_tumor_phenotype = fields.CharField(max_length = 100, blank = True, null = True, verbose_name = _("Initial phenotype of tumor cells"))
    phenotype = fields.CharField(max_length = 100, blank = True, null = True, verbose_name = _("Phenotype"))
    cd38_138_presence = fields.CharField(choices = YES_NO, max_length=4, blank = True, null = True, verbose_name = _("CD38/CD138 presence"))
    cd56_presence = fields.CharField(choices = YES_NO, max_length=4, blank = True, null = True, verbose_name = _("CD56 presence"))
    cd19_presence = fields.CharField(choices = YES_NO, max_length=4, blank = True, null = True, verbose_name = _("CD19 presence"))
    cd20_presence = fields.CharField(choices = YES_NO, max_length=4, blank = True, null = True, verbose_name = _("CD20 presence"))
    cd27_presence = fields.CharField(choices = YES_NO, max_length=4, blank = True, null = True, verbose_name = _("CD27 presence"))
    cd117_presence = fields.CharField(choices = YES_NO, max_length=4, blank = True, null = True, verbose_name = _("CD117 presence"))
    cd38cd138_percentage = fields.FloatField(blank = True, null = True, verbose_name = _("CD38/СD138, %"))
    cd56_percentage = fields.FloatField(blank = True, null = True, verbose_name = _("CD56, %"))
    cd19_percentage = fields.FloatField(blank = True, null = True, verbose_name = _("CD19, %"))
    cd20_percentage = fields.FloatField(blank = True, null = True, verbose_name = _("CD20, %"))
    cd27_percentage = fields.FloatField(blank = True, null = True, verbose_name = _("CD27, %"))
    cd117_percentage = fields.FloatField(blank = True, null = True, verbose_name = _("CD117 , %"))

class CrabCriteria(models.PatientSubrecord):
    _sort = 'crab_date'
    crab_date = fields.DateField(verbose_name = _("CRAB date"))

    CALCIUM_LEVELS = (
        ("over2.65mmol", _("> 2.65 mmol/L")),
        ("over1.5mmol", _("> 1.5 mmol/L")),
        ("Unknown", _("Unknown")),
    )

    hypercalcemia = fields.NullBooleanField(blank = True, null = True, verbose_name=_("Hypercalcemia"))
    calcium_level = fields.CharField(max_length = 30, choices = CALCIUM_LEVELS, verbose_name=_("Calcium Level"))
    renal_failure = fields.NullBooleanField(blank = True, null = True, verbose_name=_("creatinine >= 177 umol/L"))
    anemia = fields.NullBooleanField(blank = True, null = True, verbose_name=_("Hemoglobin < 100g/L or decrease of 20 g/d from norm"))
    bone_destruction = fields.NullBooleanField(blank = True, null = True, verbose_name=_("Bone destruction"))
    #TODO choice list for regions?
    region_osteolysis = fields.CharField(max_length = 50, blank=True, null=True, verbose_name=_("Region of osteolysis"))
    nb_affected_zones = fields.IntegerField(blank=True, null=True, verbose_name=_("Number of affected zones"))

class Cytogenetics(models.PatientSubrecord):
    _sort = 'cytogenetic_date'
    cytogenetic_date = fields.DateField(verbose_name= _("Cytogenetic Date"))

    CHOICES = (
        ("Yes", _("Yes")),
        ("No", _("No")),
        ("Unknown", _("Unknown"))
    )

    karyotpye = fields.CharField(max_length= 100, null=True, blank=True)
    t14_16 = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("t(14;16"))
    t4_14 = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("t(4;14)"))
    t11_14 = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("t(11;14)"))
    del13 = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("del13"))
    del17p = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("del17p"))
    ighv_rearrangement = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("IGHV rearrangement"))
    chr1_abnormalities = fields.CharField(max_length=25, null=True, blank =True, choices = CHOICES, verbose_name=_("chromosome 1 abnormalities"))
    class Meta:
        verbose_name = _("Cytogenetic tests")
        verbose_name_plural = _("Cytogenetic tests")


class TrephineBiopsy(models.PatientSubrecord):
    class Meta:
        verbose_name = _("Trephine biopsy")
        verbose_name_plural = _("Trephine biopsies")
    
    trephine_biopsy_date = fields.DateField(verbose_name=_("Trephine Biopsy Date"))
    # Cellularity
    # Percentage of hematopoietic tissue
    # Percentage of adipose tissue
    # Percentage of plasma infiltration
    # Phenotype
    # Histological and immunohistochemical features
    # indicate what should be added
    # M-Component

class BoneScan(models.PatientSubrecord):
    class Meta:
        verbose_name = _("Bone scan")
        verbose_name_plural = _("Bone scans")

    scan_date = fields.DateField(verbose_name=_("Bone Scan Date"))
    # - DZ in the skull 0-no, 1-yes
    # - DZ in the shoulder girdle 0-no, 1-yes
    # - DZ in ribs, chest 0-no, 1-yes
    # - DZ in the spine 0-no, 1-yes
    # - DZ in the pelvic bones 0-no, 1-yes
    # - DZ in long tubular bones 0-no, 1-yes
    # - MRI 1 - did not do, 2 - did
    # - MRI 1 - corresponds to Rg, 2 - improved the diagnosis
    # - CT 1 - did not do, 2 - did
    # - CT 1 - corresponds to Rg, 2 - improved the diagnosis
    # - PET-CT 1 - did not do, 2 - did
    # - PET-CT 1 - corresponds to Rg, 2 - improved diagnostics
    # - Plasmacytoma 1 - no, 2 - present
    # - Scintigraphy
    # - Compression fractures 1-no, 2 present
    # - Spinal cord compression 1 - no, 2 - yes
    # - Surgical aid 0 - did not do 1 - vertebroplasty, 2 - plate installation, 3 - - plastering

class ProteinMeasurements(models.PatientSubrecord):
    class Meta:
        verbose_name = _("Protein measurement")
        verbose_name_plural = _("Protein measurements")

        protein_measurement_date = fields.DateField(verbose_name=_("Protein measurement date"))

        # - IgG
        # - IgA
        # - IgM

        # - Bence-Jones Protein in Urine - presence 
        #   - Bence-Jones Protein in Urine - Qty/Time (only shown when box is ticked)
        # - myelokaryocytes in MG, x10 ^ 9
        # - Plasma cell count / Myelogram /,%





        # - Light Chain Secretion 
        # - Serum kappa chain
        # - Serum free kappa chain
        # - Serum Lambda Chain
        # - Free Serum Lambda Chains
        # - Urine Kappa Chain
        # - Urine Free Kappa Chains
        # - Urine Lambda Chains
        # - Urine Lambda Free Chains
        # - FLC Ratio


