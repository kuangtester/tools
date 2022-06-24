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
             if te=="$" :
                 #print(te)
                 j=i
             if te=="@" :
                 #print(te)
                 k=i     
         name=line[j:k-1]
    
         return name
def sb(xx):
    
    
    
    zz='xcf1.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx)
    f.close
def jieguo():
    
    z=0
    k=0
    a=0
    s=''
    f=io.open("b2.txt","r",encoding='utf-8')
    line=f.readline()
    #print(line)
    while line:
         j=2
         n=bidui(line)
         
         f1=io.open("b1.txt","r",encoding='utf-8')
         line1=f1.readline()
         #print(n)
         while line1:
             m=bidui(line1)
             #m=bidui(line1)
             #print(m)
             if str(m)==str(n):
                 print(m)
                 s=line1
                 sb(str(s[:-1])+"  "+str(line))
                 
                 break
             line1=f1.readline()
         f1.close()
        
             
         line=f.readline()
         
    f.close()
    return a

z=jieguo()
print(z)








