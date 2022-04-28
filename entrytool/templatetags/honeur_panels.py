from django import template
from django.db import models
from opal.templatetags import panels, forms

register = template.Library()


def is_date(field):
    return isinstance(field, (models.DateField, models.DateTimeField,))


def is_boolean(field):
    return isinstance(field, (models.BooleanField, models.NullBooleanField,))


@register.inclusion_tag('_helpers/record_panel.html', takes_context=True)
def record_panel(
    context,
    model,
    **kwargs
):
    ctx = panels.record_panel(context, model, **kwargs)
    ctx["model"] = model
    return ctx


@register.inclusion_tag('_helpers/field_display.html', takes_context=True)
def field_display(context, model_field):
    _, field_name = model_field.split('.')
    model, field = forms._model_and_field_from_path(model_field)
    ctx = {}
    ctx["label"] = model._get_field_title(field_name)
    ctx["field_name"] = field_name
    ctx["is_date"] = is_date(field)
    return ctx
