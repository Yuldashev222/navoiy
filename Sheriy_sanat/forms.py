from django.forms import ModelForm
from django import forms

from Sheriy_sanat.models import File_Talmeh, File_Tazod, File_Tanosib, File_Tashbih


class FormTalmeh(ModelForm):
    class Meta:
        model = File_Talmeh
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }


class FormTazod(ModelForm):
    class Meta:
        model = File_Tazod
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }


class FormTanosib(ModelForm):
    class Meta:
        model = File_Tanosib
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }


class FormTashbih(ModelForm):
    class Meta:
        model = File_Tashbih
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }
