# import os
# import sys
# import django
# from videoclasstest1 import models
#
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(base_dir)
# #将配置文件的路径写入DJANGO_SETTINGS_MODULE 环境变量中
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","djangotest1.settings")
# django.setup()
#
# models.UserInfo.objects.create(name='胡图图',password='123')
# models.UserInfo.objects.create(name='美羊羊',password='123')


"""
初始化动态表，在动态表中添加一些数据，方便操作
"""
import os
import sys
import django
from django.db.models import Max

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest1.settings")
django.setup()

from videoclasstest1 import models

# for i in range(1,37):
#     news_object = models.Video.objects.create(
#         videoID=i,
#         icon="https://s2.loli.net/2022/03/05/CG9tcsXEFeIVgzl.png",
#         content="还有{0}天就开学".format(i),
#         topic_id=1,
#         user_id='08181000',
#
#     )
#
#     models.class_detail.objects.create(
#         key="08a9daei1578736867828.png",
#         cos_path="https://s2.loli.net/2022/03/04/jAvGFXEMYoCgzkh.png",
#         videos=news_object
#     )
#
#     models.class_detail.objects.create(
#         key="0d3q0evq1578906084254.jpg",
#         cos_path="https://s2.loli.net/2022/03/04/WHh4IzM1QFwe3sX.png",
#         videos=news_object
#     )
iconlist = ['https://s2.loli.net/2022/04/09/fCrxv2tE4wRAKNF.png','https://s2.loli.net/2022/04/09/CzkwcblZefKSj5y.png','https://s2.loli.net/2022/03/08/kjNQzJKcZ2bplCH.png','https://s2.loli.net/2022/03/04/jAvGFXEMYoCgzkh.png','https://s2.loli.net/2022/03/04/WHh4IzM1QFwe3sX.png']
iconlist2=['https://sm.ms/image/psWfYABlvbk94TF','https://sm.ms/image/yEAumJC9P6kFvsx','https://s2.loli.net/2022/04/28/bf82S45ilz6rmne.png','https://s2.loli.net/2022/04/28/uJ1ta4EkBf6nqX7.png','https://s2.loli.net/2022/04/28/SZ1LBErq9MThPty.png','https://sm.ms/image/bexDk1KNVhPoZLj','https://sm.ms/image/sZ9aYtGz4RnCl8W','https://sm.ms/image/S35JreGsnqpfVg8','https://sm.ms/image/3hNRKgoPLADGV1y','https://sm.ms/image/UZDvNCkHmIn5sWx','https://sm.ms/image/otK9cxYaEzLRseT','https://sm.ms/image/vcQfLlOK98JzHnw','https://sm.ms/image/Ky6kUlTbG4mjIfO','https://sm.ms/image/AyGU512osHBZwI8','https://sm.ms/image/OHbKMpGPr4vglYe']
for i in range(3,4):
    print("videoid",models.Video.objects.all().aggregate(Max('videoID')))
    news_object = models.Video.objects.create(
        videoID= models.Video.objects.all().aggregate(Max('videoID'))["videoID__max"] + 1,

    # videoID=i,
        icon=iconlist2[i-1],
        content="么全部失败回滚。回滚可以用回滚日志（Undo Log）来实现，回滚日志记录着事务所执行的修改操作，在回滚时反向执行这些修改操作即可。",
        topic_id=i,
        user_id='666327008536671004',

    )

    models.class_detail.objects.create(
        key="0a4bpecg1650301354531.mp4",
        cos_path="https://klxxcdn.oss-cn-hangzhou.aliyuncs.com/histudy/hrm/media/bg2.mp4",
        videos=news_object
    )


