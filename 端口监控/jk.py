import socket
import time,os,datetime
#import port
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
def net_is_used(port,ip):
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s = socket.socket()
    
    try:
        s.connect((ip,int(port)))
        
        s.shutdown(1)
        nowtime=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        sb(nowtime+'open')
        print(nowtime+'  '+'%s:%d is used cheack again after 60 seconds' % (ip,int(port)))
        #time.sleep(60)
        os.system('cls')
        return True
    except:
        #
        nowtime1=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        sb(nowtime1+'break')
        print('%s:%d is unused' % (ip,int(port)))
        return False
i=0
while 1:
    nowtime=time.strftime('%H:%M:%S',time.localtime(time.time()))
    #print(nowtime)
    if nowtime[:2]=='10':
        if net_is_used('5572','192.168.1.244')==True:
            print("111")
            time.sleep(1)
       
