# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-14 01:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('cover', models.ImageField(upload_to='static/images')),
                ('intro', models.CharField(max_length=255)),
                ('opener_time', models.TimeField()),
                ('status', models.IntegerField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Users')),
            ],
        ),
    ]
