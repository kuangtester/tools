import psutil
import os,time
import configparser
import unicode

def judgeprocess(processname):
    pl = psutil.pids()
    list1=[]
    for pid in pl:
        j=0
        if psutil.Process(pid).name() == processname:
            
            j=j+1
            list1.append(pid)
    return list1


 
conf= configparser.ConfigParser()
def readConf(option):
    '''读取配置文件'''
    #root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf.read('config.ini')  # 文件路径
    
    name = conf.get("config", option)  # 获取指定section 的option值
    
    return name



while 1:
    nowtime=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
    #i=os.system("cls")
    l=readConf('name')
    list1=judgeprocess(l)
    k=len(list1)
    if k==0:
        exepath=readConf('path')
        #exepath=unicode(exepath, 'utf8').encode('gbk')
        os.popen(exepath)
        print("已重启进程"+l)
    print('success')
    print("sleep 10 s ")
    break
    time.sleep(10)
    os.system("cls")

