from django import forms
from .models import *


class CarRepairModelForm(forms.ModelForm):
    class Meta:
        model = CarRepairRequest
        fields = ['car_type', 'car_number', 'short_description']
        widgets = {
            'car_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نوع خودرو',
            }),
            'car_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'پلاک خودرو از چپ به راست',

            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'توضیح مختصر خرابی',
                'rows': 5,
                'id': 'message'
            })
        }

        labels = {
            'car_type': 'نوع خودرو',
            'car_number': 'پلاک خودرو از چپ به راست',
            'short_description': 'توضیح مختصر خرابی',
        }

        error_messages = {
            'car_type': {
                'required': 'وارد کردن نوع خودرو الزامیست'
            },
            'car_number': {
                'required': 'شماره پلاک الزامیست'
            },
        }
