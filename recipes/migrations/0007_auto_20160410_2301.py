# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20160410_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipestep',
            old_name='description',
            new_name='instruction',
        ),
    ]