from django.urls import path
from .views import ListEquiposApiView,DetailEquipos

from .views import ListTipoIngresoApiView, ListEstadosApiView, ListUbicacionesApiView


urlpatterns = [
    path('equipos/', ListEquiposApiView.as_view()),
    path('equipos/<int:pk>',DetailEquipos.as_view()),

    path('tipoingreso/', ListTipoIngresoApiView.as_view()),
    path('estados/', ListEstadosApiView.as_view()),
    path('ubicaciones/', ListUbicacionesApiView.as_view()),
]
