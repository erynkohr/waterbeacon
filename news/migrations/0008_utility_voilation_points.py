# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-01 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_location_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='voilation_points',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
