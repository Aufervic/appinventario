from rest_framework import serializers
from .models import Equipos,Estado, Ubicacion, TipoIngreso,EquiposMovimientos



class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estado
        fields = '__all__'

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ubicacion
        fields = '__all__'

class TipoIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoIngreso
        fields = '__all__'
class EquiposMovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquiposMovimientos
        fields = '__all__'

class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipos
        fields = '__all__'

class EquiposDetailSerializer(serializers.ModelSerializer):
    tipo_ingreso = TipoIngresoSerializer()
    estado = EstadoSerializer()
    ubicacion = UbicacionSerializer()

    class Meta:
        model=Equipos
        fields = '__all__'