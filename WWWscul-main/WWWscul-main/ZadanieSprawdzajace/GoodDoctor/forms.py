from django import forms
from .models import Wizyta

class WizytaForm(forms.ModelForm):
    class Meta:
        model = Wizyta
        fields = ["date", "pacjent", "powod", "uwagi"]
