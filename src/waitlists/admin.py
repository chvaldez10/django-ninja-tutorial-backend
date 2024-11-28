from django.contrib import admin
from .models import WaitlistEntry

class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "timestamp", "updated"]
    search_fields = ["email"]

admin.site.register(WaitlistEntry, WaitlistEntryAdmin)