from rest_framework import  serializers


class UserInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="id",read_only=True)
    name = serializers.CharField(label="姓名",max_length=32)
    password = serializers.CharField(label="密码",max_length=64)



"""
#定义序列化器（转换，校验）
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
#视图集（增删改查流程封装）
class UserinfoViewset(ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()

#url.py
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

from videoclasstest1.views import views,login
urlpatterns = [
    path('','')

]

router = DefaultRouter()
router.register(r'users',views.UserInfoSerializer,basename="Users")
urlpatterns+=router.urls

"""
