import datetime
import cx_Oracle
from faker import Faker
db = cx_Oracle.connect('system/123456@192.168.31.134:1521/ORCLCDB')
while 1:
    cursor = db.cursor()
    print(datetime.datetime.now())
    sql = "select * from cs;"
    cursor.execute(sql)
    print(cursor.fetchall())
    print(datetime.datetime.now())
