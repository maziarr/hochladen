# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='upload1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded_at1',
            field=models.DateTimeField(auto_now=True),
        ),
    ]