from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
    EstadoSerializer,
    TipoIngresoSerializer,
    UbicacionSerializer,
    EquiposMovimientosSerializer,
    ResponsableSerializer,
)

from .models import (
    Estado,
    TipoIngreso,
    Ubicacion,
    EquiposMovimientos, # OJO: podria renombrarse simplemente a Movimientos
    Responsable,
)
from .permissions import IsAsistente


class EstadoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAsistente]

    # métodos extra


class TipoIngresoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoIngresoSerializer
    queryset = TipoIngreso.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAsistente]


class UbicacionViewSet(viewsets.ModelViewSet):
    serializer_class = UbicacionSerializer
    queryset = Ubicacion.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAsistente]


class MovimientoViewSet(viewsets.ModelViewSet):
    serializer_class: EquiposMovimientosSerializer
    queryset = EquiposMovimientos.objects.all()
    permission_classes = [ IsAuthenticatedOrReadOnly, IsAsistente]


class ResponsableViewSet(viewsets.ModelViewSet):
    serializer_class = ResponsableSerializer
    queryset = Responsable.objects.all()
    permission_classes = [ IsAuthenticatedOrReadOnly, IsAsistente]

