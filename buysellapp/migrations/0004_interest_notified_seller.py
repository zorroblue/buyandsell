# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buysellapp', '0003_auto_20170324_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='notified_seller',
            field=models.BooleanField(default=False),
        ),
    ]