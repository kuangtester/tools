import os

import io
def sb(xx):
    
    ss=os.path.dirname(os.path.realpath(__file__))+'\\log\\'
    
   
    f=open('ru.txt',"a",encoding='utf-8')
    f.write(xx)
    f.close
def bidui(name):
    f=io.open("2.txt","r",encoding='utf-8')
    line=f.readline()
    xb=''
    xb1=name
    while line:
         i=0
         for te in line:
             if te=="_" :
                 #print(te)
                 
                 school=line[0:i]
                 xb=line[i+1:-1]
                 #print(school)
                 #print(xb)
                 if school==name:
                     
                     break
             i=i+1
         if school==name:
                     print(xb)
                     break
         line=f.readline()   
    f.close()
    if school==name:
       return xb
f=io.open("1.txt","r",encoding='utf-8')
line=f.readline()
while line:
    #print(line[:-1])
    s=bidui(line[:-1])
    
    ss=str(line[:-1])+','+str(s)+'\n'
    sb(ss)
    print(ss)
    line=f.readline()
        





    
