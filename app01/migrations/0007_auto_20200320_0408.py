# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-20 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_node'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='repo',
            field=models.CharField(max_length=64, verbose_name='仓库地址'),
        ),
    ]