import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# 将配置文件的路径写到 DJANGO_SETTINGS_MODULE 环境变量中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest1.settings")
django.setup()

from videoclasstest1 import models

models.ViewerRecord.objects.create(news_id=36,user_id="08181001",)
models.ViewerRecord.objects.create(news_id=36,user_id="08181002",)
models.ViewerRecord.objects.create(news_id=36,user_id="08181003",)
models.ViewerRecord.objects.create(news_id=36,user_id="08181004",)
models.ViewerRecord.objects.create(news_id=36,user_id="08181005",)
