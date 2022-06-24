import psutil
import os,time
import configparser
import socket,er
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
def judgeprocess(processname):
    pl = psutil.pids()
    list1=[]
    for pid in pl:
        j=0
        if psutil.Process(pid).name() == processname:
            sb(str(pid))
            j=j+1
            list1.append(pid)
    return list1

    
def net_is_used(port,ip):
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s = socket.socket()
    port=8999
    try:
        s.connect((ip,port))
        
        s.shutdown(3)
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
def kill_pid(pid):
    find_kill = 'taskkill -f -pid %s' % pid
    print(find_kill)
    result = os.popen(find_kill)
    print(result)

def confi(s,o):
    path=config.read('config.ini')
    path1=config.get(s, o)
    return path1
j=0
config = configparser.ConfigParser()
while 1:
    nowtime=time.strftime('%H:%M:%S',time.localtime(time.time()))
    #i=os.system("cls")
    print(nowtime[:2])
    l="QQ.exe"
    list1=judgeprocess(l)

    k=len(list1)
    print(k)
    if er.ru()==False:
        
        path1=confi('config','path')
        print(path1)
        #path=r'C:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe'
        os.startfile(path1)
        time.sleep(2)
        list2=judgeprocess(l)
        z=len(list2)
        print(list2)
        if z>=1:
            print("进程重启成功")
        time.sleep(3600)
    
    print('success')
    time.sleep(3)

