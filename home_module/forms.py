from django import forms
from accounts.models import *


class CarDeliverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'car_type', 'car_number', 'first_name', 'last_name', 'mobile', 'email', 'deliver_date',
            'costs_primary', 'costs_secondary', 'short_description',
        ]

        widgets = {
            'car_type': forms.ChoiceField(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'car_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'class': 'form-control',
                'maxlength': 11,
                'minlength': 11
            }),
            'deliver_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'costs_primary': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'costs_secondary': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            })
        }
