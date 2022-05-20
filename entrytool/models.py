"""
entrytool models.
"""
from django.db.models import fields

from opal import models
from opal.core import lookuplists
from django.utils.translation import gettext_lazy as _


class Demographics(models.Demographics):
    _icon = ''
    external_identifier = fields.CharField(
        blank=True, null=True, max_length=256, unique=True,
        verbose_name=_("External Identifier")
    )
    comments = fields.TextField(blank=True, default="", verbose_name=_("Comments"))


class Hospital(lookuplists.LookupList):
    class Meta:
        verbose_name = _("Hospital")
        verbose_name_plural = _("Hospitals")


class SCT(models.EpisodeSubrecord):
    CHOICES = (("Yes", _("Yes")), ("No", _("No")),)
    SCT_TYPES = (
        ("Allogenic", _("Allogenic")),  # ALOTPH
        ("Autologous", _("Autologous")),   # ATSP

        ("Unknown", _("Unknown")),
    )

    ALOTPH_TYPES = (
        ("HLA identical", _("HLA identical"),),
        ("HLA identicofen", _("HLA identicofen"),),
        (
            "Aplo: HLA unidentified related (>1 missmatch) phenotype",
            _("Aplo: HLA unidentified related (>1 missmatch) phenotype"),
        ),
        (
            "HLA no related ident (NO HAPLO: 1 missmatch)",
            _("HLA no related ident (NO HAPLO: 1 missmatch)"),
        ),
        (
            "HLA0 identical unrelated",
            _("HLA0 identical unrelated")
        ),
        (
            "HLA-non-identical unrelated", _("HLA-non-identical unrelated")
        ),
        (
            # TODO google translates this as a stranger... we will ask for a better tranlsation
            "An unknown",
            _("An unkown")
        ),
        ("Other", _("Other"))
    )

    ALOTPH_CONDITION_OPTIONS = (
        ("BU-FLU", _("BU-FLU"),),
        ("TT-BU-FLU", _("TT-BU-FLU"),),
        ("TT-FLU-BU", _("TT-FLU-BU"),),
        ("Cyclophosphamide-ATG", _("Cyclophosphamide-ATG"),),
        ("TT-BU-FLU-ATG", _("TT-BU-FLU-ATG"),),
        ("TT-FLU-BU-ATG", _("TT-FLU-BU-ATG"),),
        ("FLU-Cyclophosphamide-ATG", _("FLU-Cyclophosphamide-ATG"),),
        ("FLU-ATG", _("FLU-ATG"),),
    )

    ATSP_CONDITION_OPTIONS = (
        ("BEA", _("BEA"),),
        ("BUCY", _("BUCY"),),
        ("Melfalan 140", _("Melfalan 140"),),
        ("Melfalan 200", _("Melfalan 200"),),
        ("BU-MEL", _("BU-MEL"),),
        ("BEAM", _("BEAM"),),
    )

    ALOTPH_SOURCE_OPTIONS = (
        ("Bone Marrow", _("Bone Marrow"),),
        ("Cord", _("Cord"),),
        ("Peripheral Bloods", _("Peripheral Bloods"),),
        ("Bone Marrow And Peripheral Bloods", _("Bone Marrow And Peripheral Bloods"),),
        ("Other", _("Other"),),
        ("Unknown", _("Unknown"),),
    )

    order_by = "-sct_date"

    sct_date = fields.DateField(blank=True, null=True, verbose_name=_("Date of SCT"))
    number_of_cells_infused = fields.BigIntegerField(
        blank=True, null=True, verbose_name=_("Number Of Cells Infused")
    )
    sct_type = fields.CharField(
        max_length=12,
        verbose_name=_("Type of SCT"),
        choices=SCT_TYPES,
        null=True
    )

    # if SCT_Type == Allogenic
    relation = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=ALOTPH_TYPES,
        verbose_name=_("Relation")
    )
    alotph_conditioning = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=ALOTPH_CONDITION_OPTIONS,
        verbose_name=_("Conditioning")
    )

    alotph_source = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=ALOTPH_SOURCE_OPTIONS,
        verbose_name=_("Source")
    )

    # if SCT type == Autologous
    tandem_astp = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Tandem ASTP")
    )
    atsp_conditioning = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=ATSP_CONDITION_OPTIONS,
        verbose_name=_("Conditioning")
    )

    class Meta:
        verbose_name = _("Stem Cell Transplant")
        verbose_name_plural = _("Stem Cell Transplants")


class PatientStatus(models.PatientSubrecord):
    _is_singleton = True
    DEATH_CAUSES = (
        ("Mieloma Multiple", _("Mieloma Multiple"),),
        ("Infection", _("Infection"),),
        ("Other", _("Other"))
    )
    deceased = fields.NullBooleanField(verbose_name=_("Deceased"), blank=True, null= True)
    lost_to_follow_up = fields.NullBooleanField(verbose_name=_("Lost to Follow-Up"), null = True, blank = True)
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
        verbose_name = _("Patient status")
        verbose_name_plural = _("Patient status")


# TODO does this need to be kept? Can the line number be an attribute of the episode?
class TreatmentLine(models.EpisodeSubrecord):
    nb = fields.IntegerField(verbose_name=_("Treatment Line"))

    class Meta:
        verbose_name = _("Treatment Line")
        verbose_name_plural = _("Treatment Lines")


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
