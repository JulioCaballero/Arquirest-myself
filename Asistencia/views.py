from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers
from Alumno.models import Alumno

class AsistenciaDetail(APIView):
    
    def get_object(self, fecha):
        try:
            return Asistencia.objects.get(fecha=fecha)
        except Asistencia.DoesNotExist:
            return 404

    def get(self, request, fecha, format=None):
        asistencia = self.get_object(fecha)
        if asistencia != 404:
            serializer = AsistenciaSerializers(asistencia)
            return Response(serializer.data)
        else:
            return Response(asistencia, status = status.HTTP_400_BAD_REQUEST)

class AsistenciaList(APIView):
    def post(self, request, format=None):
        serializer = AsistenciaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        queryset = Asistencia.objects.all()
        serializer = AsistenciaSerializers(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
