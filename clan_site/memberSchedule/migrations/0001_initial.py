# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic', '0019_auto_20160708_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.Member')),
            ],
        ),
    ]
