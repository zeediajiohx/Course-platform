from django.shortcuts import render, HttpResponse, redirect
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..models import UserInfo
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
import re
import random
from videoclasstest1.utils.checkpic import check_code
# Create your views here.

# 重要，函数

#djangorestframe方法校验正则
def ckodevali(value):
    if re.match(r"^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$",value):
        return
    raise ValidationError('手机格式错误')


#序列化器
class chkcodesSerializer(serializers.Serializer):
    phone = serializers.CharField(label='sjh',validators=[ckodevali,])


class messview(APIView):
    def get(self,request,*args,**kwargs):
        """
        1.获取手机号
        2.手机格式验证
        3.生成随机验证码
        4.验证码发送到手机上
        5.验证码+手机号保留，超时时间 conn.set("131XXXXXXXX","2467",ex=30)
                                code = conn.get("131XXXXXXX")
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 1.获取手机号
        phone = request.query_params.get('phone')
        print(phone)
        # if not re.match(r"^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$",phone) :
        #     return Response('手机格式错误') 同下
        # 2.手机格式验证
        ser = chkcodesSerializer(data=request.query_params)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)
        # 3.生成随机验证码
        code = random.randint(100000,999999)
        # 4.验证码发送到手机上


        #5.1搭建redis服务器
        #5.2安装django-redis ; peizhi:settings.py
        from django_redis import get_redis_connection
        conn = get_redis_connection()
        conn.set(phone,code,ex=30)



        return Response({"status":True,'message':'successfuly'})


class LoginView(APIView):
    def post (self,request,*args,**kwargs):
        print(request.data)
        return Response({"status":True})




def index(request):
    return HttpResponse("HelloWorld!")

def user_list(request):
    #如果settings加上根目录的templates，找根目录下的templates
    # 在video class（app）目录的templates找，根据app注册顺序逐一找
    return render(request, "user_list.html")

def test(request):
    name = 'what'
    list = ['lora','wifi','mist','dsf']
    dictor = {"name":"hhh","salary":1000 ,"role":"sfsd"}
    dic_list = [
        {"name": "hhh", "salary": 1000 ,"role": "sfsd"},
        {"name": "ggg", "salary": 1000 ,"role": "sfsd"},
        {"name": "fff", "salary": 1000 ,"role": "sfsd"}
    ]
    return render(request, 'test.html', {"n1":name, "n2":list, "n3":dictor, "n4":dic_list})

def getsth(req):
    #request是个对象，是用户通过浏览器发送过来的所有请求相关的数据
    print(req.method)#get post两种请求方式
    print(req.GET)
    print(req.POST)

    return redirect("https://baidu.com")#重定向，
    # return HttpResponse('neirong')#响应

"""************1.序列化器，序列化单个用户对象*************"""
"""
from ..serializers import UserInfoSerializer
from ..models import UserInfo
#1.获取用户对象
User = UserInfo.objects.get(id=1)
#2.创建序列化器,
# instance=XX表示要序列化的对象
serializer = UserInfoSerializer(instance=User)
#3.转换数据
print(serializer.data)
"""

"""************2.序列化器，序列化列表用户对象*************"""
"""
from ..serializers import UserInfoSerializer
from ..models import UserInfo
#1.获取用户对象
User = UserInfo.objects.all()
#2.创建序列化器,
# instance=XX表示要序列化的对象
serializer = UserInfoSerializer(instance=User,many=True)
#3.转换数据
print(serializer.data)
#结果
# [OrderedDict([('id', 1), ('name', 'JinhuiZhang'), ('password', '123')]),
# OrderedDict([('id', 2), ('name', '333'), ('password', '444')])]

"""
