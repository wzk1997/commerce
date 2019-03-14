from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.


# 用户类
class Users(models.Model):
    # 用户编号
    id = models.AutoField(primary_key=True)
    # 登陆账号
    username = models.IntegerField(verbose_name='登陆账号')
    # 登陆密码
    userpass = models.IntegerField(verbose_name='登陆密码')
    # 用户昵称
    nickname = models.CharField(max_length=20,verbose_name='用户昵称')
    # 用户年龄
    age = models.IntegerField(verbose_name='用户年龄')
    # 用户性别
    gender = models.CharField(max_length=3,verbose_name='用户性别')
    # 用户头像
    header = models.ImageField(upload_to="static/imag/",verbose_name='用户头像')
    # 联系方式
    phone = models.IntegerField(verbose_name='联系方式')
    # 电子邮箱
    email = models.CharField(max_length=40,verbose_name='电子邮箱')
    # 注册时间
    regist_time = models.TimeField(auto_now_add=True,verbose_name='注册时间')
    # 上次登录时间
    last_login_time = models.DateField(auto_now_add=True,verbose_name='上次登录时间')
    # 用户状态0锁定1可用2删除
    status = models.IntegerField(default=1)


# 收货地址
class Address(models.Model):
    # 地址编号
    id = models.AutoField(primary_key=True)
    # 所属用户
    users = models.CharField(max_length=20)
    # 收货人姓名
    recv_name = models.CharField(max_length=20)
    # 收货人联系方式
    recv_phone = models.IntegerField()
    # 国家
    native = models.CharField(max_length=20)
    # 省区
    provice = models.CharField(max_length=20)
    # 市区
    city = models.CharField(max_length=20)
    # 县区
    country = models.CharField(max_length=20)
    # 街道
    street = models.CharField(max_length=20)
    # 详细描述
    desc = HTMLField(null=False)
    # 是否默认地址     [True默认 False非默认]
    status = models.BooleanField(True)
    # 外键连接用户
    addressUser = models.ForeignKey(Users)


    # 和系统内置的用户管理的一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE)
