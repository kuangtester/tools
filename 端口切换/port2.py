import socket
import time,os,datetime
import port

def sb(xx):
    
    ss=os.path.dirname(os.path.realpath(__file__))+'\\log\\'
    today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    zz=ss+today+'.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx)
    f.close

def net_is_used(port,ip):
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s = socket.socket()
    try:
        s.connect((ip,port))
        
        s.shutdown(1)
        nowtime=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        print(nowtime+'  '+'%s:%d is used cheack again after 60 seconds' % (ip,int(port)))
        #time.sleep(60)
        os.system('cls')
        return True
    except:
        #
        #nowtime1=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        #sb(nowtime1+' break\n')
        #print('%s:%d is unused' % (ip,int(port)))
        return False
if __name__ == '__main__':
    while 1:
        nowtime=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        k=net_is_used('8000','192.168.240.194')
        if k==False:
            print(nowtime+' 192.168.240.194:8000 is unable')
            sb(nowtime)
            sb(' 192.168.240.194:8000 is unable\n')
        j=net_is_used('9999','192.168.240.205')
        if j==False:
            print(nowtime+' 192.168.240.205:9999 is unable')
            sb(nowtime)
            sb(' 192.168.240.205:9999 is unable\n')
        
        time.sleep(1)
        os.system('cls')
