from django.db import models
from Users.models import Users


class order(models.Model):
    id = models.AutoField(primary_key=True)
    # �µ�ʱ��
    prder_time = models.TimeField()
    # �����û�
    users = models.ForeignKey(Users)
    # �ջ���
    recv_name = models.CharField(max_length=10)
    # �ջ���ַ
    recv_address = models.TextField()
    # ��ϵ��ʽ
    recv_phone = models.IntegerField()
    # ��ע��Ϣ
    recv_remark = models.CharField(max_length=255)
    # �ܽ��
    totale = models.IntegerField()


class Orderltem(models.Model):
    id = models.AutoField(primary_key=True)
    # ������Ʒ���
    oi_goods_id = models.IntegerField()
    # ������Ʒ����
    oi_goods_name = models.CharField(max_length=20)
    # ������Ʒ����
    oi_goods_price = models.IntegerField()
    # ������Ʒ����
    oi_goods_count = models.IntegerField()
    # �ɽ��۸�
    deal_price = models.IntegerField()
    # ��������
    order = models.ForeignKey(order)
# Create your models here.
