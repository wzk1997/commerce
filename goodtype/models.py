from django.db import models
from storp.models import Store


class GoodsType(models.Model):
    # 商品ID
    id = models.AutoField(primary_key=True)
    # 商品名字 unique 设定名字不能重复
    name = models.CharField(max_length=30, unique=True, verbose_name='商品名字')
    # 商品图片
    cover = models.ImageField(upload_to='static/goodtyp')
    # 商品描述
    intro = models.TextField(verbose_name='商品类别描述')
    # 自关联
    parent = models.ForeignKey('self', null=True, blank=True,verbose_name='关联父级',on_delete=models.CASCADE)


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    # 商品名字
    name = models.CharField(max_length=255, verbose_name='商品名字')
    # 商品价格DecimalField 更准确的表示浮点数 max_digits 表示位数 decimal_places 表示小数点后面的位数
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='商品价格')
    # 商品库存
    stock = models.IntegerField(verbose_name='商品库存')
    # 商品数量
    count = models.IntegerField( verbose_name='商品数量')
    # 上架时间
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上架时间')
    # 商品介绍
    intro = models.TextField(verbose_name='商品介绍')
    # 商品类型
    type = models.ForeignKey(GoodsType,verbose_name='商品类型',on_delete=models.CASCADE)
    # 所属店铺 on_delete 根据ID 进行删除·
    store = models.ForeignKey(Store, verbose_name='所属店铺',on_delete=models.CASCADE)


class Goodsimage(models.Model):
    id = models.AutoField(primary_key=True)
    # 商品图片
    path = models.ImageField(upload_to='static/goodtyp', verbose_name='商品图片')
    # 商品状态
    status = models.BooleanField(default=False, verbose_name='商品默认状态')
    # 所属商品
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

# Create your models here.
