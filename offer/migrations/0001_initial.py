# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0003_auto_20170517_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validity', models.DateField()),
                ('gist', models.TextField()),
                ('price', models.FloatField(default=0.0)),
                ('discount', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_offers', to='restaurant.Item')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='restaurant.Restaurant')),
            ],
        ),
    ]