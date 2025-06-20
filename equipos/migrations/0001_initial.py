# Generated by Django 5.2.1 on 2025-05-29 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_patrimonial', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('fecha_alta', models.DateField()),
                ('fecha_compra', models.DateField()),
                ('numero_o_c', models.CharField(max_length=100)),
                ('numero_nea', models.CharField(max_length=100)),
                ('centro_costos', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estado_id', to='equipos.estado')),
                ('tipo_ingreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_ingreso_id', to='equipos.tipoingreso')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion_id', to='equipos.ubicacion')),
            ],
        ),
    ]
