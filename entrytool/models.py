"""
entrytool models.
"""
import datetime
from django.db.models import fields
from opal.core import subrecords
from django.db.models import Max, DateField, DateTimeField

from opal import models
from opal.core import lookuplists
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

    sct_date = fields.DateField(verbose_name=_("Date of SCT"), blank=True, null=True)
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


class PatientStatus(models.PatientSubrecord):
    _is_singleton = True
    DEATH_CAUSES = (
        ("Disease", _("Disease")),
        ("Complications of Disease", _("Complications of Disease")),
        ("Other", _("Other"))
    )
    physician = fields.CharField(
        null=True, blank=True, max_length=256, verbose_name=_("Physician")
    )
    status = fields.CharField(
        null=True, blank=True, max_length=256, verbose_name=_("Status")
    )
    deceased = fields.NullBooleanField(verbose_name=_("Deceased"), blank=True, null= True)
    lost_to_follow_up = fields.NullBooleanField(verbose_name=_("Lost to Follow-Up"), null = True, blank = True)
    date_of_last_contact = fields.DateField(
        null=True, verbose_name=_("Date of Last Contact"), blank=True
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


class PatientLoad(models.PatientSubrecord):
    """
    A singleton that describes what created a patient whether
    it was the loaded in from an external source like a file
    or created by the front end.
    """
    _is_singleton = True

    LOADED_FROM_FILE = "Loaded From File"
    CREATED_FROM_UI = "Created From UI"

    SOURCE = (
        (LOADED_FROM_FILE, _("Loaded From File")),
        (CREATED_FROM_UI, _("Created From UI")),
    )

    source = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SOURCE,
        verbose_name=_("source"),
        default=CREATED_FROM_UI
    )
    validated = fields.BooleanField(
        default=False, verbose_name=_("Validated"),
    )
    has_errors = fields.BooleanField(
        default=False, verbose_name=_("Has Errors"),
    )
    data_quality_reviewed = fields.BooleanField(
        default=False, verbose_name=_("Data Quality Reviewed")
    )
    data_quality_reviewed_date = fields.DateField(blank=True, null=True)

    class Meta:
        verbose_name = _("Patient Load")
        verbose_name_plural = _("Patient Loads")


def get_date_fields(subrecord):
    """
    Returns the names of date or datetime fields on the subrecord
    excluding the created/updated timestamps
    """
    fields = subrecord._meta.get_fields()
    date_fields = []
    for field in fields:
        if isinstance(field, (DateTimeField, DateField,)):
            if field.name == 'created' or field.name == 'updated':
                continue
            date_fields.append(field.name)
    return date_fields


def get_max_date(patient, max_fields):
    """
    Given a list of annotated max_date fields on the patient
    return the most recent
    """
    max_dates = [
        getattr(patient, max_field) for max_field in max_fields
        if getattr(patient, max_field)
    ]
    if len(max_dates) == 1:
        return max_dates[0]
    elif len(max_dates) == 0:
        return None
    return max(max_dates)


def sort_by_newest_to_oldest(patients):
    """
    Takes a queryset

    Annotates with all the dates connected with the patient
    excluding created/updated

    Returns a list of patients ordered by newest to oldest.
    """
    max_fields = []
    for subrecord in subrecords.subrecords():
        if subrecord == PatientStatus:
            continue
        date_fields = get_date_fields(subrecord)
        for date_field in date_fields:
            if issubclass(subrecord, models.EpisodeSubrecord):
                field = f"episode__{subrecord.__name__.lower()}__{date_field}"
            else:
                field = f"{subrecord.__name__.lower()}__{date_field}"
            max_field = f"max_{field}"
            patients = patients.annotate(**{max_field: Max(field)})
            max_fields.append(max_field)

    max_date_and_patient = [
        (get_max_date(patient, max_fields), patient) for
        patient in patients
    ]
    return [
        i[1] for i in sorted(
            max_date_and_patient,
            key=lambda x: x[0] or datetime.datetime.min.date(),
            reverse=True
        )
    ]
