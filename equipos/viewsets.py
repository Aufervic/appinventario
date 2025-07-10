from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
    EquipoSerializerDinamico,
    EstadoSerializer,
    TipoIngresoSerializer,
    UbicacionSerializer,
    ResponsableSerializer,
    MovimientoSerializerDinamico,
)

from .models import (
    Equipos,
    Estado,
    TipoIngreso,
    Ubicacion,
    EquiposMovimientos,  # OJO: podria renombrarse simplemente a Movimientos
    Responsable,
)
from .permissions import IsAsistente


class EquipoViewSet(viewsets.ModelViewSet):
    # Corregido para trabajar con serializador dinamico
    queryset = Equipos.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAsistente]

    def get_serializer_class(self):
        # Siempre usas el serializer dinámico
        return EquipoSerializerDinamico

    def get_serializer_context(self):
        context = super().get_serializer_context()
        expand = self.request.query_params.get("expand")
        if expand:
            # Separa por coma y guarda como lista en el contexto
            context["expand"] = [e.strip() for e in expand.split(",")]
        return context


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
    # Adaptado para trabajar con serializador dinamico
    queryset = EquiposMovimientos.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAsistente]

    def get_serializer_class(self):
        return MovimientoSerializerDinamico

    def get_serializer_context(self):
        context = super().get_serializer_context()
        expand = self.request.query_params.get("expand")
        if expand:
            context["expand"] = [e.strip() for e in expand.split(",")]
        return context


class ResponsableViewSet(viewsets.ModelViewSet):
    serializer_class = ResponsableSerializer
    queryset = Responsable.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAsistente]
