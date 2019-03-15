from django.db import models
from Users.models import Users



class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name='店铺名称')
    # 店铺图片
    cover = models.ImageField(upload_to='static/storp/storpimg.png')
    # 开店描述
    intro = models.CharField(max_length=255)
    # 开店时间
    opener_time = models.DateTimeField(auto_now_add=True, verbose_name='开店时间')
    # 店铺状态 0 正常营业 1 暂停营业 2 永久删除
    status = models.IntegerField(default=0, verbose_name='店铺状态')
    # 对应的用户主键
    users = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='店铺所属用户')
# Create your models
# here.
