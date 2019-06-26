from django.db import models
from django.conf import settings

# Create your models here.

class Alumnos(models.Model):
    name = models.CharField(max_length=254, null=False)
    lastName = models.CharField(max_length=254, null=False)
    matricula = models.CharField(max_length=254, null=False)
    career = models.CharField(max_length=254, null=False)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Alumnos'

class Rfid(models.Model):
    token = models.IntegerField(null=False)
    id_alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Rfid'

