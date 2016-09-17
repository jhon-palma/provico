# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160502_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiario',
            old_name='cedula',
            new_name='numeroDocumento',
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='tipoDocumento',
            field=models.CharField(choices=[('RC', 'RC'), ('TI', 'TI'), ('CC', 'CC'), ('CE', 'CE')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
