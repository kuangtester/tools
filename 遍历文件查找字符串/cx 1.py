import os
import time
import threading
def sb(xx):
    
    ss=os.path.dirname(os.path.realpath(__file__))+'\\log\\'
    if not os.path.exists(ss):
        os.mkdir(ss)
    today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    zz=ss+today+'.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx)
    f.close
def hassend(file,str1):
    with open(file,'rb') as f:
        
        lines = f.readlines()
        for line in lines:
            if line.strip().find(str.encode(str1))!=-1:
                #print('===================')
                #print(file)
                sb(file)
                sb('\n')
                #time.sleep(60)


def file_name(file_dir,charname):
    #print('11')
    f_d=file_dir
    for dirpath,dirnames,filenames in os.walk(file_dir):
        for filename in filenames:
            hassend(os.path.join(dirpath,filename),charname)
            #print(os.path.join(dirpath,filename))
    #for root, dirs, files in os.walk(file_dir):
                #for f in files:
                    #print(f)
                    #hassend(file_dir+'\\'+f,'输入学工号')
            
    #return dirs
        

#f='D:\\python脚本\\遍历文件查找字符串\\webscreen0903'
f=input("请输入要查询的目录:")
c=input("请输入要查询的字符串：")
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        dir=file_name(f,c)
        # 释放锁，开启下一个线程
        threadLock.release()
threadLock = threading.Lock()
threads = []
def dxc():
    
    

   
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    thread3 = myThread(3, "Thread-3", 3)
    thread4 = myThread(4, "Thread-4", 4)

    # 开启新线程
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    threads.append(thread4)

    # 等待所有线程完成
    for t in threads:
        t.join()
    print ("退出主线程")
print(time.ctime(time.time()))
dxc()
#dir=file_name(f,c)
print(time.ctime(time.time()))

            


