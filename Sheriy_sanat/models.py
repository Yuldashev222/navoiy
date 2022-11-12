from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class Talmeh(models.Model):
    bayt = RichTextField(blank=True)
    mano = models.CharField(max_length=100)

    def __str__(self):
        return self.bayt


class Tazod(models.Model):
    bayt = RichTextField(blank=True)
    mano = models.CharField(max_length=200)

    def __str__(self):
        return self.bayt


class Tanosib(models.Model):
    bayt = RichTextField(blank=True)
    mano = models.CharField(max_length=300)

    def __str__(self):
        return self.bayt


class Tashbeh(models.Model):
    bayt = RichTextField(blank=True)
    oxshamish = models.CharField(max_length=300, blank=True)
    oxshatilmish = models.CharField(max_length=300, blank=True)
    sabab = models.CharField(max_length=300, blank=True)
    vosita = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.bayt


class File_Talmeh(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name


class File_Tazod(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name


class File_Tanosib(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name


class File_Tashbih(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name
