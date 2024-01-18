from django import forms
from .models import InformationOverdue, Example




class InfoForm(forms.Form):
    class Meta:
        model = Example
        fields = '__all__'