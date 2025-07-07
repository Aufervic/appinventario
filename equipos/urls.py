from django.urls import path
from .views import ListEquiposApiView,DetailEquipos

from rest_framework.routers import DefaultRouter
from .viewsets import (
    EstadoViewSet,
    TipoIngresoViewSet,
    UbicacionViewSet,
    MovimientoViewSet,
    ResponsableViewSet,
)

router = DefaultRouter()
router.register('estados', EstadoViewSet)
router.register('tipo-ingresos', TipoIngresoViewSet)
router.register('ubicaciones', UbicacionViewSet)
router.register('movimientos', MovimientoViewSet)
router.register('responsables', ResponsableViewSet)

urlpatterns = [
    path('equipos/', ListEquiposApiView.as_view()),
    path('equipos/<int:pk>',DetailEquipos.as_view())
] + router.urls
