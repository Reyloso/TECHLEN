# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 01:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prestamos', '0011_auto_20180618_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidente',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
