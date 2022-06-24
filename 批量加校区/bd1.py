import xlrd
import xlwt
import os
import io
def bidui1(line):
         i=0
         j=0
         k=0
         for te in line:
             
             i=i+1
             if te=="*" :
                 #print(te)
                 k=i     
         name=line[0:k-1]
    
         return name
def bidui(line):
         i=0
         j=0
         k=0
         for te in line:
             
             i=i+1
             if te=="/" :
                 #print(te)
                 j=i
             if te=="*" :
                 #print(te)
                 k=i     
         name=line[j:k-1]
    
         return name
def sb(xx):
    
    
    
    zz='系统内重复人员.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx)
    f.close
def jieguo():
    
    z=0
    k=0
    a=0
    f=io.open("公安人事数据.txt","r",encoding='utf-8')
    line=f.readline()
    #print(line)
    while line:
         j=0
         n=bidui(line)
         
         f1=io.open("系统内人员.txt","r",encoding='utf-8')
         line1=f1.readline()
         while line1:
             m=bidui1(line1)
             #m=bidui(line1)
             
             if m==n:
                 
                 j=j+1
             line1=f1.readline()
         f1.close()
         if j>=2:
             #z=line
             #print(z)
             sb(str(line)+str(j))
             a=a+1
             print(a)
         line=f.readline()
         
    f.close()
    return a

z=jieguo()
print(z)








