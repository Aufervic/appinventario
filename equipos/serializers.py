from rest_framework import serializers
from .models import Equipos,Estado,TipoIngreso,EquiposMovimientos

class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipos
        fields = '__all__'
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estado
        fields = '__all__'
class TipoIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoIngreso
        fields = '__all__'
class EquiposMovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquiposMovimientos
        fields = '__all__'

