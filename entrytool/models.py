"""
entrytool models.
"""
from django.db.models import fields

from opal import models
from opal.core import lookuplists
from opal.core.fields import ForeignKeyOrFreeText, enum
from django.utils.translation import gettext_lazy as _


class Demographics(models.Demographics):
    _icon = ''
    pass


class Location(models.Location):
    pass


class Diagnosis(models.Diagnosis):
    pass


class Hospital(lookuplists.LookupList):
    pass


class SCT(models.EpisodeSubrecord):
    SCT_TYPES = enum("Allogenic", "Autologous", "Unknown")
    order_by = "-sct_date"

    sct_date = fields.DateField(verbose_name=_("Date of SCT"))
    hospital = models.ForeignKeyOrFreeText(Hospital)
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

    STATUSES = enum(
         "Under Treatment",
         "Dead",
         "Lost to Follow-up"
    )
    hospital = models.ForeignKeyOrFreeText(Hospital)

    CHOICES = enum("Yes", "No", "Unknown")
    DEATH_CAUSES = enum("Disease", "Complications of Disease", "Other")
    R_ISS_STAGES = enum("Stage I", "Stage II", "Stage III")
    PP_TYPE_CHOICES = enum("IgG", "IgA", "IgE", "Light Chain Myeloma")

    status = fields.CharField(
        max_length=100, choices=STATUSES, verbose_name=_("Patient Status")
    )
    diag_date = fields.DateField(
        blank=False, null=True, verbose_name=_("Date of Diagnosis")
    )
    smm_history = fields.CharField(
        max_length=10, choices=CHOICES, verbose_name=_("History of SMM")
    )
    smm_history_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Date of SMM diagnosis")
    )
    mgus_history = fields.CharField(
        max_length=10, choices=CHOICES, verbose_name=_("History of MGUS")
    )
    mgus_history_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Date of MGUS Diagnosis")
    )
    r_iss_stage = fields.CharField(
        max_length=10, choices=R_ISS_STAGES, verbose_name=_("R-ISS Stage")
    )
    pp_type = fields.CharField(
        max_length=50, choices=PP_TYPE_CHOICES, verbose_name="PP Type"
    )
    del_17p = fields.CharField(max_length=10, choices=CHOICES, verbose_name="del(17)p")
    t4_14 = fields.CharField(max_length=10, choices=CHOICES, verbose_name="t(4;14)")
    t4_16 = fields.CharField(max_length=10, choices=CHOICES, verbose_name="t(4;16)")
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


class RegimenList(lookuplists.LookupList):
    pass


class StopReason(lookuplists.LookupList):
    pass


# TODO does this need to be kept? Can the line number be an attribute of the episode?
class TreatmentLine(models.EpisodeSubrecord):
    nb = fields.IntegerField(verbose_name=_("Treatment Line"))


class Regimen(models.EpisodeSubrecord):
    _sort = "start_date"
    order_by = "-start_date"

    REGIMEN_TYPES = enum(
        _("Induction"),
        _("Maintenance"),
        _("Conditioning"),
        _("Watch and wait"),
    )

    hospital = models.ForeignKeyOrFreeText(Hospital)
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
    category    = fields.CharField(max_length=40, choices=REGIMEN_TYPES, verbose_name="Regimen Type")
    stop_reason = ForeignKeyOrFreeText(
        StopReason, verbose_name=_("Reason for Regimen Stop")
    )


#  TODO populate list of adverse events
class AEList(lookuplists.LookupList):
    pass


class AdverseEvent(models.EpisodeSubrecord):
    order_by = "-ae_date"

    SEV_CHOICES = enum("I", "II", "III", "IV", "V")

    adverse_event = ForeignKeyOrFreeText(AEList, verbose_name=_("Adverse Event"))
    severity = fields.CharField(
        max_length=4, choices=SEV_CHOICES, verbose_name=_("Severity")
    )
    ae_date = fields.DateField(verbose_name=_("Date of AE"))


class Response(models.EpisodeSubrecord):
    _sort = "response_date"
    order_by = "-response_date"
    RESPONSES = enum(
        "Minimal response",
        "Partial response",
        "Very good partial response",
        "Complete response",
        "Stringent complete response",
        "Near complete response",
        "Immunophenotypic complete response",
        "Stable disease",
        "Progressive disease",
        "Response unknown"
    )
    response_date = fields.DateField()
    response = fields.CharField(max_length=50, choices=RESPONSES)


class FollowUp(models.PatientSubrecord):
    _sort = "followup_date"
    _icon = "fa fa-stethoscope"
    hospital = models.ForeignKeyOrFreeText(Hospital)
    follow_up_date = fields.DateField(verbose_name=_("Visit date"))

    LDH = fields.IntegerField(blank=True, null=True)
    beta2m = fields.IntegerField(blank=True, null=True)
    albumin = fields.IntegerField(blank=True, null=True)
    creatinin = fields.IntegerField(blank=True, null=True)
    MCV = fields.IntegerField(blank=True, null=True)
    Hb = fields.IntegerField(blank=True, null=True)
    kappa_lambda_ratio = fields.FloatField(blank=True, null=True)
    bone_lesions = fields.FloatField(blank=True, null=True)
