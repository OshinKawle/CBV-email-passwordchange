from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        widgets = {
            'company': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Company Name'
                }
            ),
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Model Name'
                }
            ),
            'ram': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Ram of Laptop'
                }
            ),
            'rom': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Rom of Laptop'
                }
            ),
            'processor': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Processor'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Price Of Laptop'
                }
            ),
            'weight': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Weight of Laptop'
                }
            )
        }


