import configparser

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
c=config('hang1')
print(c)
