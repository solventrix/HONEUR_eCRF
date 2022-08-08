"""
Templatetags for form/modal helpers
"""
from contextlib import contextmanager
import json
from django import template
from django.db import models
from opal.core.subrecords import get_subrecord_from_model_name
from opal.core import fields
from opal.core.serialization import OpalSerializer
from opal.templatetags import forms
from opal.templatetags.forms import get_style

register = template.Library()


def honour_context(*args, **kwargs):
    model, field = forms._model_and_field_from_path(kwargs["field"])
    context = {}
    context["model_api_name"] = model.get_api_name()
    context["field_name"] = field.name
    context["subrecord"] = f"editing.{context['model_api_name']}"
    return context


@register.inclusion_tag('_helpers/custom_datepicker.html')
def custom_datepicker(*args, **kwargs):
    kwargs["datepicker"] = True
    context = forms._input(*args, **kwargs)
    if 'mindate' in kwargs:
        context['mindate'] = kwargs['mindate']
    model, field = forms._model_and_field_from_path(kwargs["field"])
    context["date_after"] = kwargs.pop("date_after", "")
    context["date_after_diff"] = kwargs.pop("date_after_diff", "")
    context["date_after_message"] = kwargs.pop("date_after_message", "")

    context["date_before"] = kwargs.pop("date_before", "")
    context["date_before_diff"] = kwargs.pop("date_before_diff", "")
    context["date_before_message"] = kwargs.pop("date_before_message", "")

    context["user_options"] = kwargs.pop("user_options", False)
    context['ngrequired'] = kwargs.pop('ngrequired', '')
    context['validator'] = kwargs.pop('validator', '')
    context["ngrequired_error"] = kwargs.pop("ngrequired_error", "")

    # the defaults are no date should be after the date of death
    # or in the future.
    context['before_death'] = kwargs.pop('before_death', True)
    context['no_future'] = kwargs.pop('no_future', True)
    context.update(honour_context(*args, **kwargs))
    return context


@register.inclusion_tag('_helpers/number.html')
def number(*args, **kwargs):
    context = forms._input(*args, **kwargs)
    context["min_value"] = kwargs.get("min_value", "")
    context["max_value"] = kwargs.get("max_value", "")
    context["required"] = kwargs.get("required", "")
    context["ngrequired"] = kwargs.get("ngrequired", "")
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
    if warn_min_condition or warn_max_condition:
        warning = "{} || {}".format(
            warn_min_condition, warn_max_condition
        )
    context["min_max_warning"] = warning
    context.update(honour_context(*args, **kwargs))
    return context


@register.inclusion_tag('_helpers/radio.html')
def radio(*args, **kwargs):
    context = forms._radio(*args, **kwargs)
    context.update(honour_context(*args, **kwargs))
    return context


@register.inclusion_tag('_helpers/select.html')
def select(*args, **kwargs):
    context = forms.select(*args, **kwargs)
    context.update(honour_context(*args, **kwargs))
    return context
