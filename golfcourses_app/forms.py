from django import forms 
from .models import GolfSnacks

class GolfSnacksForm(forms.ModelForm):
    class Meta:
        model = GolfSnacks
        fields = ['date', 'snacks']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }