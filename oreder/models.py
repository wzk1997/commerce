from django.db import models
from Users.models import Users


class order(models.Model):
    id = models.AutoField(primary_key=True)
    # 下单时间
    prder_time = models.TimeField()
    # 所属用户
    users = models.ForeignKey(Users)
    # 收货人
    recv_name = models.CharField(max_length=10)
    # 收货地址
    recv_address = models.TextField()
    # 联系方式
    recv_phone = models.IntegerField()
    # 备注信息
    recv_remark = models.CharField(max_length=255)
    # 总金额
    totale = models.IntegerField()


class Orderltem(models.Model):
    id = models.AutoField(primary_key=True)
    # 购买商品编号
    oi_goods_id = models.IntegerField()
    # 购买商品名称
    oi_goods_name = models.CharField(max_length=20)
    # 购买商品单价
    oi_goods_price = models.IntegerField()
    # 购买商品数量
    oi_goods_count = models.IntegerField()
    # 成交价格
    deal_price = models.IntegerField()
    # 所属订单
    order = models.ForeignKey(order)
# Create your models here.
