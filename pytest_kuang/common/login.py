import json

import requests
from config.settings import longin_url
from utils.mysqlutil import MysqlUtil


def login_for_session(user,passwd):
    header={
        "Content-Type": "application/x-www-form-urlencoded"
    }
    s={
        "name":user,
        "password":passwd
    }
    body={
        "json":json.dumps(s)
    }
    result=requests.request("post",longin_url,headers=header,data=body)
    result=result.json()
    return result["data"]["session"]
def query_mysql_data(sql):
    con=MysqlUtil()
    data=con.get_fetchall(sql)
    print(data["rec_id"])

if __name__ == '__main__':
    sql="select rec_id from ecs_cart order by rec_id limit 0,1"
    query_mysql_data(sql=sql)
