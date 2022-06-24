import xlrd
import xlwt
import os
import io
def bidui():
    f=io.open("1.txt","r", encoding='utf-8')
    line=f.readline()
    
    
    print(line)
    while line:
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
                 print(name)
        line=f.readline()
        
        
      
    f.close()
    
z=bidui()

