# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deriver', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='points',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PointsPlus.User'),
        ),
    ]