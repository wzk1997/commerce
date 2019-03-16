from django.db import models
from Users.models import Users
class Shopcart(models.Model):
    id = models.AutoField(primary_key=True)
    #购买商品
    goods = models.CharField(max_length=20)
    #购买数量
    count = models.IntegerField()
    #添加时间
    add_time = models.TimeField()
    #小记金额
    subtotal = models.IntegerField()
    #所属用户
    users = models.ForeignKey(Users)


# Create your models here.
