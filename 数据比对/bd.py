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
   filename1=r"D:\python脚本\数据比对\1.xlsx"
   rb = xlrd.open_workbook(filename1)
   wb = copy(rb)

   s = wb.get_sheet(0)
   s.write(a,b,vl)
   wb.save(filename1)

filename=r"D:\python脚本\数据比对\1.xlsx"
filename2=r"D:\python脚本\数据比对\3.xlsx"

data = xlrd.open_workbook(filename)
data2 = xlrd.open_workbook(filename2)
table = data.sheets()[0]
table2 = data2.sheets()[0]
j=0
nrows = table.nrows
nrows2 = table2.nrows
#print(nrows)
#行列均从0开始计数
while 1:
    s=table.cell_value(j,0)#读取第j行，第一列
    k=0
    while 1:
        s1=table2.cell_value(k,0)
        if s==s1:
            #print(table.cell_value(k,1))
            wt(k,3,table.cell_value(k,1))#写入第k行，第4列
            break
        k=k+1
        if k==nrows2:#如果最后一行停止比对
        print("ok!!!!!!!!!")
        break
    j=j+1
    print(j)
    if j==nrows:#如果最后一行停止比对
        print("ok!!!!!!!!!")
        break
