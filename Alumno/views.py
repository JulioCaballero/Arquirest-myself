
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from Alumno.models import Alumno
from Alumno.serializer import AlumnoSerializers
from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers


from datetime import datetime, timedelta, date
import time

class AlumnoList(APIView):
    # METODO GET PARA SOLICITAR INFO
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = Alumno.objects.all()
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)

    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id)
        except Alumno.DoesNotExist:
            return 404
        
    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            alumno = serializer.save()
            datas = serializer.data
            id_alumno = alumno.id
            x = datetime.now()
      
              
            a = str(x.year)
            m = str(x.month)
            d = str(x.day)
            fechaCompara = a + "-" + m + "-" + d

            asistencia=AsistenciaSerializers(data = {"id_alumno":id_alumno, "fecha":fechaCompara})
            if asistencia.is_valid():
                asistencia.save()
                datos = {"name":serializer.data['name'],"matricula":serializer.data['matricula'],"token":serializer.data['token'],"asistencia:":asistencia.data['fecha']}
            return Response(datos)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnoDetail(APIView):
    #Metodo get para solicitar info de un solo parametro
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    def get_object(self, token):
        try:
            return Alumno.objects.get(token=token)
        except Alumno.DoesNotExist:
            return 404

    def get(self, request, token, format=None):
        alumno = self.get_object(token)
        if alumno != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = AlumnoSerializers(alumno)
            alum = serializer.data['id']
            x = datetime.now()
            a = str(x.year)
            m = str(x.month)
            d = str(x.day)
            fechaCompara = a + "-" + m + "-" + d
            
            asistencia=AsistenciaSerializers(data = {"id_alumno":alum, "fecha":fechaCompara})
            if asistencia.is_valid():
                asistencia.save()
                datos = {"name":serializer.data['name'],"matricula":serializer.data['matricula'],"token":serializer.data['token'],"asistencia:":asistencia.data['fecha']}
            return Response(datos)
        else:
            return Response(alumno, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, token, format=None):
        alumno = self.get_object(token)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response(alumno, status = status.HTTP_404_BAD_REQUEST)

    def delete(self, request, token, format=None):
        alumno = self.get_object(token)
        if alumno != 404:
            alumno.delete()
            return Response(1)
        return Response(404)
# Create your views here.
