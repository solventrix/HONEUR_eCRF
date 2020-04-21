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
    context["user_options"] = kwargs.pop("user_options", False)
    context['ngrequired'] = kwargs.pop('ngrequired', '')
    return context



