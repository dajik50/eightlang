from django.db import models
from loginAndreg.models import TotalUser
# Create your models here.
class UserLiuyan(models.Model):
    musci_liuyan = models.TextField(default='null')
    sport_liuyan = models.TextField(default='null')
    car_liuyan = models.TextField(default='null')
    movie_liuyan = models.TextField(default='null')
    food_liuyan = models.TextField(default='null')
    book_liuyan = models.TextField(default='null')
    create_time = models.DateTimeField(auto_now_add=True)
    totaluser = models.ForeignKey(TotalUser)

    class Meta:
        db_table = 'userliuyan'
