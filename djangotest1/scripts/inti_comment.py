import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest1.settings")
django.setup()

from videoclasstest1 import models

# ########################## 创建三条根评论 ##########################
first1 = models.CommentRecord.objects.create(
    news_id=42,
    content="7-好吧",
    user_id="08181006",
    depth=1,
    # videoID='0'
)

first1_1 = models.CommentRecord.objects.create(
    news_id=42,
    content="7-1-非常喜欢",
    user_id="08181001",
    reply=first1,
    depth=2,
    root=first1
)

first1_1_1 = models.CommentRecord.objects.create(
    news_id=42,
    content="9-1-1-美",
    user_id="08181009",
    reply=first1_1,
    depth=3,
    root=first1
)
first1_1_2 = models.CommentRecord.objects.create(
    news_id=42,
    content="8-1-2-他们说的对",
    user_id="08181003",
    reply=first1_1,
    depth=3,
    root=first1
)


first1_2 = models.CommentRecord.objects.create(
    news_id=42,
    content="9-2",
    user_id="08181003",
    reply=first1,
    depth=2,
    root=first1
)


first2 = models.CommentRecord.objects.create(
    news_id=42,
    content="2022",
    user_id="08181009",
    depth=1
)

first3 = models.CommentRecord.objects.create(
    news_id=42,
    content="307-耶",
    user_id="08181008",
    depth=1
)
