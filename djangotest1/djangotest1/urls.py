"""djangotest1 URL Configuration
URL和函数的对应关系，常常用
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from videoclasstest1.views import views,login,video,register,release,topic,myrecord
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('userlist/',views.user_list),
    path('test/',views.test),
    path('getsth/',views.getsth),
    path('login/',views.LoginView.as_view()),
    path('message/',views.messview.as_view()),
    path('login/pic/code/',login.showcode),
    path('regist/pic/code/',register.showcode),
    path('user/login/',login.logins),
    path('video/wxcode/<int:videoID>/',video.getwxcode),
    # path('class/upload/',video.video),
    # 登录
    path('user/register/',register.register),
    # 首页的课程
    path('index/class/',video.classcotns.as_view()),
    # 视频详细页面
    path('classdetail/<int:videoID>/', video.classDetailView.as_view()),
    # 临时密钥
    path('credential/',release.credential.as_view()),
    # 发布视频
    path('class/release/',release.videopvb.as_view()),
    # path('news/release/', release.newspvb.as_view()),
    path('video/topic/',topic.TopicView.as_view()),
    path('login/manager/',login.managerlogin.as_view()),
    path('login/user/',login.userlogin.as_view()),
    path('video/comment/',video.CommentView.as_view()),
    path('class/dofavor/',video.FavorView.as_view()),
    path('class/docollect/',video.CollectView.as_view()),
    path('record/my/',myrecord.myclasscotns.as_view()),
    path('record/favor/',myrecord.favorclasscontns.as_view()),
    path('record/collect/',myrecord.collectclasscontns.as_view()),
    path('user/getinfo/',login.getuserinfo.as_view()),
    path('index/videoselect/',video.selectedclasscotns.as_view()),
    path('user/caresbd/',myrecord.careView.as_view()),
    path('user/relatednumrecord/',myrecord.getfavorview.as_view()),
    path('video/careauthclass/',video.careclasscotns.as_view()),
    path('video/careclassselect/',video.careselectedclasscotns.as_view())
    # path('video/videolist/',video)

]

