from django.db import models
from django.conf import settings
from Alumno.models import Alumno

# Create your models here.
class Asistencia(models.Model):
    id_alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Asistencia'