import datetime
from re import I
from django.views.generic import TemplateView
from django.utils.translation import get_language
from django.db.models import Q, Max, DateField, DateTimeField
from entrytool.models import PatientStatus
from opal.models import Patient, EpisodeSubrecord
from opal.core import subrecords


class ValidationRules(TemplateView):
    template_name = "validation_rules.js"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, content_type="text/javascript")


class AngularLocale(TemplateView):
    """
    Because we can't guarentee hospitals have white listed cdns
    and so that we can provide datepicker translations we generate
    the angular locale file on the fly with translations from
    the .po

    This is usGed by the datepicker

    expected values
    Hebrew(he)
    locale_dash=he local_underscore=he

    Brazilian portuguese(pt-br)
    locale_dash=pt-br local_underscore=pt_BR
    """
    http_method_names = ['get']
    template_name = "angular_locale.html"

    def get(self, request):
        lang = language = get_language()
        local_underscore = lang
        if "-" in local_underscore:
            splitted = local_underscore.split("-")
            local_underscore = "{}_{}".format(
                splitted[0], splitted[1].upper()
            )
        ctx = {
            "locale_dash": lang,
            "local_underscore": local_underscore
        }
        return self.render_to_response(ctx, content_type="text/javascript")


class OrphanedRecords(TemplateView):
    template_name = "patient_lists/orphaned_records.html"

    @property
    def since(self):
        """
        Anything older than this date is considered orphaned
        """
        return datetime.date.today() - datetime.timedelta(180)

    def get_date_fields(self, subrecord):
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

    def get_max_date(self, patient, max_fields):
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
        return max(max_dates)

    def get_patient_list(self):
        """
        Returns a list of (most_recent_date, patient_id)
        of all patients that are not deceased/lost
        and have not been updated since self.since
        """
        qs = Patient.objects.all().exclude(
            Q(patientstatus__deceased=True) |
            Q(patientstatus__lost_to_follow_up=True) |
            Q(patientstatus__discharged=True)
        )
        max_fields = []
        for subrecord in subrecords.subrecords():
            if subrecord == PatientStatus:
                continue
            date_fields = self.get_date_fields(subrecord)
            for date_field in date_fields:
                if issubclass(subrecord, EpisodeSubrecord):
                    field = f"episode__{subrecord.__name__.lower()}__{date_field}"
                else:
                    field = f"{subrecord.__name__.lower()}__{date_field}"
                print(f"field {field}")
                field_filter = f"{field}__gte"
                qs = qs.exclude(**{field_filter: self.since})

                max_field = f"max_{field}"
                qs = qs.annotate(**{max_field: Max(field)})
                max_fields.append(max_field)

        max_date_and_patient_id = [
            (self.get_max_date(patient, max_fields), patient.id,) for
            patient in qs
        ]
        return sorted(max_date_and_patient_id, key=lambda x: x[0])

    def get_context_data(self, *args, **kwargs):
        """
        Returns the template context for the view
        """
        ctx = super().get_context_data(*args, **kwargs)
        ctx["object_list"] = self.get_patient_list
        return ctx
