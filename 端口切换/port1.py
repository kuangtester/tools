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
        time.sleep(60)
        os.system('cls')
        return True
    except:
        #
        nowtime1=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        sb(nowtime1+'break')
        print('%s:%d is unused' % (ip,int(port)))
        return False
if __name__ == '__main__':
    
    name='C:\\SynjonesSoft\\门禁考勤管理系统\\Web\\Page\\NewDoor\\NewWaterMonitor.aspx'
    name1='C:\\SynjonesSoft\\门禁考勤管理系统\\Web\\Web.config'
    while 1:
        print('stand by!!!!!')
        f=open("config.txt","rb")
        s=f.readline()
        line=f.readline()
        f.close
        i=0
        
        if net_is_used(int(s[1:-1]),ip='192.168.183.46')==False:
            #p=os.popen('C:\\Windows\\System32\\inetsrv\\appcmd.exe stop site 门禁考勤管理系统')
            time.sleep(10)   
            #sb(p.read()+'\n')
            #C:\Windows\System32\inetsrv\appcmd.exe stop site 网站名称
            #C:\Windows\System32\inetsrv\appcmd.exe start site 网站名称
            port.check_port(name,s[1:5],line[1:5])
            port.check_port(name1,s[1:5],line[1:5])
            f=open("config.txt",'r+',encoding='utf-8')
            f.seek(0)
            old=f.read()
            #替换后config配置
            str1='d'+str(line[1:5],encoding='utf-8')#line2
            str2='b'+str(s[1:5],encoding='utf-8')#line1
            #当前config配置
            str4='d'+str(s[1:5],encoding='utf-8')
            str5='b'+str(line[1:5],encoding='utf-8')
            #替换config备用端口
            str3=str1+'\n'+str2
            f.seek(0)
            f.truncate()
            f.write(str3)
            f.flush()
            f.close()
            print('change port is ok!!!!!!!!!!!!!!!!!')
            sb('change port is ok!!!!!!!!!!!!!!!!!\n')
            #p1=os.popen('C:\\Windows\\System32\\inetsrv\\appcmd.exe start site 门禁考勤管理系统')
            #sb(p1.read()+'\n')
            i=i+1
            nowtime3=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
            sb(nowtime3+'已切换端口'+str(i)+'次\n')
            print(nowtime3+'已切换端口'+str(i)+'次')
            time.sleep(1800)
            
        
        
