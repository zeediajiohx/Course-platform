from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from django.forms import model_to_dict
from django.db.models import F
from videoclasstest1.models import User,Video,classFavorRecord,classcollectRecord,class_detail,ViewerRecord,CommentRecord,Care
from videoclasstest1.utils.auth import UserAuthentication
class clsvidModelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()
    # key = serializers.SerializerMethodField()
    class Meta:
        model = Video
        fields = ['videoID','icon','content','topic','user','like','collect']
    def get_user(self,obj):
        return model_to_dict(obj.user,fields=['userID','nickname','avatar'])
        # return {'id':obj.user_id,'nickname':obj.user.name,'avater':obj.user.avatar}
    def get_topic(self,obj):
        if not obj.topic:
            return
        return {'id':obj.topic_id,'title':obj.topic.title}

class deleclassDetailModelserializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    createtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    user = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()
    viewer = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    is_favor = serializers.SerializerMethodField()
    is_collect = serializers.SerializerMethodField()

    class Meta:
        model = Video
        # fields="__all__"
        exclude = ['icon']
    def get_images(self,obj):
        detailqueryset = class_detail.objects.filter(videos=obj)
        # return [row.cos_path for row in detail_queryset]
        # return [{'id':row.id,'path':row.cos_path} for row in detail_queryset]
        return [model_to_dict(row, ['id', 'cos_path','key']) for row in detailqueryset]
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

#*****************************课程列表***************************
class myclasscotns(APIView):
    authentication_classes = [UserAuthentication,]

    def get(self,request,*args,**kwargs):
        min_id = request.query_params.get('min_id')
        max_id = request.query_params.get('max_id')

        if min_id:
            # queryset = Video.objects.filter(user=request.user)

            queryset = Video.objects.filter(user=request.user,videoID__lt=min_id).order_by('-videoID')[0:10]
        elif max_id:
            queryset = Video.objects.filter(videoID__gt=max_id,user = request.user).order_by('videoID')[0:10]
        else:
            queryset = Video.objects.filter(user = request.user).order_by('-videoID')[0:10]
        print('myquryst',queryset)
        ser = clsvidModelSerializer(instance=queryset,many=True)
        return Response(ser.data,status=200)

class optclsvidModelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    topic = serializers.SerializerMethodField()
    # key = serializers.SerializerMethodField()
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


class favorclasscontns(APIView):
    authentication_classes = [UserAuthentication, ]

    def get(self, request, *args, **kwargs):
        min_id = request.query_params.get('min_id')
        max_id = request.query_params.get('max_id')

        # if min_id:
        #     favorqueryset = classFavorRecord.objects.filter(user=request.user, create_date__lt=min_id).order_by('-create_date')[
        #                     0:10]
        # elif max_id:
        #     favorqueryset = classFavorRecord.objects.filter(user=request.user, create_date__gt=max_id).order_by('create_date')[
        #                     0:10]
        # else:
        favorqueryset = classFavorRecord.objects.filter(user=request.user).order_by('-create_date')
        favernews = []
        for row in favorqueryset:
            favernews.append(row.news_id)
        quereset = Video.objects.filter(videoID__in=favernews)
        print('qurest',quereset)
        ser = optclsvidModelSerializer(instance=quereset, many=True)
        return Response(ser.data, status=200)

class collectclasscontns(APIView):
    authentication_classes = [UserAuthentication, ]

    def get(self, request, *args, **kwargs):
        # min_id = request.query_params.get('min_id')
        # max_id = request.query_params.get('max_id')
        # # collectqueryset = classcollectRecord.objects.filter(user= request.user)
        #
        # if min_id:
        #     favorqueryset = classcollectRecord.objects.filter(user=request.user, news__lt=min_id).order_by('-news')[
        #                     0:10]
        # elif max_id:
        #     favorqueryset = classcollectRecord.objects.filter(user=request.user, news__gt=max_id).order_by('news')[
        #                     0:10]
        # else:
        favorqueryset = classcollectRecord.objects.filter(user=request.user).order_by('-create_date')[0:10]
        collectnews = []
        for row in favorqueryset:
            collectnews.append(row.news_id)
        quereset = Video.objects.filter(videoID__in=collectnews)
        # if min_id:
        #
        #     # queryset = Video.objects.filter(user=request.user)
        #
        #     queryset = Video.objects.filter(videoID=collectqueryset.videoID, videoID__lt=min_id).order_by('-videoID')[0:10]
        # elif max_id:
        #     queryset = Video.objects.filter(videoID__gt=max_id, user=request.user).order_by('videoID')[0:10]
        # else:
        #     queryset = Video.objects.filter(videoID = collectqueryset.videoID,user=request.user).order_by('-videoID')[0:10]
        ser = optclsvidModelSerializer(instance=quereset, many=True)
        return Response(ser.data, status=200)



class deleteclassDetailView(RetrieveAPIView):
    lookup_field = 'videoID'
    queryset = Video.objects
    serializer_class = deleclassDetailModelserializer
#     添加用户访问记录
    def get(self,request, *args,**kwargs):

        response = super().get(request, *args,**kwargs)
        if not request.user:
            return response
        # 获取请求头中的token
        # 判断当前用户是否有访问此新闻的记录？
        news_object = self.get_object() # models.News.objects.get(pk=pk)
        exists = ViewerRecord.objects.filter(user=request.user,news=news_object).exists()
        if exists:
            return response
        ViewerRecord.objects.create(user=request.user,news=news_object)
        # News.objects.filter(id=news_object.id).update(viewer_count=F('viewer_count')+1)

        return response



# class deleteserialize(serializers.Serializer):
#
#
# class deleteclass(APIView):
#     authentication_classes = [UserAuthentication,]
#     def post(self,request,*args,**kwargs):

# *************************点关注***************************************
class careModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Care
        fields = ['carewho']


class careView(APIView):
    authentication_classes = [UserAuthentication,]
    def post(self,request,*args,**kwargs):
        ser = careModelSerializer(data=request.data)
        if not ser.is_valid():
            return Response({},status=status.HTTP_400_BAD_REQUEST)
        cared_object = ser.validated_data.get('carewho')
        queryset = Care.objects.filter(userID=request.user,carewho=cared_object)
        exists = queryset.exists()
        if exists:
            queryset.delete()
            print("qxlcloo")
            User.objects.filter(userID=cared_object.userID).update(cared=F('cared')-1)
            return Response({},status=status.HTTP_200_OK)
        Care.objects.create(userID=request.user,carewho=cared_object)
        User.objects.filter(userID=cared_object.userID).update(cared=F('cared') + 1)
        return Response({},status=status.HTTP_201_CREATED)

#***************************被赞、关注**************************************
class getfavcolcareserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['cared','favored','collected']

class getfavorview(APIView):
    authentication_classes = [UserAuthentication,]
    def get(self,request,*args,**kwargs):
        berelatedqueryset = User.objects.filter(userID=request.user.userID)
        print('qurest', berelatedqueryset)
        ser = getfavcolcareserializer(instance=berelatedqueryset,many=True)
        print("serfavo",ser.data)
        return Response(ser.data, status=200)
