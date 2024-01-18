from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import InformationOverdue



@admin.register(InformationOverdue)
class InfoAdmin(ImportExportModelAdmin):
    list_display = ("MFO", "Unique", "NameClient", "Type", "Sum",
                     "StatusWork", "StatusTurnover")



