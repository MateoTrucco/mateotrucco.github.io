# En tu archivo forms.py
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'required_age', 'contact_number']
