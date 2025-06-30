from django.db import models
class TipoIngreso(models.Model):
    nombre=models.CharField(max_length=100)
class Estado(models.Model):
    estado=models.CharField(max_length=100)
class Ubicacion(models.Model):
    nombre=models.CharField(max_length=100)
class Responsable (models.Model):
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=8)
    celular=models.CharField(max_length=9)
class Equipos(models.Model):
    codigo_patrimonial=models.CharField(max_length=12)
    descripcion=models.CharField(max_length=100)
    numero_serie=models.CharField(max_length=10)
    marca=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)
    fecha_alta=models.DateField(auto_now_add=False)
    fecha_compra=models.DateField(auto_now_add=False)
    numero_o_c=models.CharField(max_length=100)
    numero_nea=models.CharField(max_length=100)
    centro_costos=models.CharField(max_length=100)
    tipo_ingreso=models.ForeignKey(
        TipoIngreso,related_name="equipos",on_delete=models.CASCADE
    )
    estado=models.ForeignKey(
        Estado,related_name="equipos",on_delete=models.CASCADE
    )
    ubicacion=models.ForeignKey(
        Ubicacion,related_name="equipos",on_delete=models.CASCADE
    )
    responsable=models.ForeignKey(
        Responsable,related_name="equipos",on_delete=models.CASCADE)
class EquiposMovimientos(models.Model):
    id_equipo=models.ForeignKey(
        Equipos, related_name="movimientos",on_delete=models.CASCADE
    )
    ubicacion=models.ForeignKey(
        Ubicacion,related_name="movimientos",on_delete=models.CASCADE
    )
    