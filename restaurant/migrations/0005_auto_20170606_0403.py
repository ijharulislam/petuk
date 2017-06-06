# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-06 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20170606_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='accepts_reservations',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='buffet',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='has_carryouts',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='has_kids_menu',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='has_wifi',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='outdoor_seating',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='party_room',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/restaurant'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/restaurant'),
        ),
    ]
