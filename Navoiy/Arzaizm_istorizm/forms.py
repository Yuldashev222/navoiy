from django.forms import ModelForm
from django import forms

from Arzaizm_istorizm.models import File_Arxaizm


class FormArxaizm(ModelForm):
    class Meta:
        model = File_Arxaizm
        fields = ['files']

        widgets = {
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose file'
            }),
        }
