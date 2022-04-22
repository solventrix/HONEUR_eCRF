from django.forms import CharField
from django.utils.translation import gettext_lazy as _
from django.db import models as fields
from opal.core.fields import ForeignKeyOrFreeText
from opal.core import lookuplists
from opal import models
from entrytool.models import Hospital


class MMRegimenList(lookuplists.LookupList):
    class Meta:
        verbose_name = _("MM Regimen List")
        verbose_name_plural = _("MM Regimen List")


class MMStopReason(lookuplists.LookupList):
    class Meta:
        verbose_name = _("MM Stop Reason List")
        verbose_name_plural = _("MM Stop Reason List")


class MMPastMedicalHistory(models.PatientSubrecord):
    _is_singleton = True
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

    previous_neoplasm_2 = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Prevous Neoplasm 2")
    )
    previous_neoplasm_date_of_diagnosis_2 = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of Diagnosis")
    )
    previous_neoplasm_details_2 = fields.TextField(
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
        blank=True, null=True, verbose_name=_("Diagnosis Date")
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
    comments = fields.TextField(blank=True, default="", verbose_name=_("Comments"))

    class Meta:
        verbose_name = _("Past Medical History")
        verbose_name_plural = _("Past Medical Histories")


class MMDiagnosisDetails(models.EpisodeSubrecord):
    _is_singleton = True  # One entry per patient that is updated
    CHOICES = (("Yes", _("Yes")), ("No", _("No")),)

    R_ISS_STAGES = (
        ("Stage I", _("Stage I")),
        ("Stage II", _("Stage II")),
        ("Stage III", _("Stage III")),
        ("Unknown", _("Unknown")),
    )

    # TODO check that this list is exhaustive
    SUBCLASSIFICATION_CHOICES = (
            ("MM IgG Kappa", _("MM IgG Kappa"),),
            ("MM IgA Kappa", _("MM IgA Kappa"),),
            ("MM IgD Kapper", _("MM IgD Kapper"),),
            ("MM IgE Kapper", _("MM IgE Kapper"),),
            ("MM Light Chain Kappa", _("MM Light Chain Kappa"),),

            ("MM IgG Lambda", _("MM IgG Lambda"),),
            ("MM IgA Lambda", _("MM IgA Lambda"),),
            ("MM IgD Lambda", _("MM IgD Lambda"),),
            ("MM IgE Lambda", _("MM IgE Lambda"),),
            ("MM Light Chain Lambda", _("MM Light Chain Lambda"),),

            ("Other", _("Other"),),
    )

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

    DIAGNOSIS_OPTIONS = (
        ("Solitary Bone Plasmacytoma", _("Solitary Bone Plasmacytoma"))
        ("Symptomatic Multiple Myeloma", _("Symptomatic Multiple Myeloma")),
        ("Plasmatic Celiac Leukemia", _("Plasmatic Celiac Leukemia")),
        ("Primary Amylodosis", _("Primary Amylodosis")),
        ("Asymptomatic MM", _("Asymptomatic MM")),
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

    infection_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=INFECTION_TYPE_CHOICES,
        verbose_name=_("")
    )
    diagnosis = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=DIAGNOSIS_OPTIONS,
        verbose_name=_("Diagnosis")
    )
    subclassification = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SUBCLASSIFICATION_CHOICES,
        verbose_name=_("SUBCLASSIFICATION")
    )

    riss_stage = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=R_ISS_STAGES,
        verbose_name=_("R-ISS Stage")
    )

    # GAH Score 0 to 94
    gah_score = models.IntegerField(
        blank=True, null=True, verbose_name=_("GAH Score")
    )
    # IMWG Scale 1 to 8
    imwg_scale = fields.IntegerField(
        blank=True, null=True, verbose_name=_("IMWG Scale")
    )
    # ICC scale 0 to 31
    cc_scale = fields.IntegerField(blank=True, null=True, verbose_name=_("ICC Scale"))

    ircp_diag_date = models.DateField(
        blank=True, null=True, verbose_name=_("IRCP Diagnosis Date")
    )

    class Meta:
        verbose_name = _("Diagnosis Details")
        verbose_name_plural = _("Diagnosis Details")


class Cytogenetics(models.EpisodeSubrecord):
    CHOICES = CHOICES = (("Yes", _("Yes")), ("No", _("No")),)

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
    t4_14 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("t(4;14)"))
    t4_14_16 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("t(14;16)"))
    t11_14 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("t(11;14)"))
    comments = models.TextField(blank=True, default="", verbose_name=_(""))


class LabTests(models.EpisodeSubrecord):
    # Troponine I, ng/L, min 0 max 350
    troponina = models.IntegerField(blank=True, null=True, verbose_name=_("Troponina"))
    total_proteins = models.IntegerField(blank=True, null=True, verbose_name=_("Total Proteins"))


class Imaging(models.EpisodeSubrecord):
    CT_SCAN_OPTIONS = (
        ("Blank", _("Blank")),
        ("Negative", _("Negative")),
        ("Positive", _("Positive")),
        ("Not Done", _("Not Done")),
    )
    ct_scan = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CT_SCAN_OPTIONS,
        verbose_name=_("CT Scan")
    )
    ct_scan_description = models.TextField(
        blank=True, default="", verbose_name=_("CT Scan Description")
    )


class MMRegimen(models.EpisodeSubrecord):
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
    start_date = fields.DateField(
        verbose_name=_("Start Date"),
    )
    end_date = fields.DateField(verbose_name=_("End Date"), blank=True, null=True)
    regimen = ForeignKeyOrFreeText(MMRegimenList, verbose_name=_("Regimen"))
    category = fields.CharField(
        max_length=40, choices=REGIMEN_TYPES, verbose_name=_("Regimen Type")
    )
    stop_reason = ForeignKeyOrFreeText(
        MMStopReason, verbose_name=_("Reason for Regimen Stop")
    )

    class Meta:
        verbose_name = _("Regimen")
        verbose_name_plural = _("Regimens")


class MMResponse(models.EpisodeSubrecord):
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
        ("Response unknown/NA", _("Response unknown/NA")),
    )
    response_date = fields.DateField(verbose_name=_("Response Date"))
    response = fields.CharField(
        max_length=50, choices=RESPONSES, verbose_name=_("Response")
    )

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")


class MMFollowUp(models.EpisodeSubrecord):
    _sort = "followup_date"
    _icon = "fa fa-stethoscope"
    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    follow_up_date = fields.DateField(verbose_name=_("Visit date"))

    LDH = fields.FloatField(blank=True, null=True, verbose_name=_("LDH"))
    beta2m = fields.FloatField(blank=True, null=True, verbose_name=_("beta2m"))
    albumin = fields.FloatField(blank=True, null=True, verbose_name=_("Albumin"))
    mprotein_urine = fields.FloatField(
        blank=True, null=True, verbose_name=_("MProtein Urine")
    )
    mprotein_serum = fields.FloatField(
        blank=True, null=True, verbose_name=("MProtein Serum")
    )
    mprotein_24h = fields.FloatField(
        blank=True, null=True, verbose_name=_("Mprotein in 24 hour urine")
    )

    class Meta:
        verbose_name = _("Follow-up")
        verbose_name_plural = _("Follow-ups")
