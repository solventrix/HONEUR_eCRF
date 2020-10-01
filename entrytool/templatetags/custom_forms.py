"""
Templatetags for form/modal helpers
"""
import json
from django import template
from django.db import models
from opal.core.subrecords import get_subrecord_from_model_name
from opal.core import fields
from opal.utils import camelcase_to_underscore
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

    context["date_after"] = kwargs.pop("date_after", "")
    context["date_after_diff"] = kwargs.pop("date_after_diff", "")
    context["date_after_message"] = kwargs.pop("date_after_message", "")

    context["date_before"] = kwargs.pop("date_before", "")
    context["date_before_diff"] = kwargs.pop("date_before_diff", "")
    context["date_before_message"] = kwargs.pop("date_before_message", "")

    context["user_options"] = kwargs.pop("user_options", False)
    context['ngrequired'] = kwargs.pop('ngrequired', '')
    validators = json.loads(
        kwargs.pop("custom_validators", "{}")
    )
    context["custom_validators"] = []
    for k, v in validators.items():
        kebab = camelcase_to_underscore(k).replace("_", "-")
        context["custom_validators"].append((k, kebab, v,))
    return context
