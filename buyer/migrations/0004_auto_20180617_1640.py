# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_remove_buyer_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer_profile',
            name='bio',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='buyer_profile',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='buyer_profile',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyer_profile',
            name='profile_pic',
            field=models.ImageField(default=1, upload_to='Buyer_profiles'),
            preserve_default=False,
        ),
    ]
