# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-01 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_in_feet', models.IntegerField()),
                ('distance_achievement_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('-distance_in_feet',),
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('manufacturing_date', models.DateTimeField()),
                ('has_it_competed', models.BooleanField(default=False)),
                ('inserted_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DroneCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('races_count', models.IntegerField()),
                ('inserted_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='drone',
            name='drone_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drones', to='drones.DroneCategory'),
        ),
        migrations.AddField(
            model_name='competition',
            name='drone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drones.Drone'),
        ),
        migrations.AddField(
            model_name='competition',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='drones.Pilot'),
        ),
    ]
