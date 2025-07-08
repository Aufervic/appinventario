from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Equipos
from .serializers import EquiposSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from  .permissions import IsAsistente
class ListEquiposApiView(APIView):
    allowed_methods = ['GET', 'POST']
    permission_classes = [IsAuthenticatedOrReadOnly, IsAsistente]
    def get(self,request):
        equipos=Equipos.objects.all()
        serializer=EquiposSerializer(equipos,many=True)
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
    def get(self,request,pk):
        equipo=self.get_object(pk)
        if equipo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=EquiposSerializer(equipo)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        equipo=self.get_object(pk)
        if equipo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=EquiposSerializer(equipo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def delete(self,request,pk):
        equipo=self.get_object(pk)
        if equipo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Estado
from .serializers import EstadoSerializer

class ListEstadosApiView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()
    
'''

from rest_framework.decorators import api_view, permission_classes
from .models import Ubicacion

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly, IsAsistente])
def dashboard_summary(request):
    total_inventarios = -1
    total_equipos = Equipos.objects.count()
    total_oficinas = Ubicacion.objects.count()


    equipos_buenos = Equipos.objects.filter(estado__estado__iexact='Bueno').count()
    equipos_regulares = Equipos.objects.filter(estado__estado__iexact='Regular').count()
    equipos_malogrados = Equipos.objects.filter(estado__estado__iexact='Malogrado').count()

    return Response({
        "total_inventarios": total_inventarios,
        "total_equipos": total_equipos,
        "total_oficinas": total_oficinas,
        "equipos_buenos": equipos_buenos,
        "equipos_regulares": equipos_regulares,
        "equipos_malogrados": equipos_malogrados,
    })
