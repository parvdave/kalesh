from django import forms
from .models import Kalesh, Kaleshi

class KaleshForm(forms.ModelForm):
    class Meta:
        model = Kalesh
        fields = ['email_1', 'email_2']
        widgets = {
            'email_1': forms.EmailInput(
                attrs={'class': 'form-control',
                        'placeholder': 'Enter first Kaleshi\'s email address'}),
            'email_2': forms.EmailInput(
                attrs={'class': 'form-control',
                        'placeholder': 'Enter second Kaleshi\'s email address'}),
        }

class KaleshiResponseForm(forms.ModelForm):
    class Meta:
        model = Kaleshi
        fields = ['kaleshi_response']
        widgets = {
            'kaleshi_response': 
            forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Make sure you don\'t hold back!',
                    'rows': 5,
                    'cols': 20
                    }
                )
        }
