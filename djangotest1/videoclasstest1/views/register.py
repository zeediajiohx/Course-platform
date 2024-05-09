from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from ..models import User
from videoclasstest1.utils.checkpic import check_code
from io import BytesIO

#picture checkcode
def showcode(request):
    pics, codes = check_code()
    print("registe", codes)
    # 写入到自己的session中
    request.session['pics_code'] = codes
    request.session.set_expiry(60)
    if request.method=="GET":

        stream = BytesIO()
        pics.save(stream, 'png')
        return HttpResponse(stream.getvalue())

    if request.method=="POST":
        submmitcode = request.POST.get('code',None)
        if submmitcode==codes:
            return JsonResponse({'code': 0,'msg': 'Right'})
        else:
            return JsonResponse({'code': 1,'msg': 'error'})

def register(request):
    # 如果已经登录就直接返回主页
    message = ""
    # 处理注册表单
    if request.method == "POST":
        # 获取表单信息
        userID = request.POST.get("userID", None)
        password = request.POST.get("password", None)
        repassword = request.POST.get("repassword", None)
        # 处理账号重复、密码不一致问题
        if User.objects.filter(userID=userID):
            message = {"code": 0, "msg": "账号已存在，请直接登录！"}
        elif password!=repassword:
            message = {"code": 1, "msg": "两次密码不一致！"}
        else:
            User.objects.create(userID=userID, password=password)
            message = {"code": 2, "msg": "注册成功，请登录！"}
        return JsonResponse(message)


