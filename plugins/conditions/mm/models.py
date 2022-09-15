from django.db.models.signals import post_save
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


class MMDiagnosisDetails(models.EpisodeSubrecord):
    _is_singleton = True  # One entry per patient that is updated

    CHOICES = (("Yes", _("Yes")), ("No", _("No")), ("Unknown", _("Unknown")))

    R_ISS_STAGES = (
        ("Stage I", _("Stage I")),
        ("Stage II", _("Stage II")),
        ("Stage III", _("Stage III")),
        ("Unknown", _("Unknown")),
    )
    PP_TYPE_CHOICES = (
        ("IgG", _("IgG")),
        ("IgA", _("IgA")),
        ("IgE", _("IgE")),
        ("Light Chain Myeloma", _("Light Chain Myeloma")),
    )
    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
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
    iss_stage = fields.CharField(
        max_length=10, choices=R_ISS_STAGES, verbose_name=_("ISS Stage")
    )
    ds_stage = fields.CharField(
        max_length=10, choices=R_ISS_STAGES, verbose_name=_("DS Stage")
    )
    pp_type = fields.CharField(
        max_length=50, choices=PP_TYPE_CHOICES, verbose_name=_("PP Type")
    )
    del_17p = fields.CharField(
        max_length=10, choices=CHOICES, verbose_name=_("del(17)p")
    )
    del_13 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("del13"))
    t4_14 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("t(4;14)"))
    t4_16 = fields.CharField(max_length=10, choices=CHOICES, verbose_name=_("t(4;16)"))

    class Meta:
        verbose_name = _("Diagnosis Details")
        verbose_name_plural = _("Diagnosis Details")


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
