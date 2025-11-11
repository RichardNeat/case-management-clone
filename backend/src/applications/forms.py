from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["applicant_name", "country_of_origin", "supporting_document"]