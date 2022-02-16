from opal.core import lookuplists
from django.utils.translation import gettext_lazy as _


class CLLRegimenList(lookuplists.LookupList):
    class Meta:
        verbose_name = _("CLL Regimen List")
        verbose_name_plural = _("CLL Regimen List")


class CLLStopReason(lookuplists.LookupList):
    class Meta:
        verbose_name = _("CLL Stop Reason List")
        verbose_name_plural = _("CLL Stop Reason List")
