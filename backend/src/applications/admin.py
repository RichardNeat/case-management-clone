from django.contrib import admin

# Register your models here.

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("applicant_name", "country_of_origin", "status", "submission_date")
