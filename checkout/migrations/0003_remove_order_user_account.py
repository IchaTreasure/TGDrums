# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-27 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_user_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_account',
        ),
    ]