"""
Templatetags for form/modal helpers
"""
import json
from django import template
from django.db import models
from opal.core.subrecords import get_subrecord_from_model_name
from opal.core import fields
from opal.core.serialization import OpalSerializer
from opal.templatetags import forms
from opal.templatetags.forms import get_style

register = template.Library()

@register.inclusion_tag('_helpers/custom_datepicker.html')
def custom_datepicker(*args, **kwargs):
    kwargs["datepicker"] = True
    context = forms._input(*args, **kwargs)
    if 'mindate' in kwargs:
        context['mindate'] = kwargs['mindate']
    model, _ = forms._model_and_field_from_path(kwargs["field"])

    context["model_name"] = "editing.{}".format(model.get_api_name())

    context["date_after"] = kwargs.pop("date_after", "")
    context["date_after_diff"] = kwargs.pop("date_after_diff", "")
    context["date_after_message"] = kwargs.pop("date_after_message", "")

    context["date_before"] = kwargs.pop("date_before", "")
    context["date_before_diff"] = kwargs.pop("date_before_diff", "")
    context["date_before_message"] = kwargs.pop("date_before_message", "")

    context["user_options"] = kwargs.pop("user_options", False)
    context['ngrequired'] = kwargs.pop('ngrequired', '')
    context['validator'] = kwargs.pop('validator', '')

    # the defaults are no date should be after the date of death
    # or in the future.
    context['before_death'] = kwargs.pop('before_death', True)
    context['no_future'] = kwargs.pop('no_future', True)
    return context


@register.inclusion_tag('_helpers/number.html')
def number(*args, **kwargs):
    context = forms._input(*args, **kwargs)
    context["min_value"] = kwargs.get("min_value", "")
    context["max_value"] = kwargs.get("max_value", "")
    warn_min = kwargs.get("warn_min", "")
    warn_max = kwargs.get("warn_max", "")
    warn_min_condition = None
    warn_max_condition = None
    warning = None
    if warn_min:
        warn_min_condition = "{} <= {}".format(
            context["model"], warn_min
        )
    if warn_max:
        warn_max_condition = "{} >= {}".format(
            context["model"], warn_max
        )
    if warn_min_condition and warn_max_condition:
        warning = "{} || {}".format(
            warn_min_condition, warn_max_condition
        )
    context["min_max_warning"] = warning
    return context
