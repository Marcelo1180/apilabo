# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 21:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xapitest', '0002_archivosauditlogentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivos',
            options={'permissions': (('view_archivos', 'Puede ver los registros'), ('options_archivos', 'Puede ver los options'))},
        ),
    ]