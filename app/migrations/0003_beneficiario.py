# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160409_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.IntegerField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('estrato', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], max_length=2)),
                ('escolaridad', models.CharField(choices=[('Pr', 'Primaria'), ('Sc', 'Secundaria'), ('Te', 'Tecnico'), ('Tl', 'Tecnolgo'), ('Pr', 'Profesional'), ('NR', 'No registra')], max_length=2)),
                ('ocupacion', models.CharField(max_length=50)),
                ('parentesco', models.CharField(max_length=50)),
                ('cabeza', models.IntegerField(max_length=13)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ciudad')),
            ],
        ),
    ]
