import xlrd
import xlwt
from xlutils.copy import copy

def config(f):
   file = 'config.ini'
   con = configparser.ConfigParser()

# 读取文件
   con.read(file, encoding='utf_16')

# 获取所有section
   sections = con.sections()
# ['url', 'email']


# 获取特定section
   items = con.items('参数') 	# 返回结果为元组
# [('baidu','http://www.baidu.com'),('port', '80')] 	# 数字也默认读取为字符串

# 可以通过dict方法转换为字典
   items = dict(items)
   s=items[f]
   return s
   
def wt(a,b,vl):#修改
   filename1=r"D:\python脚本\数据比对\11.xls"
   rb = xlrd.open_workbook(filename1)
   wb = copy(rb)

   s = wb.get_sheet(0)
   s.write(a,b,vl)
   wb.save(filename1)

filename=r"D:\python脚本\数据比对\11.xls"
filename2=r"D:\python脚本\数据比对\黄林1016.xls"

data = xlrd.open_workbook(filename)
data2 = xlrd.open_workbook(filename2)
table = data.sheets()[0]
table2 = data2.sheets()[0]
rows=table.row_values(0)

j=0
nrows = table.nrows
ncols = table.ncols
ncols2 = table2.ncols
nrows2 = table2.nrows
print(ncols)
q=0
#行列均从0开始计数
def sb(xx):
    zz='系统内重复人员.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx+'\n')
    f.close
def sb1(xx):
    zz='系统内重复人员1.txt'
    f=open(zz,"a",encoding='utf-8')
    f.write(xx+'\n')
    f.close
a=0
b=0
while 1:
    s=table.cell_value(j,11)#读取第j行，第一列
    k=0
    while 1:
        
        s1=table.cell_value(k,1)
        if s==s1:
            
            sb(table.cell_value(k,12))
            
            a=a+1
            break
        k=k+1
        if k==nrows2:#如果最后一行停止比对
           #print("ok!!!!!!!!!")
           rows=str(table.row_values(j))
            #print(rows)
           sb1(rows)
           b=b+1
           break
    j=j+1
    
    if j==nrows:#如果最后一行停止比对
        print("ok!!!!!!!!!")
        
        break


