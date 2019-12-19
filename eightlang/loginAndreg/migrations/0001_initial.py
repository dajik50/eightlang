# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-17 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TotalUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=11, verbose_name='帐号')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('passwd', models.CharField(max_length=60, verbose_name='密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='用户创建时间')),
                ('music_fangwen', models.IntegerField(default=0, verbose_name='音乐频道访问次数')),
                ('car_fangwen', models.IntegerField(default=0, verbose_name='音乐频道访问次数')),
                ('sport_fangwen', models.IntegerField(default=0, verbose_name='音乐频道访问次数')),
                ('movie_fangwen', models.IntegerField(default=0, verbose_name='音乐频道访问次数')),
                ('book_fangwen', models.IntegerField(default=0, verbose_name='音乐频道访问次数')),
                ('food_fangwen', models.IntegerField(default=0, verbose_name='音乐频道访问次数')),
            ],
            options={
                'db_table': 'totaluser',
            },
        ),
    ]
