# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0009_auto_20160702_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terittorybattle',
            name='hypothesis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Hypothesis'),
        ),
    ]