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
    BINET_STAGES =(
        ("Stage A", _("Stage A")),
        ("Stage B", _("Stage B")),
        ("Stage C", _("Stage C"))
    )
   
    status = fields.CharField(
        max_length=100, choices=STATUSES, verbose_name=_("Patient Status")
    )
    diag_date = fields.DateField(
        blank=False, null=True, verbose_name=_("Date of Diagnosis")
    )

    binet_stage = fields.CharField(
        max_length= 100, choices=BINET_STAGES, verbose_name = _("Binet Stage")
    )
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
    RESPONSES_IWCLL = (
        ("CR", _("Complete Remission")),
        ("PD", _("Progressive Disease")),
        ("PR", _("Partial Response")),
        ("SD", _("Stable Disease"))
    )
    response_date = fields.DateField(verbose_name=_("Response Date"))
    response = fields.CharField(max_length=50, choices=RESPONSES_IWCLL, verbose_name=_("Response"))

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")

class Cytogenetics(models.PatientSubrecord):
    _sort = 'cytogenetic_date'
    cytogenetic_date = fields.DateField(verbose_name= _("Cytogenetic Date"))

    CHOICES = (
        ("Yes", _("Yes")),
        ("No", _("No")),
        ("Unknown", _("Unknown"))
    )

    del17p = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("del17p"))
    ighv_rearrangement = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES, verbose_name = _("IGHV rearrangement"))
    del11q = fields.CharField(max_length=25, null = True, blank=True, choices = CHOICES, verbose_name = _("del11q"))
    tp53_mutation = fields.CharField(max_length=25, null=True, blank=True,choices=CHOICES,verbose_name=_("TP53 mutation"))
    class Meta:
        verbose_name = _("Cytogenetic tests")
        verbose_name_plural = _("Cytogenetic tests")

class FollowUp(models.PatientSubrecord):
    _sort = "followup_date"
    _icon = "fa fa-stethoscope"
    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    follow_up_date = fields.DateField(verbose_name=_("Visit date"))

    LDH = fields.FloatField(blank=True, null=True, verbose_name=_("LDH"))
    beta2m = fields.FloatField(blank=True, null=True, verbose_name=_("beta2m"))
    albumin = fields.FloatField(blank=True, null=True, verbose_name=_("Albumin"))
    mprotein_urine = fields.FloatField(blank=True, null=True, verbose_name=_("MProtein Urine"))
    mprotein_serum = fields.FloatField(blank = True, null = True ,verbose_name=("MProtein Serum"))
    mprotein_24h = fields.FloatField(blank = True, null = True, verbose_name=_("Mprotein in 24 hour urine"))

    class Meta:
        verbose_name = _("Follow-up")
        verbose_name_plural = _("Follow-ups")
