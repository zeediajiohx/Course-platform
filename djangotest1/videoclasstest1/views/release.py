
from django.db.models import Max
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from ..models import Video,class_detail
from videoclasstest1.utils.auth import UserAuthentication
class credential(APIView):
    def get(self,requests,*args,**kwargs):
        from sts.sts import Sts
        from django.conf import settings
        config = {
            # 'url': 'https://sts.tencentcloudapi.com/',
            # # 域名，非必须，默认为 sts.tencentcloudapi.com
            # 'domain': 'sts.tencentcloudapi.com',
            # 临时密钥有效时长，单位是秒
            'duration_seconds': 1800,
            # 'secret_id': os.environ['COS_SECRET_ID'],
            'secret_id': settings.TENCENT_SECRET_ID,
            # 固定密钥
            # 'secret_key': os.environ['COS_SECRET_KEY'],
            'secret_key': settings.TENCENT_SECRET_KEY,
            # 设置网络代理
            # 'proxy': {
            #     'http': 'xx',
            #     'https': 'xx'
            # },
            # 换成你的 bucket
            'bucket': 'videotest1-1301605345',
            # 换成 bucket 所在地区
            'region': 'ap-nanjing',
            # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
            # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
            'allow_prefix': '*',
            # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
            'allow_actions': [
                # 简单上传
                # 'name/cos:PutObject',
                'name/cos:PostObject',
                'name/cos:DeleteObject',

                # 分片上传
                # 'name/cos:InitiateMultipartUpload',
                # 'name/cos:ListMultipartUploads',
                # 'name/cos:ListParts',
                # 'name/cos:UploadPart',
                # 'name/cos:CompleteMultipartUpload'
            ],

        }

        try:
            sts = Sts(config)
            response = sts.get_credential()
            # print('get data : ' + json.dumps(dict(response), indent=4))
            return Response(response)
        except Exception as e:
            print(e)

'''class_detail序列化器'''
# class clsdetaModelSerializer(serializers.Serializer):
#     key = serializers.CharField()
#     cos_path = serializers.CharField()
class clsdetModelSerializer(serializers.Serializer):
    key = serializers.CharField()
    cos_path = serializers.CharField()

class videoModelSerializer(serializers.ModelSerializer):
    # imageList = clsdetModelSerializer(many=True)
    videoList = clsdetModelSerializer(many=True)

    class Meta:
        model = Video
        exclude = ['videoID','user', 'like', 'collect','comment_count','section']

    def create(self, validated_data):
        # image_list = validated_data.pop('imageList')
        print("validata",validated_data)
        video_list = validated_data.pop('videoList')
        videoid =Video.objects.all().aggregate(Max('videoID')),
        print(videoid[0]['videoID__max'],'videoidd',type(videoid))
        news_object = Video.objects.create(**validated_data,videoID=videoid[0]['videoID__max']+1)
        # idata_list = class_detail.objects.bulk_create(
        #     [class_detail(**info, videos=news_object) for info in image_list]
        # )
        vdata_list = class_detail.objects.bulk_create(
            [class_detail(**info, videos=news_object) for info in video_list]
        )
        # news_object.imageList = idata_list
        news_object.videoList = vdata_list

        if news_object.topic:
            news_object.topic.count += 1
            news_object.save()

        return news_object


"""
    image = clsdetaModelSerializer(many=True)#[{cos_path:"http....",key:01xxxx.png},{cos_path:"http....",key:01xxxx.png},....]
    video = clsdetaModelSerializer(many=True)
    class Meta:
        model = Video
        # fields = "__all__"
        exclude = ['user','collect','like']
    def create(self, validated_data):
        # 去掉image
        image_list = validated_data.pop('image')
        #去掉video
        video_list = validated_data.pop('video')
        # 创建video表中的数据
        news_object = Video.objects.create(**validated_data)
        #批量创建classdetail
        imgdata_list = class_detail.objects.bulk_create(
            [class_detail(**info, videos=news_object) for info in image_list]
        )
        viddata_list = class_detail.objects.bulk_create(
            [class_detail(**info, videos=news_object) for info in video_list]
        )
        news_object.imageList = imgdata_list
        news_object.videoList = viddata_list

        if news_object.topic:
            news_object.topic.count += 1
            news_object.save()

        return news_object
"""

class videopvb(CreateAPIView):
    authentication_classes = [UserAuthentication,]

    # userid = request.user
    """创建视频"""
    serializer_class = videoModelSerializer
    # print(serializer_class.context['request'].user)

    def perform_create(self, serializer):
        user = self.request.user
        print('user',user)
        new_object = serializer.save(user_id=user.userID)#videoID=Video.objects.all().aggregate(Max('videoID'))["videoID__max"] + 1)
        return new_object


# class CreateNewsTopicModelSerializer(serializers.Serializer):
#     key = serializers.CharField()
#     cos_path = serializers.CharField()
#
#
# class CreateNewsModelSerializer(serializers.ModelSerializer):
#     imageList = CreateNewsTopicModelSerializer(many=True)
#
#     class Meta:
#         model = models.News
#         exclude = ['user', 'viewer_count', 'comment_count']
#
#     def create(self, validated_data):
#         image_list = validated_data.pop('imageList')
#         news_object = models.News.objects.create(**validated_data)
#         data_list = models.NewsDetail.objects.bulk_create(
#             [models.NewsDetail(**info, news=news_object) for info in image_list]
#         )
#         news_object.imageList = data_list
#
#         if news_object.topic:
#             news_object.topic.count += 1
#             news_object.save()
#
#         return news_object
# class newsdetaModelSerializer(serializers.Serializer):
#     key = serializers.CharField()
#     cos_path = serializers.CharField()
#
# class newsModelSerializer(serializers.ModelSerializer):
#     imageList = newsdetaModelSerializer(many=True)
#
#     class Meta:
#         model = Newstest
#         exclude = ['user', 'viewer_count', 'comment_count','favor_count']
#
#     def create(self, validated_data):
#         image_list = validated_data.pop('imageList')
#         news_object = Newstest.objects.create(**validated_data)
#         data_list = news_detail.objects.bulk_create(
#             [news_detail(**info, videos=news_object) for info in image_list]
#         )
#         news_object.imageList = data_list
#
#         if news_object.topic:
#             news_object.topic.count += 1
#             news_object.save()
#
#         return news_object
#
# class newspvb(CreateAPIView):
#     serializer_class = newsModelSerializer
#
#     def perform_create(self, serializer):
#         new_object = serializer.save(user_id='08181006')
#         return new_object

"""创建新视频
class CreateclsModelSerializer(serializers.ModelSerializer):
    images = clsdetaModelSerializer(
        many=True)  # [{cos_path:"http....",key:01xxxx.png},{cos_path:"http....",key:01xxxx.png},....]

    class Meta:
        moels = Video
        # fields = "__all__"
        # exclude = ['user','view_count','comment_count']
        exculde = ['user']

    def create(self,validated_data):
        imagelist = validated_data.pop('imagelist')
        news_object = Video.objects.create(**validated_data)
        .....
class Cratxls
"""

"""
class NewsView(CreateAPIView,ListAPIView):
    queryset = Video.objects.prefetch_related('user','topic').order_by(".id")
    filter_backends = [RechBottom,Pulldown]
    def ferfrom_create(self,serializer):
       new_obj = serializer.save(user_id=1)
       return new_obj
    def get_serrializer_class(self):
       if self.request.method == 'POST':
          return createnewsmocelserializer
       if self.request.method == 'GET':
          return ListNews....
"""
