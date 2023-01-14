from django.db import models

# Create your models here.
from django.db.models import CASCADE

from Gazal.models import Auditoriya_yoshi


class Devon(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name


class Janrlar(models.Model):
    devon_id = models.ForeignKey(Devon, on_delete=CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ChistonJavob(models.Model):
    javob = models.CharField(max_length=200)

    def __str__(self):
        return self.javob


class JanrMisra(models.Model):
    janr_number = models.PositiveSmallIntegerField(null=True)
    janr = models.ForeignKey(Janrlar, on_delete=CASCADE)
    misra = models.CharField(max_length=300)
    chiston_javobi = models.ForeignKey(ChistonJavob, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.misra

    class Meta:
        verbose_name = 'Janr misrasi'
        verbose_name_plural = 'Janr misralari'


class JanrMisraSoz(models.Model):
    janr = models.ForeignKey(Janrlar, on_delete=CASCADE)
    janr_number = models.PositiveSmallIntegerField(null=True)
    soz = models.CharField(max_length=150)
    mano = models.CharField(max_length=400, null=True)
    auditoriya_yoshi = models.ForeignKey(Auditoriya_yoshi, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name = 'Janr sozi'
        verbose_name_plural = 'Janr sozlari'

# class Janr_meta(models.Model):
#     janr = models.ForeignKey(Janrlar, on_delete=CASCADE)
#     janr_number = models.IntegerField(null=True)
