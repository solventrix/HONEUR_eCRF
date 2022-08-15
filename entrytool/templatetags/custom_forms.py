"""
Templatetags for form/modal helpers
"""
from django import template
from django.urls import reverse
from opal.templatetags import forms

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


@register.inclusion_tag('_helpers/custom_select.html')
def custom_select(*args, **kwargs):
    """
    A wrapper around the opal select that the option of
    including a link to the admin site to add a foreign key.

    To do this you pass in include_admin_link=True and user=request.user

    It only works for foreignkey or free text fields.
    """
    model, _ = forms._model_and_field_from_path(kwargs["field"])

    ctx = forms.select(*args, **kwargs)
    ctx['validator'] = kwargs.pop('validator', '')
    ctx["model_name"] = "editing.{}".format(model.get_api_name())
    ctx["include_admin_link"] = kwargs.get('include_admin_link')
    if ctx["include_admin_link"]:
        ctx["user"] = kwargs.get("user")
        if ctx["include_admin_link"] and not ctx["user"]:
            raise ValueError('To include admin links a user argument is required')
        _, field = forms._model_and_field_from_path(kwargs["field"])
        lookup_list = field.foreign_model
        app = lookup_list._meta.app_label
        ctx["admin_url"] = reverse(f"admin:{app}_{lookup_list.__name__.lower()}_changelist")
    return ctx


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


@register.inclusion_tag('_helpers/input.html')
def input(*args, **kwargs):
    context = forms.input(*args, **kwargs)
    context.update(honour_context(*args, **kwargs))
    return context
