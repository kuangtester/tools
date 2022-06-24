import time
import os
# 打印时间戳
def sb(xx):
    
    ss=os.path.dirname(os.path.realpath(__file__))+'\\log\\'
    today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    zz=ss+today+'.txt'
    f=open(zz,"a+",encoding='utf-8')
    lines = f.readlines()
    print(lines)
    f.write(xx)
    f.write("\n")
    f.close
while 1:
    
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    sb(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    
    time.sleep(30)
    print('ok')
    os.system('cls')
