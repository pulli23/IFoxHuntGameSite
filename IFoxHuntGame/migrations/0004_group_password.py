# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFoxHuntGame', '0003_powerup_who'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='password',
            field=models.CharField(default='password', max_length=200, verbose_name='password'),
            preserve_default=False,
        ),
    ]
