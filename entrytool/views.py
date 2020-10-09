from django.views.generic import TemplateView
from django.utils.translation import get_language


class AngularLocale(TemplateView):
    """
    Because we can't guarentee hospitals have white listed cdns
    and so that we can provide datepicker translations we generate
    the angular locale file on the fly with translations from
    the .po

    This is used by the datepicker

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