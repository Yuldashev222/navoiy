from django.db import models


# Create your models here.

class arxaizm(models.Model):
    soz = models.CharField(max_length=200)
    mano = models.CharField(max_length=200)

    def __str__(self):
        return self.soz


class istorizm(models.Model):
    soz = models.CharField(max_length=200)
    mano = models.CharField(max_length=200)

    def __str__(self):
        return self.soz


class File_Arxaizm(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name