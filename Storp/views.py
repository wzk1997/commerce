from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.views.decorators.http import require_GET


@csrf_exempt
# 添加店铺
def add(request):
    if request.method == 'GET':
        return render(request, 'storp/add.html')
    elif request.method == 'POST':
        id = request.session.get('art')
        print(id)
        name = request.POST.get('name')
        intro = request.POST.get('intro')  # 店铺信息
        try:
            # 店铺图片
            cover = request.FILES.get('cover')
            store = models.Store(name=name, cover=cover, intro=intro, users_id=id)
        except:
            store = models.Store(name=name, intro=intro, users_id=id)
        store.save()
        return redirect(reverse('Storp:list'))
        # return redirect(reverse('storp:detail',kwargs={'s_id':store.id}))


# 店铺列表
@require_GET
def list(request):
    id = request.session.get('art')
    print(id)
    storplist = models.Store.objects.filter(users=id)
    print(storplist)
    return render(request, 'storp/list.html', {'storplist': storplist})


# 更改店铺
def update(request, s_id):
    pass


# 店铺详情
def detail(request, s_id):
    if request.method == 'GET':
        storp = models.Store.objects.filter(pk=s_id)
        return render(request, 'storp/detailc.html', {"storp": storp})


@require_GET
# 修改店铺状态
def change(request, s_id, stutas):
    storp = models.Store.objects.get(id=s_id)
    storp.status = int(stutas)
    storp.save()
    return render(request, 'storp/detailc.html', {"storp": storp})
