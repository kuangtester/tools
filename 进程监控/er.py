import requests
import json
import qrcode
import time,os,datetime
def create_dir_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)
def sb(xx):
    ss=os.path.dirname(os.path.realpath(__file__))+'\\log\\'
    if not os.path.exists(ss):
        os.mkdir(ss)
    today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    zz=ss+today+'.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx)
    f.close
def getcode():
    data = {
         "appkey":"",
         "account":"",
         "paytype":"1",
         "payacc":"###"
    }
    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}

    ## post的时候，将data字典形式的参数用json包转换成json格式。
    try:
        
        response = requests.post(url=, headers=headers, data=json.dumps(data))
        return response
    except:
        sb("+++++++++++连接失败")
def ru():
    
    s=getcode()
    #sb(s.text)
    state=json.loads(s.text).get('errmsg')
    if state=="操作成功":
        return False
    else:
        return False
    
    
