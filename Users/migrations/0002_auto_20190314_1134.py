# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-14 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=40, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=3, verbose_name='用户性别'),
        ),
        migrations.AlterField(
            model_name='users',
            name='header',
            field=models.ImageField(upload_to='static/imag/', verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_login_time',
            field=models.DateField(auto_now_add=True, verbose_name='上次登录时间'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(verbose_name='联系方式'),
        ),
        migrations.AlterField(
            model_name='users',
            name='regist_time',
            field=models.TimeField(auto_now_add=True, verbose_name='注册时间'),
        ),
    ]
