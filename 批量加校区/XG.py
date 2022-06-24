import xlrd
import xlwt
import bidui
import datetime
import os
import xlutils
def gettime():
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return now_time
def sb(xx):
    
    ss=os.path.dirname(os.path.realpath(__file__))+'\\log\\'
    
    zz=ss+gettime()+'.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx)
    f.close
def xg(file):
    from xlutils.copy import copy
    i=0  
    workbook = xlrd.open_workbook(file)
    #workbook1 = xlwt.Workbook(file)
    wb=copy(workbook)
    ws = workbook.sheet_by_index(0)
    rowNum = ws.nrows
    ws1=wb.get_sheet(0)
    #x=int(ws.cell_value(0,0)) # 获取第四行内容
    #c=ws.col_values(6) # 获取第三列内容
    while 1:
       
        if i==rowNum:
            break
        temp=ws.cell_value(i,4)
        
        #j=0
        #for te in temp:
                
                #if te=="/" :
                   # school=temp[0:j+1]
                    #xb=temp[j+1:]
                    
                #j=j+1
        
        tem=bidui.bidui(temp)
        if tem==None:
            print(str(temp)+'：没有对应校区请添加\n')
            #sb(temp+'：没有对应校区请添加\n')
            
        
        
        if tem!=None:
            ws1.write(i,4,tem)
            wb.save(file)
        print(i)
        i=i+1
    
    
    
    
   

   
