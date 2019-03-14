from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, logout, login
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from . import models, utils



  # 这个方法是一个装饰器 只有在登录的时候才能访问到
# 登陆之后用户看到的主页
def homepage(req):
    return render(req, 'Users/homepage.html')


  # 这个方法是一个装饰器 只有在登录的时候才能访问到
# 退出登录
def user_logout(req):
    logout(req)
    return render(req, 'Users/login.html')


# 登陆
@csrf_exempt
def login(req):
    if req.method == 'GET':
        return render(req, 'Users/login.html')
    elif req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        try:
            art = models.Users.objects.get(username=username, userpass=password)
            req.session['art'] = art.id
            print(art)
            return render(req,'Users/homepage.html')
        except:
            return render(req, 'Users/login.html', {'mas', '密码错误'})


# 注册
@csrf_exempt
def register(req):
    if req.method == 'GET':
        return render(req, 'Users/register.html')
    elif req.method == 'POST':
        username = req.POST.get('Username')
        password = req.POST.get('Password')
        nickname = req.POST.get('nickname')
        age = req.POST.get('age')
        gender = req.POST.get('gender')
        henader = req.FILES.get('henader')
        email = req.POST.get('email')
        phone = req.POST.get('phone')

        try:
            models.Users.objects.get(username=username)

            return render(req, 'Users/register.html', {'mas': '账号存在请重新输入'})
        except:
            user = models.Users(username=username,
                                userpass=password,
                                nickname=nickname,
                                age=age,
                                gender=gender,
                                header=henader,
                                email=email,
                                phone=phone,
                                )
            user.save()
        return render(req, 'Users/login.html', {'mas': '验证码错误'})

    return render(req, 'Users/register.html')

# 个人中心
def personal(req):
    if req.method == 'GET':
        id = req.session.get('art')
        art = models.Users.objects.filter(pk=id)
        req.session['id'] = id
        return render(req, 'Users/personal.html', {'art': art})
    elif req.method == 'POST':
        id = req.session.get('id')
        print(id)
        nickname = req.POST.get('nickname')
        phone = req.POST.get('phone')
        age = req.POST.get('age')
        gender = req.POST.get('gender')
        email = req.POST.get('email')
        uimg = req.FILES.get('header')
        models.Users.objects.filter(id=id).update(nickname=nickname,
                                                  gender=gender,
                                                  phone=phone,
                                                  age=age,
                                                  email=email,
                                                  header=uimg,
                                                  )
        return render(req, 'Users/index1.html')


@login_required
def address(req):
    return render(req, 'Users/address.html')


# # Create yourin.html') views here.

# 添加图片验证码
def addutils(req):
    # 创建内存空间
    B = BytesIO()
    # 引入图片和数字
    img, code = utils.create_code()
    # 保存图片
    # 将图片保存在内存空间
    req.session['check_code'] = code
    img.save(B, 'PNG')
    return HttpResponse(B.getvalue())
