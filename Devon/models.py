from django.db import models

# Create your models here.
from django.db.models import CASCADE


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
