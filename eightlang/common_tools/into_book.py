import pymysql
import re
import datetime
db = pymysql.connect(host='localhost',
                     passwd='123456',
                     port=3306,
                     user='root',
                     charset='utf8',
                     database='eightlang')

cur = db.cursor()
sql2 = 'insert into author (id,author,age,sex,magnum_opus,a_decs) values (%s,%s,%s,%s,%s,%s)'
with open('./author.txt','r+') as f:
    for i in f:
        s = eval(i)
        cur.execute(sql2,s)
        db.commit()

        print(i)

sql = 'insert into book (id,name,publish,a_decs,sort,content,up_time,stow_number,read_number,imgs_src,author_id ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

with open('./book.txt','r+') as f:
    for i in f:
        s = eval(i)

        cur.execute(sql,s)
        db.commit()

        print(i)
