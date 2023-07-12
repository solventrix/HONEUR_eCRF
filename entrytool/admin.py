from django.contrib.admin.models import LogEntry
from django.contrib import admin
import random
from plugins.conditions.mm.models import Immunofixation
from plugins.conditions.mm.models import ClinicalPresentation 


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"

    list_filter = ["user", "content_type", "action_flag"]

    search_fields = ["object_repr", "change_message"]

    list_display = [
        "action_time",
        "user",
        "content_type",
        "action_flag",
        "change_message",
    ]

def set_token(modeladmin, request, queryset):
    queryset.update(consistency_token=random.randint(0,10000))
set_token.short_description = "Set consistency_token"


class ImmunofixationAdmin(admin.ModelAdmin):
    actions = [set_token]

class ClinicalPresentationAdmin(admin.ModelAdmin):
    actions = [set_token]    

admin.site.unregister(Immunofixation)
admin.site.unregister(ClinicalPresentation)
admin.site.register(ClinicalPresentation, ClinicalPresentationAdmin)
admin.site.register(Immunofixation, ImmunofixationAdmin)

