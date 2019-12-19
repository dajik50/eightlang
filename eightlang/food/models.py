from django.db import models


# Create your models here.
class Master(models.Model):
    pass


class Food(models.Model):
    name = models.CharField('菜名', max_length=50, null=False)
    point = models.IntegerField('点赞数', default=0, null=False)
    main_meal = models.CharField('主材', max_length=500, null=False)
    assist_meal = models.CharField('辅材', max_length=500, null=False)
    others = models.CharField('其他', max_length=500, null=False)
    food_method = models.CharField('做法', max_length=1000, null=False)
    image_name = models.CharField('图片', max_length=100)
    food_kind = models.CharField('菜系', max_length=20)

    def __str__(self):
        return '<%s %s %s %s %s %s %s %s>' % (
        self.name, self.point, self.main_meal, self.assist_meal, self.others, self.food_method, self.image_name,
        self.food_kind)

    class Meta:
        db_table = 'food'
