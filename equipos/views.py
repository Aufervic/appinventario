from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Equipos
from .serializers import EquiposSerializer, EquiposDetailSerializer
class ListEquiposApiView(APIView):
    allowed_methods = ['GET', 'POST']
    def get(self,request):
        equipos=Equipos.objects.select_related('tipo_ingreso', 'estado', 'ubicacion').all()
        serializer=EquiposDetailSerializer(equipos,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EquiposSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
class DetailEquipos(APIView):
    def get_object(self,pk):
        try:
            return Equipos.objects.get(id=pk)
        except Equipos.DoesNotExist:
            return None
        
    def get_objectDetail(self,pk):
        try:
            return Equipos.objects.select_related('tipo_ingreso', 'estado', 'ubicacion').get(id=pk)
        except Equipos.DoesNotExist:
            return None
        
    def get(self,request,pk):
        equipo=self.get_object(pk)
        print(equipo.estado)
        if equipo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=EquiposDetailSerializer(equipo)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        equipo=self.get_object(pk)
        if equipo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=EquiposSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def delete(self,request,pk):
        equipo=self.get_object(pk)
        if equipo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Temp ::::::::::::::::::::::::::::::::::::::::::::
from .models import TipoIngreso
from .serializers import TipoIngresoSerializer

class ListTipoIngresoApiView(APIView):
    allowed_methods = ['GET']

    def get(self, request):
        tipo_ingreso = TipoIngreso.objects.all()
        serializer = TipoIngresoSerializer(tipo_ingreso, many=True)
        return Response(serializer.data)


from .models import Estado
from .serializers import EstadoSerializer

class ListEstadosApiView(APIView):
    allowed_methods = ['GET']

    def get(self, request):
        estados = Estado.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return Response(serializer.data)
    


from .models import Ubicacion
from .serializers import UbicacionSerializer

class ListUbicacionesApiView(APIView):
    allowed_methods = ['GET']

    def get(self, request):
        ubicaciones = Ubicacion.objects.all()
        serializer = UbicacionSerializer(ubicaciones, many=True)
        return Response(serializer.data)