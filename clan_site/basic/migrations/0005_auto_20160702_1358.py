# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20160630_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terittorybattle',
            name='planet',
            field=models.CharField(choices=[('S', 'Syra'), ('T', 'Terra')], max_length=1),
        ),
    ]
