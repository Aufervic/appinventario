from rest_framework import serializers
from .models import (
    Equipos,
    Estado,
    TipoIngreso,
    EquiposMovimientos,
    Ubicacion,
    Responsable,
)

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

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'


class EquipoSerializerDinamico(serializers.ModelSerializer):
    class Meta:
        model = Equipos
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        expand = context.get('expand', [])

        super().__init__(*args, **kwargs)

        if 'estado' in expand:
            self.fields['estado'] = EstadoSerializer()
        if 'ubicacion' in expand:
            self.fields['ubicacion'] = UbicacionSerializer()
        if 'responsable' in expand:
            self.fields['responsable'] = ResponsableSerializer()
        if 'tipo_ingreso' in expand:
            self.fields['tipo_ingreso'] = TipoIngresoSerializer()



class MovimientoSerializerDinamico(serializers.ModelSerializer):
    class Meta:
        model = EquiposMovimientos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        expand = context.get('expand', [])

        super().__init__(*args, **kwargs)
        if 'equipo' in expand:
            self.fields['id_equipo'] = EquiposSerializer()
        if 'ubicacion' in expand:
            self.fields['ubicacion'] = UbicacionSerializer()
