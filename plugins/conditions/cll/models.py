from django.utils.translation import gettext_lazy as _
from django.db import models as fields
from opal.core import lookuplists
from opal.core.fields import ForeignKeyOrFreeText
from opal import models
from entrytool.models import Hospital


class CLLRegimenList(lookuplists.LookupList):
    class Meta:
        verbose_name = _("CLL Regimen List")
        verbose_name_plural = _("CLL Regimen List")


class CLLStopReason(lookuplists.LookupList):
    class Meta:
        verbose_name = _("CLL Stop Reason List")
        verbose_name_plural = _("CLL Stop Reason List")


class CLLDiagnosisDetails(models.EpisodeSubrecord):
    _is_singleton = True  # One entry per patient that is updated

    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))

    CHOICES = (("Yes", _("Yes")), ("No", _("No")), ("Unknown", _("Unknown")))

    BINET_STAGES = (
        ("Stage A", _("Stage A")),
        ("Stage B", _("Stage B")),
        ("Stage C", _("Stage C")),
        ("Unknown", _("Unknown")),
    )

    diag_date = fields.DateField(
        blank=False, null=True, verbose_name=_("Date of Diagnosis")
    )

    binet_stage = fields.CharField(
        max_length=100,
        choices=BINET_STAGES,
        verbose_name=_("Binet Stage"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Diagnosis details")
        verbose_name_plural = _("Diagnosis details")


class CLLRegimen(models.EpisodeSubrecord):
    _sort = "start_date"
    order_by = "-start_date"

    REGIMEN_TYPES = (
        ("Treatment", _("Treatment")),
        ("Observation after remission", _("Observation after remission")),
    )

    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    nbCycles = fields.IntegerField(
        verbose_name=_("Number of Cycles"),
        null=True,
        blank=True,
    )
    start_date = fields.DateField(
        verbose_name=_("Start Date"), blank=True, null=True
    )
    end_date = fields.DateField(verbose_name=_("End Date"), blank=True, null=True)
    regimen = ForeignKeyOrFreeText(CLLRegimenList, verbose_name=_("Regimen"))
    category = fields.CharField(
        max_length=40, choices=REGIMEN_TYPES, verbose_name=_("Regimen Type")
    )
    stop_reason = ForeignKeyOrFreeText(
        CLLStopReason, verbose_name=_("Reason for Regimen Stop")
    )
    part_of_clinical_trial = fields.NullBooleanField(
        verbose_name=_("Regimen part of clinical trial"), blank=True, null=True
    )
    indefinite_duration = fields.NullBooleanField(
        verbose_name=_("Treatment of indefinite duration"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Regimen")
        verbose_name_plural = _("Regimens")


class BestResponse(models.EpisodeSubrecord):
    _sort = "response_date"
    order_by = "-response_date"
    RESPONSES_IWCLL = (
        ("CR", _("Complete Remission")),
        ("PD", _("Progressive Disease")),
        ("PR", _("Partial Response")),
        ("SD", _("Stable Disease")),
        ("Unknown", _("Unknown")),
    )
    response_date = fields.DateField(
        verbose_name=_("Response Date"), blank=True, null=True
    )
    response = fields.CharField(
        max_length=50, choices=RESPONSES_IWCLL, verbose_name=_("Best Response")
    )


class QualityOfLife5Q(models.EpisodeSubrecord):
    _sort = "q5_date"
    q5_date = fields.DateField(
        verbose_name=_("Date of Questionnaire"), blank=True, null=True
    )

    Q5_OPTIONS = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))

    q5_mobility = fields.FloatField(
        blank=True, null=True, choices=Q5_OPTIONS, verbose_name=_("Mobility")
    )
    q5_selfcare = fields.FloatField(
        blank=True, null=True, choices=Q5_OPTIONS, verbose_name=_("Selfcare")
    )
    q5_usual_activities = fields.FloatField(
        blank=True, null=True, choices=Q5_OPTIONS, verbose_name=_("Usual Activities")
    )
    q5_pain_discomfort = fields.FloatField(
        blank=True, null=True, choices=Q5_OPTIONS, verbose_name=_("Pain/Discomfort")
    )
    q5_anxiety_depression = fields.FloatField(
        blank=True, null=True, choices=Q5_OPTIONS, verbose_name=_("Anxiety/Depression")
    )


class AdditionalCharacteristics(models.EpisodeSubrecord):
    _sort = "characteristic_date"
    characteristic_date = fields.DateField(
        verbose_name=_("Date of measurement"), blank=True, null=True
    )

    CHOICES = (("Yes", _("Yes")), ("No", _("No")), ("Unknown", _("Unknown")))
    ECOG_CHOICES = ((0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"))

    ecog_score = fields.FloatField(
        blank=True, null=True, verbose_name=_("ECOG"), choices=ECOG_CHOICES
    )
    cirs_score = fields.FloatField(blank=True, null=True, verbose_name=_("CIRS"))
    creatinine_clearance = fields.FloatField(
        blank=True, null=True, verbose_name=_("Creatinine clearance")
    )
    beta2m = fields.FloatField(
        blank=True, null=True, verbose_name=_("Beta-2-Microglobulin")
    )
    LDH = fields.FloatField(blank=True, null=True, verbose_name=_("LDH"))
    bulky_disease = fields.CharField(
        blank=True,
        null=True,
        choices=CHOICES,
        verbose_name=_("Bulky disease present"),
        max_length=25,
    )


class Cytogenetics(models.EpisodeSubrecord):
    _sort = "cytogenetic_date"
    cytogenetic_date = fields.DateField(
        verbose_name=_("Cytogenetic Date"), blank=True, null=True
    )

    CHOICES = (("Yes", _("Yes")), ("No", _("No")), ("Unknown", _("Unknown")))
    CHOICES_IGHV = (
        ("Mutated", _("Mutated")),
        ("Non-mutated", _("Non-mutated")),
        ("Unknown", _("Unknown")),
    )

    del17p = fields.CharField(
        max_length=25, null=True, blank=True, choices=CHOICES, verbose_name=_("del17p")
    )
    ighv_rearrangement = fields.CharField(
        max_length=25,
        null=True,
        blank=True,
        choices=CHOICES_IGHV,
        verbose_name=_("IGHV rearrangement"),
    )
    del11q = fields.CharField(
        max_length=25, null=True, blank=True, choices=CHOICES, verbose_name=_("del11q")
    )
    tp53_mutation = fields.CharField(
        max_length=25,
        null=True,
        blank=True,
        choices=CHOICES,
        verbose_name=_("TP53 mutation"),
    )
    karyotype = fields.CharField(
        max_length=25,
        null=True,
        blank=True,
        choices=CHOICES,
        verbose_name=_("Complex Karyotype"),
    )

    class Meta:
        verbose_name = _("Cytogenetic tests")
        verbose_name_plural = _("Cytogenetic tests")
