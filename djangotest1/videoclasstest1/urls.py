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
