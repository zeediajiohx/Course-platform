import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
list = ['政治','计算机','物理','化学','材料','土木','金融','管理','建筑','环境','人文','体育','其他']
# 将配置文件的路径写到 DJANGO_SETTINGS_MODULE 环境变量中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest1.settings")
django.setup()

from videoclasstest1 import models
for item in list:
    models.Topic.objects.create(title=item)
# models.Topic.objects.create(title="PV操作")
