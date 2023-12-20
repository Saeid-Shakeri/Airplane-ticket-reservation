from django import forms
from .models import Flight


class SearchFrom(forms.ModelForm):
    
    class Meta:
        model = Flight
        fields = ["way", "date"]

