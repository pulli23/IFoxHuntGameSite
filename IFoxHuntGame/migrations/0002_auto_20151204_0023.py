# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFoxHuntGame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PU_id', models.PositiveIntegerField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('altitude', models.FloatField(default=0)),
                ('PU_time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='hunter',
            field=models.BooleanField(default=True),
        ),
    ]
