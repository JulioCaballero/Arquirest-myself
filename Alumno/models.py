from django.db import models
from django.conf import settings

class Alumno(models.Model):    
    name = models.CharField(max_length=254, null=False)
    lastName = models.CharField(max_length=254, null=False)
    matricula = models.CharField(max_length=254, null=False)
    career = models.CharField(max_length=254, null=False)
    token = models.CharField(max_length=254, null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Alumno'


