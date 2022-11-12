from django.db import models


# Create your models here.


class Asar(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.name
