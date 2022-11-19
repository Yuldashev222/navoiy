from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Matn_tipi(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Auditoriya_yoshi(models.Model):
    yosh = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.yosh


class Gazal(models.Model):
    number = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    matn_tipi = models.ForeignKey(Matn_tipi, on_delete=models.CASCADE, null=True)
    auditoriya_yoshi = models.ForeignKey(Auditoriya_yoshi, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Misra(models.Model):
    gazal_id = models.ForeignKey(Gazal, on_delete=CASCADE, related_name='misralar')
    misra = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.gazal_id.number}: {self.misra[:10]}...'

    class Meta:
        verbose_name = 'Misra'
        verbose_name_plural = 'Misralar'


class Soz(models.Model):
    soz_id = models.ForeignKey(Gazal, verbose_name='Gazal', blank=True, on_delete=models.CASCADE)
    soz = models.CharField(max_length=200, blank=True, db_index=True)
    mano = models.CharField(max_length=100, blank=True)
    janr = models.CharField(max_length=100, default='g`azal')
    satr = models.ForeignKey(Misra, on_delete=CASCADE)
    tip = models.ForeignKey(Matn_tipi, on_delete=CASCADE)
    yosh = models.ForeignKey(Auditoriya_yoshi, on_delete=CASCADE)

    def __str__(self):
        return self.soz


    class Meta:
        verbose_name = 'Soz'
        verbose_name_plural = 'Sozlar'

class File(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name


class File_Word(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name


class File_Meta(models.Model):
    name = models.CharField(max_length=100, default="")
    files = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name
