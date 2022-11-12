from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

class View_number(models.Model):
    number = models.IntegerField(default=0)


class Maqola(models.Model):
    name = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='files')

    def __str__(self):
        return self.name


class Tarjimayi_hol(models.Model):
    date = RichTextField(blank=True)

    def __str__(self):
        return self.date
