from django import forms
from django.forms import ModelForm

from Sheriy_sanat.models import File_Talmeh
from .models import *


class FormFile(ModelForm):
    class Meta:
        model = File
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }


class FormWord(ModelForm):
    class Meta:
        model = File_Word
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }


class FormMeta(ModelForm):
    class Meta:
        model = File_Meta
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }


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


