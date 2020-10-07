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
    )
    PP_TYPE_CHOICES = (
        ("IgG", _("IgG")),
        ("IgA", _("IgA")),
        ("IgE", _("IgE")),
        ("Light Chain Myeloma", _("Light Chain Myeloma")),
    )
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
        max_length=50, choices=PP_TYPE_CHOICES, verbose_name=_("PP Type")
    )
    del_17p = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("del(17)p"))
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
        blank=True, null=True, verbose_name=_("Lost to Follow-up ")
    )

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


class AdverseEvent(models.EpisodeSubrecord):
    order_by = "-ae_date"

    SEV_CHOICES = (
        ("I", _("I")),
        ("II", _("II")),
        ("III", _("III")),
        ("IV", _("IV")),
        ("V", _("V"))
    )
    adverse_event = ForeignKeyOrFreeText(AEList, verbose_name=_("Adverse Event"))
    severity = fields.CharField(
        max_length=4, choices=SEV_CHOICES, verbose_name=_("Severity")
    )
    ae_date = fields.DateField(verbose_name=_("Date of AE"))

    class Meta:
        verbose_name = _("Adverse Event")
        verbose_name_plural = _("Adverse Event")


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
        ("Response unknown", _("Response unknown"))
    )
    response_date = fields.DateField(verbose_name=_("Response Date"))
    response = fields.CharField(max_length=50, choices=RESPONSES, verbose_name=_("Response"))

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")


class FollowUp(models.PatientSubrecord):
    _sort = "followup_date"
    _icon = "fa fa-stethoscope"
    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    follow_up_date = fields.DateField(verbose_name=_("Visit date"))

    LDH = fields.FloatField(blank=True, null=True, verbose_name=_("LDH"))
    beta2m = fields.FloatField(blank=True, null=True, verbose_name=_("beta2m"))
    albumin = fields.FloatField(blank=True, null=True, verbose_name=_("Albumin"))
    creatinin = fields.FloatField(blank=True, null=True, verbose_name=_("Creatinin"))
    MCV = fields.FloatField(blank=True, null=True, verbose_name=_("MCV"))
    Hb = fields.FloatField(blank=True, null=True, verbose_name=_("Hb"))
    kappa_lambda_ratio = fields.FloatField(blank=True, null=True, verbose_name=_("Kappa Lambda Ratio"))
    bone_lesions = fields.FloatField(blank=True, null=True, verbose_name=_("Bone Lesions"))

    class Meta:
        verbose_name = _("Follow-up")
        verbose_name_plural = _("Follow-ups")
