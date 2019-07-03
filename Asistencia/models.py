from django.db import models
from django.conf import settings
from Alumno.models import Alumno
from django.utils import timezone

# Create your models here.
class Asistencia(models.Model):
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Asistencia'