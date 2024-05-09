import re
import random,string
import uuid
from django.shortcuts import render,HttpResponse, redirect
from django import forms
from django.forms import Form,ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django_redis import get_redis_connection
from videoclasstest1 import models
from ..utils import wxcode2Session
from videoclasstest1.utils.checkpic import check_code
from videoclasstest1.utils.auth import UserAuthentication
#图片验证码
from io import BytesIO
def showcode(request):


    if request.method=="GET":
        pics, codes = check_code()
        print(codes)
        # conn = get_redis_connection()
        # conn.set()
        # 写入到自己的session中
        request.session['pics_code'] = codes
        # 给session 设置60秒超时
        # request.session.set_expiry(60)
        stream = BytesIO()
        pics.save(stream, 'png')
        return HttpResponse(stream.getvalue())
    # if request.method=="POST":
    #     # data = json.loads(request.body.decode('utf-8'))
    #     imgcodes = request.session.get('pics_code',"")
    #     submmitcode = request.POST.get('code',None)
    #     print("1",submmitcode,"2",imgcodes)
    #     if submmitcode==imgcodes:
    #         return JsonResponse({'code': 0,'msg': 'Right'})
    #     else:
    #         return JsonResponse({'code': 1,'msg': 'error'})
    return HttpResponse("stherror")

class loadform(Form):
    username = forms.CharField(label='name',widget=forms.TextInput)
    password = forms.CharField(label='pwd')

""" page style"""
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     #circlate all the fields in the Form,setting properties for the plug-in
    #     for name,field in self.fields.items():
    #         if field .widget.attrs:
    #             field.widget.attrs["class"] = "XXXX"
    #             field.widget.attrs["placeholder"] = field.label
    #         else:
    #             field.widget.attrs = {
    #                 "class" : "XXXX",
    #                 "placeholder" : field.label
    #             }

def logins(request):
    videoID = 0
    # 处理登录表单
    if request.method == "POST":
        # 获取登录信息
        imgcode = request.session.get('pics_code')
        print("imgcode",imgcode)
        userID = request.POST.get('userID', None)
        password = request.POST.get('password', None)
        chkcode = request.POST.get('code',None)
        print("uere",userID,"psd",password,"chkc",chkcode)
        if (imgcode!=chkcode):
            message = {'code':4,'msg':'验证码错误'}

        message = {'code':0,'msg':'需要填写完整'}
        if userID and password:
            # 移除首位空格
            IDpop = userID.strip()
            # 密码验证
            try:
                user = models.User.objects.get(userID=IDpop)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.userID
                    request.session['user_name'] = user.nickname
                    print("uuuuu",user.password)
                    message= {'code':1,"msg":'success'}
                else:

                    print("uuuuu",user.password,"pwddd",password)
                    message = {'code':2,"msg":"password or ID error"}
            except:
                user = models.User.objects.get(userID='3270085366724')
                print(user)
                message = {'code':3,"msg":'no such user'}
        print(message)
        return JsonResponse(message)
    # GET 请求直接返回登录页



class login(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name","password"]



@csrf_exempt
def user_login(request):
    if request.method == "GET":
        form = login
        return render(request,"user_login.html",{"form": form})
    form = login(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        return HttpResponse("chenggong")

        # return  ({"status":True,'message':'successfuly'})

    else:
        print(form.errors)


class useinfoserialization(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['nickname','academy','major','sex','grade']

class getuserinfo(APIView):
    authentication_classes = [UserAuthentication,]
    def post(self,request,*args,**kwargs):
        ser = useinfoserialization(data=request.data)
        if not ser.is_valid():
            return Response({},status=status.HTTP_400_BAD_REQUEST)

        # ser.save(userID = request.user)
        # return Response(ser.data, status=status.HTTP_201_CREATED)

        newnickname = ser.data.get('nickname')
        academy = ser.data.get('academy')
        major = ser.data.get('major')
        sex = ser.data.get('sex')
        grade = ser.data.get('grade')
        models.User.objects.filter(userID=request.user.userID).update(nickname=newnickname,academy=academy,major=major,sex=sex,grade=grade)
        return Response({}, status=status.HTTP_200_OK)


class magloginSerializer(serializers.Serializer):
    userID = serializers.CharField(label="账号")
    password = serializers.CharField(label="密码")
    nickname = serializers.CharField(label="昵称")
    avatar = serializers.CharField(label="头像")
    def validate_password(self, value):
        userID = self.initial_data.get('userID')
        IDpop = userID.strip()
        try:
            user = models.User.objects.get(userID=IDpop)
            if user.root != 1:
                print("非管理员账号！")
                raise ValidationError("非管理员账号！")
            if user.password != value:
                print("mmacw")
                raise ValidationError("密码错误！")
        except:
            print("yhbcz")
            raise ValidationError('用户不存在！')
        return value




class managerlogin(APIView):
    def post(self, request, *args, **kwargs):
        print('managerrequest', request.data)
        """"""

        # 正式操作
        ser = magloginSerializer(data=request.data)

        if not ser.is_valid():
            return Response({"status": False, 'message': '账号或密码错误！'})

        userID = ser.validated_data.get('userID')
        clearid = userID.strip()
        nickname = ser.validated_data.get('nickname')
        avatar = ser.validated_data.get('avatar')
        # user_object, flag = models.UserInfo.objects.get_or_create(
        #     telephone=phone,
        #     defaults={
        #         "nickname": nickname,
        #         'avatar': avatar}
        # )
        user_object = models.User.objects.get(userID=clearid)
        try:
            user_object.nickname = nickname
            user_object.avatar = avatar
            user_object.token = str(uuid.uuid4())
            user_object.save()
        except:
            code = []
            for i in range(4):
                char = random.choice(string.ascii_letters+string.digits)
                code.append(char)
            # user_object.nickname = "professor-{0}".format(code)
            user_object.nickname = nickname
            user_object.avatar = 'https://videotest1-1301605345.cos.ap-nanjing.myqcloud.com/%E6%A0%A1%E5%BE%BD.jpg'
            user_object.token = str(uuid.uuid4())
            user_object.save()

        return Response({"status": True, "data": {"token": user_object.token, 'userid': clearid}})




# def phone_validator(value):
#     if not re.match(r"^(1[3|4|5|6|7|8|9])\d{9}$",value):
#         raise ValidationError('手机格式错误')

class userloginSerializer(serializers.Serializer):
    # ID = serializers.CharField(label="手机号",validators=[phone_validator, ])
    code = serializers.CharField(label='wx.code')
    nickname = serializers.CharField(label="昵称")
    avatar = serializers.CharField(label='头像')
    # avatar = serializers.CharField(label='头像')
    # academy = serializers.CharField(label='学院')
    # major = serializers.CharField(label='专业')
    # grade = serializers.CharField(label='年级')
    # gender = serializers.CharField(label='性别')


class userlogin(APIView):
    def post(self, request):
        print('request', request)
        # ser = userloginSerializer(data=request.data)
        # if not ser.is_valid():
        #     return Response({"status": 1, "msg": '缺少参数'})
        # code = ser.validated_data.get('code')
        # nickname = ser.validated_data.get('nickname')
        # avatar = ser.validated_data.get('avatar')
        param = request.data
        print(request.data)
        if not param.get('code'):
            return Response({"status": 1, "msg": '缺少参数'})
        else:
            code = param.get("code")
            nickname = param.get("nickname")
            avatar = param.get('avatar')
            user_data = wxcode2Session.get_login_info(code)

            if user_data:
                openID = user_data['openid']
                sessionKey =user_data['session_key']
                # val = user_data['session_key'] + "&" + user_data['openid']
                # md5 = hashlib.md5()
                # md5.update(str(time.clock()).encode("utf-8"))
                # key = md5.hexdigest()
                # cache.set(key, val)  # 放进内存redis库中,把key传给前端当token.下次前台带着key就能拿到val
                try:
                    user_object = models.User.objects.get(userID=openID)  # 判断openid是否存在
                    try:
                        user_object.nickname = nickname
                        user_object.avatar = avatar
                        user_object.root = 0
                        user_object.password = sessionKey
                        user_object.token = str(uuid.uuid4())
                        user_object.save()
                    except:
                        user_object.nickname = nickname
                        user_object.avatar = "https://videotest1-1301605345.cos.ap-nanjing.myqcloud.com/%E6%A0%A1%E5%BE%BD.jpg"
                        user_object.root = 0
                        user_object.password = sessionKey
                        user_object.token = str(uuid.uuid4())
                        user_object.save()

                except:
                    try:
                        print("NN",nickname)
                        user_object, flag = models.User.objects.get_or_create(
                            userID=openID,
                            defaults={
                                "nickname": nickname,
                                'avatar': avatar,
                                'root':0,
                                'password': sessionKey
                            }
                        )
                        user_object.token = str(uuid.uuid4())
                        user_object.save()
                        print("可以更新",user_object.nickname)
                    except:
                        user_object, flag = models.User.objects.get_or_create(
                            userID=openID,
                            defaults={
                                "nickname": nickname,
                                'avatar': "https://videotest1-1301605345.cos.ap-nanjing.myqcloud.com/%E6%A0%A1%E5%BE%BD.jpg",
                                'root': 0,
                                'password': sessionKey
                            }
                        )
                        user_object.token = str(uuid.uuid4())
                        user_object.save()
                        print("校徽")

                    print("新token了")
                    # models.User.objects.create(openid=user_data['openid'])
                return Response({
                    "status": True,
                    "msg": "ok",
                    "data": {"token": user_object.token,"userid":user_object.userID}
                })
            else:
                return Response({"status": 0, "data": "无效的code"})
    # def post(self,request,*args,**kwargs):
    #     print('request',request)
    #     ser = userloginSerializer(data = request.data)
    #     userID = ser.validated_data.get('phone')
    #     nickname = ser.validated_data.get('nickname')
    #     avatar = ser.validated_data.get('avatar')
    #     # major = ser.validated_data.get('major')
    #     # grade = ser.validated_data.get('grade')
    #     # gender = ser.validated_data.get('gender')
    #     root = False
    #     #
    #     # # 临时操作
    #     # phone = request.data.get('phone')
    #     # nickname = request.data.get('nickname')
    #     # avatar = request.data.get('avatar')
    #
    #     # phone = ser.validated_data.get("phone")
    #     # user_object ,flag = models.UserInfo.objects.get_or_create(phone=phone)
    #
    #     user_object, flag = models.User.objects.get_or_create(
    #         userID = userID,
    #         defaults={
    #             "nickname": nickname,
    #             'avatar': avatar}
    #     )
    #     user_object.token = str(uuid.uuid4())
    #     user_object.save()
    #
    #     return Response({"status": True, "data": {"token": user_object.token, 'phone': phone}})

"""
from videclass1 import models
class LoadModelForm(forms.ModelForm):
    class Meta:
      model = model.Admin
      fields = ['username','password']
"""
