from django.db import models
import uuid
# Create your models here.

# 【重要】对数据库操作
'''用户信息'''
class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    avatar = models.CharField(verbose_name='头像', max_length=64, null=True,blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=64,default='cumter')
    tesuser = models.ForeignKey(verbose_name='正式用户',to='User',on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
class User(models.Model):
    userID = models.CharField(max_length=128, primary_key=True)
    password = models.CharField(max_length=128, null=False)
    nickname = models.CharField(max_length=128, null=True,verbose_name='昵称')
    academy = models.CharField(max_length=128, null=True,verbose_name='学院')
    major = models.CharField(max_length=128, null=True,verbose_name='专业')
    grade = models.CharField(max_length=128, null=True)
    sex = models.CharField(max_length=128, null=True,default="0")
    avatar = models.CharField(max_length=255, null=True)
    root = models.BooleanField(max_length=128, null=False, default=False)
    token = models.CharField(verbose_name='用户Token', max_length=64, null=True, blank=True,default=str(uuid.uuid4()))
    cared = models.IntegerField(verbose_name='关注数',null=False,default=0)
    favored = models.IntegerField(verbose_name='点赞数',null=False,default=0)
    collected = models.IntegerField(verbose_name='收藏数',null=False,default=0)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'


class Topic(models.Model):
    """
    主题
    """
    title = models.CharField(verbose_name='主题', max_length=32)
    count = models.PositiveIntegerField(verbose_name='关注度', default=0)

    class Meta:
        verbose_name = '学科'
        verbose_name_plural = '学科列表'


class Video(models.Model):
    videoID = models.IntegerField(primary_key=True)
    # academy = models.CharField(max_length=128,null=False,verbose_name='学院')
    # subject = models.CharField(verbose_name='课程',max_length=128,null=False)
    section = models.CharField(verbose_name='章节',max_length=128,null=False)
    # name = models.CharField(verbose_name='题目',max_length=128,null=False)
    content = models.TextField(verbose_name='内容',null=True)
    collect = models.IntegerField(verbose_name='收藏数',null=False,default=0)
    comment_count = models.IntegerField(verbose_name='评论数',null=False,default=0)
    like = models.IntegerField(verbose_name='点赞数',null=False,default=0)
    # file = models.CharField(verbose_name='文件路径',max_length=255, null=True)
    icon = models.CharField(verbose_name='封面路径',max_length=255, null=True)
    # owner = models.CharField(verbose_name='所有者',max_length=128,null=True)
    address = models.TextField(verbose_name='位置',null=True)
    createtime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    topic = models.ForeignKey(verbose_name='话题', to='Topic', null=True, blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='发布者', to='User', related_name='user',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程列表'



class class_detail(models.Model):
    key = models.CharField(verbose_name='TencentYun-File name',max_length=128,help_text='以后方便删除')
    cos_path = models.TextField(verbose_name='图片路径')
    videos = models.ForeignKey(verbose_name='课程', to='Video',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '视频/图片'
        verbose_name_plural = '腾讯云存储文件列表'



class classFavorRecord(models.Model):
    """
    课程赞记录表
    """
    news = models.ForeignKey(verbose_name='课程', to='Video',on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='点赞用户', to='User',on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name='点赞时间',auto_now_add=True)

    class Meta:
        verbose_name = '点赞记录'
        verbose_name_plural = '点赞记录'
class classcollectRecord(models.Model):
    """
    课程收藏记录表
    """
    news = models.ForeignKey(verbose_name='课程', to='Video', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='收藏用户', to='User', on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name='收藏时间',auto_now_add=True)

    class Meta:
        verbose_name = '收藏记录'
        verbose_name_plural = '收藏记录'

class like(models.Model):
    userID = models.CharField(max_length=128, null=False)
    videoID = models.IntegerField(null=False)

class CommentRecord(models.Model):
    """
    评论记录表
    """
    news = models.ForeignKey(verbose_name='动态', to='Video',on_delete=models.CASCADE)
    content = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(verbose_name='评论者', to='User',on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)

    reply = models.ForeignKey(verbose_name='回复', to='self', null=True, blank=True,related_name='replys',on_delete=models.CASCADE)
    depth = models.PositiveIntegerField(verbose_name='评论层级', default=1)
    root = models.ForeignKey(verbose_name='根评',to='self',null=True,blank=True,related_name='roots',on_delete=models.CASCADE)
    favor_count = models.PositiveIntegerField(verbose_name='赞数', default=0)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论列表'
class CommentFavorRecord(models.Model):
    """
    评论赞记录
    """
    comment = models.ForeignKey(verbose_name='动态', to='CommentRecord',on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='点赞用户', to='User',on_delete=models.CASCADE)

class Collect(models.Model):
    userID = models.CharField(max_length=128, null=False)
    videoID = models.IntegerField(null=False)


class Care(models.Model):
    userID = models.ForeignKey(verbose_name='主人',to='User',related_name='carebythis',on_delete=models.CASCADE)
    carewho = models.ForeignKey(verbose_name='被关注',to='User',related_name='thisbecared',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '关注'
        verbose_name_plural = '关注记录'

class ViewerRecord(models.Model):
    """
    浏览器记录
    """
    news = models.ForeignKey(verbose_name='动态', to='Video',on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='用户', to='User',on_delete=models.CASCADE)
    class Meta:
        verbose_name = '浏览记录'
        verbose_name_plural = '浏览记录'
# class news_detail(models.Model):
#     key = models.CharField(verbose_name='TencentYun-File name',max_length=128,help_text='以后方便删除')
#     cos_path = models.CharField(verbose_name='图片路径', max_length=128)
#     videos = models.ForeignKey(verbose_name='课程', to='Newstest',on_delete=models.CASCADE)
#
# class Newstest(models.Model):
#     """
#     动态
#     """
#     cover = models.CharField(verbose_name='封面', max_length=128)
#     content = models.CharField(verbose_name='内容', max_length=255)
#     topic = models.ForeignKey(verbose_name='话题', to='Topic', null=True, blank=True,on_delete=models.CASCADE)
#     address = models.CharField(verbose_name='位置', max_length=128, null=True, blank=True)
#
#     user = models.ForeignKey(verbose_name='发布者', to='User', related_name='news',on_delete=models.CASCADE)
#
#     favor_count = models.PositiveIntegerField(verbose_name='赞数', default=0)
#     # favor = models.ManyToManyField(verbose_name='点赞记录', to='UserInfo', related_name="news_favor")
#
#     viewer_count = models.PositiveIntegerField(verbose_name='浏览数', default=0)
#     # viewer = models.ManyToManyField(verbose_name='浏览器记录', to='UserInfo', related_name='news_viewer')
#
#     comment_count = models.PositiveIntegerField(verbose_name='评论数', default=0)
#
#     create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

"""
翻译成：
create table app名字_表名字(
    id bigint auto_increment primary key,
    name varchar(32),
    ...
    )
"""
