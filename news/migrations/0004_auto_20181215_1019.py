# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-15 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20181215_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='advisory_feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, choices=[(b'goog', b'Google News Feed'), (b'twitter', b'Twitter'), (b'', b'')], default='', max_length=255, null=True)),
                ('feed', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Advisory Feeds',
            },
        ),
        migrations.CreateModel(
            name='advisory_keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, choices=[(b'goog', b'Google News Feed'), (b'twitter', b'Twitter'), (b'', b'')], default='', max_length=255, null=True)),
                ('keyword', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Advisory Keywords',
            },
        ),
        migrations.CreateModel(
            name='alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, choices=[(b'goog', b'Google News Feed'), (b'twitter', b'Twitter'), (b'', b'')], default='', max_length=255, null=True)),
                ('sourceId', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[(b'info', b'Informational'), (b'boil', b'Boil Water'), (b'notdrink', b'Do Not Drink'), (b'notuse', b'Do Not Use'), (b'unknown', b'Unknown'), (b'safe', b'Safe')], default='safe', max_length=255, null=True)),
                ('ignore', models.BooleanField(default=True)),
                ('text', models.TextField(blank=True, default='', null=True)),
                ('text_wo_stopwords', models.TextField(blank=True, default='', null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='county_served',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='location',
        ),
        migrations.AlterModelOptions(
            name='utility',
            options={'verbose_name_plural': 'Utilities'},
        ),
        migrations.RemoveField(
            model_name='url',
            name='links',
        ),
        migrations.RemoveField(
            model_name='url',
            name='tweet',
        ),
        migrations.AddField(
            model_name='location',
            name='fips_county',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='fips_state',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='link',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='city',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='fips_county',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='fips_state',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='people_served',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='utility',
            name='state',
            field=localflavor.us.models.USStateField(blank=True, choices=[(b'AL', 'Alabama'), (b'AK', 'Alaska'), (b'AS', 'American Samoa'), (b'AZ', 'Arizona'), (b'AR', 'Arkansas'), (b'AA', 'Armed Forces Americas'), (b'AE', 'Armed Forces Europe'), (b'AP', 'Armed Forces Pacific'), (b'CA', 'California'), (b'CO', 'Colorado'), (b'CT', 'Connecticut'), (b'DE', 'Delaware'), (b'DC', 'District of Columbia'), (b'FL', 'Florida'), (b'GA', 'Georgia'), (b'GU', 'Guam'), (b'HI', 'Hawaii'), (b'ID', 'Idaho'), (b'IL', 'Illinois'), (b'IN', 'Indiana'), (b'IA', 'Iowa'), (b'KS', 'Kansas'), (b'KY', 'Kentucky'), (b'LA', 'Louisiana'), (b'ME', 'Maine'), (b'MD', 'Maryland'), (b'MA', 'Massachusetts'), (b'MI', 'Michigan'), (b'MN', 'Minnesota'), (b'MS', 'Mississippi'), (b'MO', 'Missouri'), (b'MT', 'Montana'), (b'NE', 'Nebraska'), (b'NV', 'Nevada'), (b'NH', 'New Hampshire'), (b'NJ', 'New Jersey'), (b'NM', 'New Mexico'), (b'NY', 'New York'), (b'NC', 'North Carolina'), (b'ND', 'North Dakota'), (b'MP', 'Northern Mariana Islands'), (b'OH', 'Ohio'), (b'OK', 'Oklahoma'), (b'OR', 'Oregon'), (b'PA', 'Pennsylvania'), (b'PR', 'Puerto Rico'), (b'RI', 'Rhode Island'), (b'SC', 'South Carolina'), (b'SD', 'South Dakota'), (b'TN', 'Tennessee'), (b'TX', 'Texas'), (b'UT', 'Utah'), (b'VT', 'Vermont'), (b'VI', 'Virgin Islands'), (b'VA', 'Virginia'), (b'WA', 'Washington'), (b'WV', 'West Virginia'), (b'WI', 'Wisconsin'), (b'WY', 'Wyoming')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='zipcode',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='tweet',
        ),
        migrations.AddField(
            model_name='county_served',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.location'),
        ),
        migrations.AddField(
            model_name='county_served',
            name='utility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.utility'),
        ),
        migrations.AddField(
            model_name='alert',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.location'),
        ),
        migrations.AddField(
            model_name='url',
            name='alert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.alert'),
        ),
    ]
