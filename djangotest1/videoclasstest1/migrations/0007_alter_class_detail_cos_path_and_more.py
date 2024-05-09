# Generated by Django 4.0.1 on 2022-04-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoclasstest1', '0006_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_detail',
            name='cos_path',
            field=models.TextField(max_length=128, verbose_name='图片路径'),
        ),
        migrations.AlterField(
            model_name='commentrecord',
            name='content',
            field=models.TextField(max_length=255, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='7175b744-3080-4b39-9cf5-ddbb86e299d9', max_length=64, null=True, verbose_name='用户Token'),
        ),
        migrations.AlterField(
            model_name='video',
            name='address',
            field=models.TextField(null=True, verbose_name='位置'),
        ),
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.TextField(max_length=128, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.CharField(max_length=255, null=True, verbose_name='文件路径'),
        ),
        migrations.AlterField(
            model_name='video',
            name='icon',
            field=models.CharField(max_length=255, null=True, verbose_name='封面路径'),
        ),
    ]