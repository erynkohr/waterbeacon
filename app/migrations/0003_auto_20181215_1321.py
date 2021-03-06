# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-15 13:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='county',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='fips_county',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='fips_state',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='state',
            field=localflavor.us.models.USStateField(blank=True, choices=[(b'AL', 'Alabama'), (b'AK', 'Alaska'), (b'AS', 'American Samoa'), (b'AZ', 'Arizona'), (b'AR', 'Arkansas'), (b'AA', 'Armed Forces Americas'), (b'AE', 'Armed Forces Europe'), (b'AP', 'Armed Forces Pacific'), (b'CA', 'California'), (b'CO', 'Colorado'), (b'CT', 'Connecticut'), (b'DE', 'Delaware'), (b'DC', 'District of Columbia'), (b'FL', 'Florida'), (b'GA', 'Georgia'), (b'GU', 'Guam'), (b'HI', 'Hawaii'), (b'ID', 'Idaho'), (b'IL', 'Illinois'), (b'IN', 'Indiana'), (b'IA', 'Iowa'), (b'KS', 'Kansas'), (b'KY', 'Kentucky'), (b'LA', 'Louisiana'), (b'ME', 'Maine'), (b'MD', 'Maryland'), (b'MA', 'Massachusetts'), (b'MI', 'Michigan'), (b'MN', 'Minnesota'), (b'MS', 'Mississippi'), (b'MO', 'Missouri'), (b'MT', 'Montana'), (b'NE', 'Nebraska'), (b'NV', 'Nevada'), (b'NH', 'New Hampshire'), (b'NJ', 'New Jersey'), (b'NM', 'New Mexico'), (b'NY', 'New York'), (b'NC', 'North Carolina'), (b'ND', 'North Dakota'), (b'MP', 'Northern Mariana Islands'), (b'OH', 'Ohio'), (b'OK', 'Oklahoma'), (b'OR', 'Oregon'), (b'PA', 'Pennsylvania'), (b'PR', 'Puerto Rico'), (b'RI', 'Rhode Island'), (b'SC', 'South Carolina'), (b'SD', 'South Dakota'), (b'TN', 'Tennessee'), (b'TX', 'Texas'), (b'UT', 'Utah'), (b'VT', 'Vermont'), (b'VI', 'Virgin Islands'), (b'VA', 'Virginia'), (b'WA', 'Washington'), (b'WV', 'West Virginia'), (b'WI', 'Wisconsin'), (b'WY', 'Wyoming')], max_length=2, null=True),
        ),
    ]
