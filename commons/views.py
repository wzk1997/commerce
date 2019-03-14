from django.shortcuts import render,HttpResponse
from . import utils
from io import BytesIO
def baes(request):
    return render(request,'baes.html')

def additils(requset):
    # 创建内存空间
    B = BytesIO()
    # 引入图片和数字
    img, code = utils.create_code()
    # 保存图片
    # 将图片保存在内存空间
    requset.session['check_code'] = code
    img.save(B, 'PNG')
    return HttpResponse(B.getvalue())
# Create your views here.
