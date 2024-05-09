import re
import random
import requests,json
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView,CreateAPIView
from django.forms import model_to_dict
from rest_framework import status
from django.db.models import F
from ..models import UserInfo,User,Video,like,Collect,classcollectRecord,class_detail,ViewerRecord,CommentRecord,classFavorRecord,Care
from ..utils.auth import GeneralAuthentication,UserAuthentication
from djangotest1 import settings

# def video(request,videoID):
#     # 没登录直接去登录
#     if not request.session.get('is_login', None):
#     # return redirect('/login/?videoID='+str(videoID), locals())
#     userid = request.session.get('user_id')
#     user = User.objects.get(userID=userid)
#     video = Video.objects.get(videoID=videoID)
#     othervideos = Video.objects.all()[:5]
#     if request.method == "POST":
#         if request.POST.get("like",None):
#             ll = Like.objects.filter(userID=userid).filter(videoID=videoID)
#             if ll:
#                 ll.delete()
#                 video.like -= 1
#                 video.save()
#                 message = "<script>alert(\"取消点赞！\")</script>"
#                 return render(request, 'video.html', locals())
#             else:
#                 video.like += 1
#                 video.save()
#                 Like.objects.create(userID=userid,videoID=videoID)
#                 message = "<script>alert(\"点赞成功！\")</script>"
#                 # return render(request, 'video.html', locals())
#         if request.POST.get("collect",None):
#             cc = Collect.objects.filter(userID=userid).filter(videoID=videoID)
#             if cc:
#                 cc.delete()
#                 video.collect -= 1
#                 video.save()
#                 message = "<script>alert(\"取消收藏！\")</script>"
#                 return render(request, 'video.html', locals())
#             else:
#                 video.collect += 1
#                 video.save()
#                 Collect.objects.create(userID=userid,videoID=videoID)
#                 message = "<script>alert(\"收藏成功！\")</script>"
#                 return render(request, 'video.html', locals())
#
#
#     return render(request, 'video.html', locals())

# def upload(request):
#     # 没登录直接去登录
#     if not request.session.get('is_login', None):
#         return redirect('/login/')
#     userid = request.session.get('user_id')
#     user = User.objects.get(userID=userid)
#     # 没有限权直接打回
#     if user.root is False:
#         return redirect('/user/', locals())
#     new = {}
#     if Video.objects.all().aggregate(Max('videoID'))["videoID__max"] is None:
#         new["id"] = 1
#     else:
#         print(Video.objects.all().aggregate(Max('videoID'))["videoID__max"])
#         new["id"] = Video.objects.all().aggregate(Max('videoID'))["videoID__max"] + 1
#     new["academy"] = user.academy
#
#     if request.method == "POST":
#
#         # 缓存一部分数据
#         new["academy"] = request.POST["academy"]
#         new["subject"] = request.POST["subject"]
#         new["section"] = request.POST["section"]
#
#         # 保存视频封皮
#         img = request.FILES.get("icon", None)
#         if img is not None and img.name.split('.')[-1] not in ['jpg', 'png', 'jpeg']:
#             message = "<script>alert(\"图片格式错误请重新上传！\")</script>"
#             return render(request, 'upload.html', locals())
#         elif img is not None:
#             # 保存图片
#             path = './static/videoImg/' + img.name
#             with open(path, 'wb') as f:
#                 for content in img.chunks():
#                     f.write(content)
#             user.icon = img.name
#
#         # 保存视频
#         newvideo = request.FILES.get("newvideo", None)
#         print(newvideo)
#         if newvideo is not None and newvideo.name.split('.')[-1] not in ['mp4']:
#             message = "<script>alert(\"视频格式错误请重新上传！\")</script>"
#             return render(request, 'upload.html', locals())
#         elif newvideo is not None:
#             # 保存视频
#             path = './static/video/' + newvideo.name
#             with open(path, 'wb') as f:
#                 for content in newvideo.chunks():
#                     f.write(content)
#
#         Video.objects.create(videoID=new["id"],
#                              academy = request.POST["academy"],
#                              subject = request.POST["subject"],
#                              section = request.POST["section"],
#                              name = request.POST["name"],
#                              owner = user.userID,
#                              icon = img.name,
#                              file= newvideo.name
#                              )
#
#         message = "<script>alert(\"视频上传成功！\")</script>"
#         return render(request, 'upload.html', locals())
#
#     return render(request, 'upload.html', locals())


# def classupload(request):
#
#     message = ""
#     # 处理注册表单
#     if request.method == "POST":
#         # 获取表单信息
#         title = request.POST.get("userID", None)
#         password = request.POST.get("password", None)
#         repassword = request.POST.get("repassword", None)
#         # 处理账号重复、密码不一致问题
#         if User.objects.filter(userID=userID):
#             message = "<script>alert(\"账号已存在，请直接登录！\")</script>"
#             return render(request, 'register.html', locals())
#         elif password != repassword:
#             message = "<script>alert(\"两次密码不一致！\")</script>"
#             return render(request, 'register.html', locals())
#         else:
#             message = "<script>alert(\"注册成功请登录！\")</script>"
#             User.objects.create(userID=userID, password=password)
#             # 注册成功，进入登录界面
#             return redirect('/login/', locals())
#     return render(request, 'register.html', locals())

class clsvidModelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['videoID','icon','content','topic','user','like','collect',]
    def get_user(self,obj):
        return model_to_dict(obj.user,fields=['userID','nickname','avatar'])
        # return {'id':obj.user_id,'nickname':obj.user.name,'avater':obj.user.avatar}
    def get_topic(self,obj):
        if not obj.topic:
            return
        return {'id':obj.topic_id,'title':obj.topic.title}
#*****************************课程列表***************************
class classcotns(APIView):
    def get(self,request,*args,**kwargs):
        min_id = request.query_params.get('min_id')
        max_id = request.query_params.get('max_id')
        if min_id:
            queryset = Video.objects.filter(videoID__lt=min_id).order_by('-videoID')[0:10]
        elif max_id:
            queryset = Video.objects.filter(videoID__gt=max_id).order_by('videoID')[0:10]
        else:
            queryset = Video.objects.all().order_by('-videoID')[0:10]
        ser = clsvidModelSerializer(instance=queryset,many=True)
        return Response(ser.data,status=200)

class selectedclasscotns(APIView):
    def get(self,request,*args,**kwargs):
        min_id = request.query_params.get('min_id')
        max_id = request.query_params.get('max_id')
        topicid = request.query_params.get("topic")
        if min_id:
            queryset = Video.objects.filter(topic_id = topicid,videoID__lt=min_id).order_by('-videoID')[0:10]
        elif max_id:
            queryset = Video.objects.filter(topic_id = topicid,videoID__gt=max_id).order_by('videoID')[0:10]
        else:
            queryset = Video.objects.filter(topic_id = topicid).order_by('-videoID')[0:10]
        ser = clsvidModelSerializer(instance=queryset,many=True)
        return Response(ser.data,status=200)

#****************************关注模式****************************

class careclasscotns(APIView):
    authentication_classes = [UserAuthentication,]
    def get(self,request,*args,**kwargs):
        min_id = request.query_params.get('min_id')
        max_id = request.query_params.get('max_id')
        carewhoqust = Care.objects.filter(userID = request.user)
        careauth = []
        for row in carewhoqust:
            careauth.append(row.carewho)
        if min_id:
            queryset = Video.objects.filter(videoID__lt=min_id,user__in=careauth).order_by('-videoID')[0:10]
        elif max_id:
            queryset = Video.objects.filter(videoID__gt=max_id,user__in=careauth).order_by('videoID')[0:10]
        else:
            queryset = Video.objects.filter(user__in=careauth).order_by('-videoID')[0:10]
        print("carezuth",carewhoqust,"carequst",queryset)
        ser = clsvidModelSerializer(instance=queryset,many=True)
        return Response(ser.data,status=200)

class careselectedclasscotns(APIView):
    authentication_classes = [UserAuthentication]
    def get(self,request,*args,**kwargs):
        min_id = request.query_params.get('min_id')
        max_id = request.query_params.get('max_id')
        topicid = request.query_params.get("topic")
        carewhoqust = Care.objects.filter(userID=request.user)
        careauth = []
        for row in carewhoqust:
            careauth.append(row.carewho)
        if min_id:
            queryset = Video.objects.filter(topic_id = topicid,videoID__lt=min_id,user__in=careauth).order_by('-videoID')[0:10]
        elif max_id:
            queryset = Video.objects.filter(topic_id = topicid,videoID__gt=max_id,user__in=careauth).order_by('videoID')[0:10]
        else:
            queryset = Video.objects.filter(topic_id = topicid,user__in=careauth).order_by('-videoID')[0:10]
        ser = clsvidModelSerializer(instance=queryset,many=True)
        print("sermyrecod",ser.data)
        return Response(ser.data,status=200)
#****************************视频列表*****************************
# class videolist(APIView):

"""
#动态切分list
from utils.filters import MaxFilterBackend, MinFilterBackend
from utils.pagination import OldBoyLimitPagination
class NewsView(ListAPIView):
    serializer_class = NewsModelSerializer
    queryset = models.News.objects.all().order_by('-id')

    pagination_class = OldBoyLimitPagination
    filter_backends = [MinFilterBackend, MaxFilterBackend]

# ********filter:MaxFilterBackend, MinFilterBackend*********
from rest_framework.filters import BaseFilterBackend
class MinFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_id = request.query_params.get('min_id')
        if min_id:
            return queryset.filter(id__lt=min_id).order_by('-id')
        return queryset
class MaxFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        max_id = request.query_params.get('max_id')
        if max_id:
            return queryset.filter(id__gt=max_id).order_by('id')
        return queryset
#**************pagination ：OldBoyLimitPagination*****************
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
class OldBoyLimitPagination(LimitOffsetPagination):
    #本质上帮助我们进行切片的处理：[0:N]
    default_limit = 5
    max_limit = 50
    limit_query_param = 'limit'
    offset_query_param = 'offset'

    def get_offset(self, request):
        return 0
    def get_paginated_response(self, data):
        return Response(data)
"""
#******************************课程详细***************************
class classDetailModelserializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    createtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    user = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()
    viewer = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    is_favor = serializers.SerializerMethodField()
    is_collect = serializers.SerializerMethodField()
    is_care = serializers.SerializerMethodField()

    class Meta:
        model = Video
        # fields="__all__"
        exclude = ['icon']
    def get_images(self,obj):
        detailqueryset = class_detail.objects.filter(videos=obj)
        # return [row.cos_path for row in detail_queryset]
        # return [{'id':row.id,'path':row.cos_path} for row in detail_queryset]
        return [model_to_dict(row, ['id', 'cos_path']) for row in detailqueryset]
    def get_user(self,obj):
        return model_to_dict(obj.user,fields=['userID','nickname','avatar','academy'])
        # return {'id':obj.user_id,'nickname':obj.user.name,'avater':obj.user.avatar}
    def get_topic(self,obj):
        if not obj.topic:
            return
        return {'id':obj.topic_id,'title':obj.topic.title}
    def get_viewer(self,obj):
        # 根据新闻的对象 obj(news)
        # viewer_queryset = models.ViewerRecord.objects.filter(news_id=obj.id).order_by('-id')[0:10]
        queryset = ViewerRecord.objects.filter(news_id=obj.videoID)
        viewer_object_list = queryset.order_by('-id')[0:10]
        context = {
            'count':queryset.count(),
            'result': [model_to_dict(row.user,['nickname','avatar']) for row in viewer_object_list]
        }
        return context
    def get_comment(self,obj):
        """
        获取所有的1级评论，再给每个1级评论获取一个二级评论。
        :param obj:
        :return:
        """
        # 1.获取所有的 一级 评论
        first_queryset = CommentRecord.objects.filter(news=obj,depth=1).order_by('id')[0:10].values(
            'id',
            'content',
            'depth',
            'user__nickname',
            'user__avatar',
            'create_date'
        )
        first_id_list = [ item['id'] for item in first_queryset]
        # 2.获取所有的二级评论
        # second_queryset = models.CommentRecord.objects.filter(news=obj,depth=2)
        # 2. 获取所有1级评论下的二级评论
        # second_queryset = models.CommentRecord.objects.filter(news=obj, depth=2,reply_id__in=first_id_list)
        # 2. 获取所有1级评论下的二级评论(每个二级评论只取最新的一条)
        from django.db.models import Max
        result = CommentRecord.objects.filter(news=obj, depth=2, reply_id__in=first_id_list).values('reply_id').annotate(max_id=Max('id'))
        second_id_list = [item['max_id'] for item in result] # 5, 8

        second_queryset = CommentRecord.objects.filter(id__in=second_id_list).values(
            'id',
            'content',
            'depth',
            'user__nickname',
            'user__avatar',
            'create_date',
            'reply_id',
            'reply__user__nickname'
        )

        import collections
        first_dict = collections.OrderedDict()
        for item in first_queryset:
            item['create_date'] = item['create_date'].strftime('%Y-%m-%d')
            first_dict[item['id']] = item

        for node in second_queryset:
            first_dict[node['reply_id']]['child'] = [node,]

        return first_dict.values()
    def get_is_favor(self,obj):
        # 1. 用户未登录
        user_object = self.context['request'].user
        if not user_object:
            return False

        # 2. 用户已登录
        print()
        exists = classFavorRecord.objects.filter(user=user_object,news=obj).exists()
        return exists
    def get_is_collect(self,obj):
        # 1. 用户未登录
        user_object = self.context['request'].user
        if not user_object:
            return False

        # 2. 用户已登录
        print()
        exists = classcollectRecord.objects.filter(user=user_object,news=obj).exists()
        return exists
    def get_is_care(self,obj):
        # 1. 用户未登录
        user_object = self.context['request'].user
        if not user_object:
            return False

        # 2. 用户已登录
        print()
        exists = Care.objects.filter(userID=user_object,carewho=obj.user).exists()
        return exists



class classDetailView(RetrieveAPIView):
    lookup_field = 'videoID'
    queryset = Video.objects
    serializer_class = classDetailModelserializer
#     添加用户访问记录
    def get(self,request, *args,**kwargs):

        response = super().get(request, *args,**kwargs)
        if not request.user:
            return response
        # 获取请求头中的token
        # 判断当前用户是否有访问此新闻的记录？
        news_object = self.get_object() # models.Video.objects.get(pk=pk)
        exists = ViewerRecord.objects.filter(user=request.user,news=news_object).exists()
        if exists:
            return response
        ViewerRecord.objects.create(user=request.user,news=news_object)
        # News.objects.filter(id=news_object.id).update(viewer_count=F('viewer_count')+1)

        return response



# def classcotns(request):
#     # Video.objects.all().orderby('-id')[0:10] 倒数前十条课程
#
#     if request.method == "GET":
#         return JsonResponse({'status':'true'})

#**************************评论************************************
# class CommentModelSerializer(serializers.ModelSerializer):
#     create_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
#     nickname = serializers.CharField(source='user.nickname', read_only=True)
#     avatar = serializers.CharField(source='user.avatar', read_only=True)
#     reply_nickname = serializers.CharField(source='reply.user.nickname', read_only=True)
#
#     class Meta:
#         model = CommentRecord
#         exclude = ["favor_count", "user"]
#
#     def get_user(self, obj):
#         return model_to_dict(obj.user, fields=['id', 'nickname', 'avatar'])
#
#
# class CommentView(CreateAPIView):
#     serializer_class = CommentModelSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user_id=1)
#

class CommentModelSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d')
    user__nickname = serializers.CharField(source='user.nickname')
    user__avatar = serializers.CharField(source='user.avatar')
    reply_id = serializers.CharField(source='reply.id')
    reply__user__nickname = serializers.CharField(source='reply.user.nickname')
    class Meta:
        model = CommentRecord
        exclude = ['news','user','reply','root']


class CreateCommentModelSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%Y-%m-%d',read_only=True)
    user__nickname = serializers.CharField(source='user.nickname',read_only=True)
    user__avatar = serializers.CharField(source='user.avatar',read_only=True)
    reply_id = serializers.CharField(source='reply.id',read_only=True)
    reply__user__nickname = serializers.CharField(source='reply.user.nickname',read_only=True)

    class Meta:
        model = CommentRecord
        # fields = "__all__"
        exclude = ['user','favor_count']

class CommentView(APIView):
    def get_authenticators(self):
        if self.request.method == 'POST':
            return [UserAuthentication(), ]
        return [GeneralAuthentication(), ]

    def get(self,request,*args,**kwargs):
        root_id = request.query_params.get('root')
        # 1. 获取这个根评论的所有子孙评论
        node_queryset = CommentRecord.objects.filter(root_id=root_id).order_by('id')
        # 2. 序列化
        ser = CommentModelSerializer(instance=node_queryset,many=True)

        return Response(ser.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        # 1. 进行数据校验: news/depth/reply/content/root
        print('requestdata',request.data)
        ser = CreateCommentModelSerializer(data=request.data)
        if ser.is_valid():
            # 保存到数据库
            print('request.user',request.user.userID)
            ser.save(user_id= request.user.userID)
            # CommentRecord.objects.create(user=request.user)

            # 对新增到的数据值进行序列化(数据格式需要调整)
            news_id = ser.data.get('news')
            Video.objects.filter(videoID=news_id).update(comment_count=F('comment_count')+1)

            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
# *********************************点赞***********************************
class FavorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = classFavorRecord
        fields = ['news']
class FavorView(APIView):
    authentication_classes = [UserAuthentication,]
    def post(self,request,*args,**kwargs):
        ser = FavorModelSerializer(data=request.data)
        if not ser.is_valid():
            return Response({},status=status.HTTP_400_BAD_REQUEST)
        news_object = ser.validated_data.get('news')
        user_object = news_object.user
        print("user-pbject",user_object)
        queryset = classFavorRecord.objects.filter(user=request.user,news=news_object)
        exists = queryset.exists()
        if exists:
            queryset.delete()
            Video.objects.filter(videoID=news_object.videoID).update(like=F('like')-1)
            User.objects.filter(userID=user_object.userID).update(favored=F('favored')-1)
            print("qvxiaol")
            return Response({},status=status.HTTP_200_OK)
        classFavorRecord.objects.create(user=request.user,news=news_object)
        Video.objects.filter(videoID=news_object.videoID).update(like=F('like') + 1)
        User.objects.filter(userID=user_object.userID).update(favored=F('favored') + 1)
        return Response({},status=status.HTTP_201_CREATED)
#***************************收藏*********************
class collectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = classcollectRecord
        fields = ['news']


class CollectView(APIView):
    authentication_classes = [UserAuthentication,]
    def post(self,request,*args,**kwargs):
        ser = collectModelSerializer(data=request.data)
        if not ser.is_valid():
            return Response({},status=status.HTTP_400_BAD_REQUEST)
        news_object = ser.validated_data.get('news')
        user_object = news_object.user
        queryset = classcollectRecord.objects.filter(user=request.user,news=news_object)
        exists = queryset.exists()
        if exists:
            queryset.delete()
            print("qxlcloo")
            Video.objects.filter(videoID=news_object.videoID).update(collect=F('collect')-1)
            User.objects.filter(userID=user_object.userID).update(collected=F('collected')-1)
            return Response({},status=status.HTTP_200_OK)
        classcollectRecord.objects.create(user=request.user,news=news_object)
        Video.objects.filter(videoID=news_object.videoID).update(collect=F('collect') + 1)
        User.objects.filter(userID=user_object.userID).update(collected=F('collected') + 1)

        return Response({},status=status.HTTP_201_CREATED)

#*********************************二维码*******************************
from ..utils import wxcode2Session
def getwxcode(request,videoID):
    print('videpid',videoID)
    accsess_token = wxcode2Session.get_AccessToken()
    print("accstk",accsess_token)
    if accsess_token:
        accode_url = settings.getwxacunlim.format(accsess_token)

        secend = "videoID={}".format(videoID)
        prams = json.dumps({
            "scene":secend,
            "page":"pages/video/video",
            "check_path":False,
            "width":200
        })

        response = requests.post(url=accode_url,data=prams)  # 返回的是json数据
        return HttpResponse(response)
    else:
        return False
        # json_response = response.json()  # 把json数据转换为字典
        # print('jsonresponse', json_response)

        # if json_response.get('access_token'):
        #     return json_response
        # else:
        #     return False
