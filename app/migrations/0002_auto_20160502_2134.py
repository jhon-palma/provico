# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='codigo',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='codigo',
            field=models.CharField(max_length=2),
        ),
    ]
