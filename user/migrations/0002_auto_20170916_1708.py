# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.CharField(max_length=5),
        ),
    ]
