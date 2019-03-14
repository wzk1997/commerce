from django.db import models
from Users.models import Users
class Shopcart(models.Model):
    id = models.AutoField(primary_key=True)
    #������Ʒ
    goods = models.CharField(max_length=20)
    #��������
    count = models.IntegerField()
    #���ʱ��
    add_time = models.TimeField()
    #С�ǽ��
    subtotal = models.IntegerField()
    #�����û�
    users = models.ForeignKey(Users)


# Create your models here.
