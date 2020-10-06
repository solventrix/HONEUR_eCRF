from django import template
from opal.templatetags import panels

register = template.Library()


@register.inclusion_tag('_helpers/record_panel.html', takes_context=True)
def record_panel(
    context,
    model,
    **kwargs
):
    ctx = panels.record_panel(context, model, **kwargs)
    ctx["model"] = model
    return ctx