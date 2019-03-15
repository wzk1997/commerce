from django.db import models
from storp.models import Store


class GoodsType(models.Model):
    # ��Ʒz
    id = models.AutoField(primary_key=True)
    # ��Ʒ����
    gt_name = models.CharField(max_length=30)
    # ��ƷͼƬ
    cover = models.ImageField(upload_to='static/images')
    # �������
    gt_desc = models.TextField()


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    # ��Ʒ����
    name = models.CharField(max_length=255)
    # ��Ʒ����
    price = models.IntegerField()
    # ��Ʒ���
    stock = models.IntegerField()
    # ��������
    count = models.IntegerField()
    # �ϼ�ʱ��
    add_time = models.TimeField()
    # ��Ʒ����
    desc = models.CharField(max_length=255)
    # ��Ʒ����
    goods_detail_type = models.CharField(max_length=255)
    # ��������
    goods_store = models.ForeignKey(Store)


class Goodsimage(models.Model):
    id = models.AutoField(primary_key=True)
    # ͼƬ·��
    path = models.ImageField(upload_to='static/images')
    # Ĭ��չʾ
    status = models.ImageField(upload_to='static/imgages')
    # ������Ʒ
    goods = models.ForeignKey(Goods)

# Create your models here.
