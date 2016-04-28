# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_beneficiario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiario',
            name='cedula',
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='genero',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='nace',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='cabeza',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='escolaridad',
            field=models.CharField(choices=[('Pr', 'Primaria'), ('Sc', 'Secundaria'), ('Te', 'Tecnico'), ('Tl', 'Tecnologo'), ('Pr', 'Profesional'), ('NR', 'No registra')], max_length=2),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='estrato',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]