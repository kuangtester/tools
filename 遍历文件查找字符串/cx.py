import os
import time
def sb(xx):
    
    ss=os.path.dirname(os.path.realpath(__file__))+'\\log\\'
    if not os.path.exists(ss):
        os.mkdir(ss)
    today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    zz=ss+today+'.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx)
    f.close
def hassend(file,str1,count):
    with open(file,'rb') as f:
        
        lines = f.readlines()
        for line in lines:
            if line.strip().find(str.encode(str1))!=-1:
                #print('===================')
                count=count+1
                print(file)
                #print(count)
                sb(file)
                sb('\n')
                #time.sleep(60)


def file_name(file_dir,charname,count):
    #print('11')
    f_d=file_dir
    for dirpath,dirnames,filenames in os.walk(file_dir):
        for filename in filenames:
            hassend(os.path.join(dirpath,filename),charname,count)
            #print(os.path.join(dirpath,filename))
    #for root, dirs, files in os.walk(file_dir):
                #for f in files:ZP=>''
                    #print(f)
                    #hassend(file_dir+'\\'+f,'输入学工号')
            
    #return dirs
        

#f='D:\\python脚本\\遍历文件查找字符串\\webscreen0903'
count=0
f=input("请输入要查询的目录:")
while 1:
    c=input("请输入要查询的字符串：")
    dirs=file_name(f,c,count)

            


