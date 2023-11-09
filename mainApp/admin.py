from django.contrib import admin
from .models import *


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "details", "date", "status"]
    list_display_links = ["id", "title"]
    list_filter = ["status", "date"]
    search_fields = ["title"]
