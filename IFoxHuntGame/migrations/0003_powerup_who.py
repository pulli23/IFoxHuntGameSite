# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFoxHuntGame', '0002_auto_20151204_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerup',
            name='who',
            field=models.IntegerField(default=0),
        ),
    ]
