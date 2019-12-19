from django.db import models


# Create your models here.

class Author(models.Model):
    author = models.CharField('作者', max_length=100)
    age = models.IntegerField('年龄',default=0)
    sex = models.CharField('性别', max_length=100)
    magnum_opus = models.CharField('代表作', max_length=100)
    a_decs = models.TextField('作者简介')

    class Meta:
        db_table = 'author'


class Book(models.Model):
    name = models.CharField('书名', max_length=100)
    publish = models.CharField('出版社', max_length=100)
    a_decs = models.TextField('图书简介')
    sort = models.CharField('类别', max_length=50)
    content = models.TextField('内容')
    up_time = models.DateTimeField('上架时间')
    stow_number = models.IntegerField('收藏数', default=0)
    read_number = models.IntegerField('阅读数', default=0)
    imgs_src = models.CharField('图片地址', max_length=200)
    author = models.ForeignKey(Author)

    class Meta:
        db_table = 'book'
