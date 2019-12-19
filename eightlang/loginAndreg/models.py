from django.db import models

# Create your models here.
class TotalUser(models.Model):
    uname = models.CharField(verbose_name='帐号',max_length=11)
    nickname = models.CharField(verbose_name='昵称',max_length=32)
    passwd = models.CharField(verbose_name='密码',max_length=60)
    create_time = models.DateTimeField(verbose_name='用户创建时间',auto_now_add=True)
    music_fangwen = models.IntegerField(verbose_name='音乐频道访问次数',default=0)
    car_fangwen = models.IntegerField(verbose_name='音乐频道访问次数', default=0)
    sport_fangwen = models.IntegerField(verbose_name='音乐频道访问次数', default=0)
    movie_fangwen = models.IntegerField(verbose_name='音乐频道访问次数', default=0)
    book_fangwen = models.IntegerField(verbose_name='音乐频道访问次数', default=0)
    food_fangwen = models.IntegerField(verbose_name='音乐频道访问次数', default=0)
    class Meta:
        db_table = 'totaluser'

