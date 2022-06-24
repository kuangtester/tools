import xlrd
import xlwt
import os
import io
def bidui(name):
    f=io.open("school.txt","r",encoding='utf-8')
    line=f.readline()
    xb=''
    xb1=name
    while line:
         i=0
         
         for te in line:
             
             
             if te=="/" :
                 #print(te)
                 
                 school=line[0:i+1]
                 xb=line[i+1:-1]
                 
                 if xb==name:
                     
                     break
             i=i+1
         if xb==name:
                     
                     break
         line=f.readline()
         
        
        
      
    f.close()
    if xb==name:
        
       return school+xb



