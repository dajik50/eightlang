import pymysql
import re
db = pymysql.connect(host='localhost',
                     passwd='123456',
                     port=3306,
                     user='root',
                     charset='utf8',
                     database='eightlang')

cur = db.cursor()


sql = 'insert into food (id,name,point,main_meal,assist_meal,others,food_method,image_name,food_kind) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

with open('./foodfile.txt','r+') as f:
    for i in f:
        s = eval(i)
        try:
            cur.execute(sql,s)
            db.commit()
        except:
            db.rollback()
        print(i)
