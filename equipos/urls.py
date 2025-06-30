from django.urls import path
from .views import ListEquiposApiView,DetailEquipos

urlpatterns = [
    path('equipos/', ListEquiposApiView.as_view()),
    path('equipos/<int:pk>',DetailEquipos.as_view())
]
