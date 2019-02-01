# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-16 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20181215_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='status',
            field=models.CharField(blank=True, choices=[(b'info', b'Informational'), (b'boil', b'Boil Water'), (b'notdrink', b'Do Not Drink'), (b'notuse', b'Do Not Use'), (b'unknown', b'Unknown'), (b'safe', b'Safe')], default='safe', max_length=255, null=True),
        ),
    ]