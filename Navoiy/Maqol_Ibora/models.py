from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class Maqol(models.Model):
    misra = RichTextField(blank=True)
    maqol = models.CharField(max_length=300)

    def __str__(self):
        return self.misra


class Ibora(models.Model):
    bayt = RichTextField(blank=True)
    ibora = models.CharField(max_length=300)

    def __str__(self):
        return self.bayt
