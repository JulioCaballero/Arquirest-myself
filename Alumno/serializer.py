# -------------AGREGANDO LIBRERIAS FRAMEWORK-----------
from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from alumno.models import Alumno

class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__')

