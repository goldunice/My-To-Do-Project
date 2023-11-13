from django.contrib import admin
from .models import *


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "details", "date", "status", "egasi"]
    list_display_links = ["id", "title"]
    list_filter = ["status", "date", "egasi"]
    search_fields = ["title"]
