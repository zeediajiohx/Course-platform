import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# 将配置文件的路径写到 DJANGO_SETTINGS_MODULE 环境变量中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest1.settings")
django.setup()

from videoclasstest1 import models
for i in range(4,7):
    models.User.objects.create(
        userID='66632700853667{0}'.format((i+1000)),
        nickname='professor-{0}'.format(i),
        avatar='http://www.cumt.edu.cn/_upload/article/16/07/f625226441e7b7bd316688880442/5f51029d-cf63-48b6-81a0-bd3bdf2201c3.jpg',
        password = '223344',
        academy = '计算机',
        major = '大数据',
        grade='2018',
        sex='male',
        root=True
    )
