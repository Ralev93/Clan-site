# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0010_auto_20160702_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terittorybattle',
            name='hypothesis',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Hypothesis'),
        ),
    ]