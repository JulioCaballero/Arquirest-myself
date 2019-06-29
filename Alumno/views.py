
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Alumno.models import Alumno
from Alumno.serializer import AlumnoSerializers

class AlumnoList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete = False)
        serializer = AlumnoSerializers(queryset)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnoDetail(APIView):
    #Metodo get para solicitar info de un solo parametro
    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id, delete = False)
        except Alumno.DoesNotExist:
            return 404

    def get(self, id, request, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = AlumnoSerializers(alumno)
            return Response(serializer.data)
        else:
            return Response(alumno)

    def put(self, request, id, format=None):
        alumno = self.get_object(id)
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


# Create your views here.
