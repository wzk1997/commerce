# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-16 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='商品名字')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品价格')),
                ('stock', models.IntegerField(verbose_name='商品库存')),
                ('count', models.IntegerField(verbose_name='商品数量')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='上架时间')),
                ('intro', models.TextField(verbose_name='商品介绍')),
                ('goods_detail_type', models.CharField(max_length=255, verbose_name='商品类型')),
                ('goods_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storp.Store', verbose_name='所属店铺')),
            ],
        ),
        migrations.CreateModel(
            name='Goodsimage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.ImageField(upload_to='static/goodtyp', verbose_name='商品图片')),
                ('status', models.BooleanField(default=False, verbose_name='商品默认状态')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodtype.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='商品名字')),
                ('cover', models.ImageField(upload_to='static/goodtyp')),
                ('intro', models.TextField(verbose_name='商品类别描述')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goodtype.GoodsType')),
            ],
        ),
    ]
