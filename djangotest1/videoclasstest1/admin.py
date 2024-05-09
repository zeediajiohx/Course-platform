from django.contrib import admin

from videoclasstest1.models import ViewerRecord, CommentRecord, User, Video, Topic,class_detail,classcollectRecord


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fields = ('userID','nickname', 'password','root')
    list_display = ['userID', 'nickname',  'root','academy','major']

    # 点击此字段可进行跳转详情页
    list_display_links = ['userID', 'nickname', 'root','academy','major']

    # 搜索字段
    search_fields = ['userID', 'nickname', 'avatar', 'root','academy','major','token']

    # 每页显示多少条记录
    list_per_page = 20

    # #不显示字段
    # exclude = ['is_virtual']

    # 侧边过滤器
    list_filter = ['nickname', 'root','academy','major']

class topicadmin(admin.ModelAdmin):
    fields = ('title','count')
    list_display = ['title']

    # 点击此字段可进行跳转详情页
    list_display_links = ['title']

    # 搜索字段
    search_fields = ['title']

    # 每页显示多少条记录
    list_per_page = 20

    # #不显示字段
    # exclude = ['is_virtual']

    # 侧边过滤器
    list_filter = ['title']

class classdetailinline(admin.TabularInline):
    model = class_detail
    verbose_name = '课程文件'
    verbose_name_plural = '课程文件'
    fields = ['key']

class classvideodetailinline(admin.StackedInline):
    model = class_detail
    verbose_name = '课程文件'
    verbose_name_plural = '课程文件'


class videoadmin(admin.ModelAdmin):
    fields = ['videoID','user','content','icon']
    list_display = ['videoID', 'createtime','content']

    # 点击此字段可进行跳转详情页
    list_display_links = ['videoID', 'createtime']

    # 搜索字段
    search_fields = ['videoID', 'createtime','user','content']

    # 每页显示多少条记录
    list_per_page = 20

    # #不显示字段
    # exclude = ['is_virtual']

    # 侧边过滤器
    list_filter = ['topic']

    inlines = [classdetailinline,classvideodetailinline]


class clsdetadmin(admin.ModelAdmin):
    fields = ('key','cos_path', 'videos')
    list_display = ['key','videos_id','videocontent','videoauther']

    # 点击此字段可进行跳转详情页
    list_display_links = ['key','videos_id','videocontent']

    # 搜索字段
    search_fields = ['key','videos']

    # 每页显示多少条记录
    list_per_page = 20

    # #不显示字段
    # exclude = ['is_virtual']

    # 侧边过滤器
    list_filter = ['videos']

    def videos_id(self,obj):
        return obj.videos.videoID
    def videocontent(self,obj):
        return obj.videos.content
    def videoauther(self,obj):
        return obj.videos.user.userID




class commenadmin(admin.ModelAdmin):
    fields = ('news', 'user','reply','depth','root','favor_count')
    list_display = ['news','user','create_date','reply','depth','root']

    # 点击此字段可进行跳转详情页
    list_display_links = ['news','user','create_date','reply','depth','root']

    # 搜索字段
    search_fields = ['user','news','create_date']

    # 每页显示多少条记录
    list_per_page = 20

    # #不显示字段
    # exclude = ['is_virtual']

    # 侧边过滤器
    list_filter = ['depth']

class viRecordadmin(admin.ModelAdmin):
    fields = ('news','user')
    list_display = ['news','user']

    # 点击此字段可进行跳转详情页
    list_display_links = ['news','user']

    # 搜索字段
    search_fields = ['news','user']

    # 每页显示多少条记录
    list_per_page = 20

class colRecorddadmin(admin.ModelAdmin):
    fields = ('news', 'user')
    list_display = ['news', 'user']

    # 点击此字段可进行跳转详情页
    list_display_links = ['news', 'user']

    # 搜索字段
    search_fields = ['news', 'user']

    # 每页显示多少条记录
    list_per_page = 20
    list_filter = ['create_date']
    # #不显示字段
    # exclude = ['is_virtual']

admin.site.register(User, ContactAdmin)
admin.site.register(Video,videoadmin)
admin.site.register(Topic,topicadmin)
admin.site.register(class_detail,clsdetadmin)
admin.site.register(CommentRecord,commenadmin)
admin.site.register(ViewerRecord,viRecordadmin)
admin.site.register(classcollectRecord,colRecorddadmin)


admin.site.site_header = '矿大小课堂后台管理系统'
