# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-07 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0012_plugininstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugininstance',
            name='status',
            field=models.CharField(default='started', max_length=30),
        ),
    ]
