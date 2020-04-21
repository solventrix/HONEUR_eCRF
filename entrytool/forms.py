import json
from django import template
from django.db import models
from opal.core.subrecords import get_subrecord_from_model_name
from opal.core import fields
from opal.core.serialization import OpalSerializer
from opal.templatetags.froms import _input

# register = template.Library()

# @register.inclusion_tag('_helpers/input.html')
# def input(*args, **kwargs):
#     """
#     Render a text input

#     Kwargs:
#     - hide : Condition to hide
#     - show : Condition to show
#     - model: Angular model
#     - label: User visible label
#     - lookuplist: Name of the lookuplist
#     - required: label to show when we're required!
#     """
#     ctx =  _input(*args, **kwargs)
#     ctx['pattern'] = kwargs.pop('pattern', '')

#     return ctx
