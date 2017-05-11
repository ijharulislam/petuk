# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_available', models.BooleanField(default=False)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/restaurant/menu')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Item')),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
