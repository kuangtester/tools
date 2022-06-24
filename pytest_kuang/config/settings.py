import os

DB_CONFIG = {"host": "192.168.174.133",
             "user": "root",
             "password": "123456",
             "database": "ecshop",
             "port": 3306,
             "charset": "utf8"}
base_url="http://shop.ecmobile.cn"
longin_url=f"{base_url}/ecmobile/?url=/user/signin"
addcart_url=f"{base_url}/ecmobile/?url=/cart/create"
# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)
# 获取文件所在目录的上一级目录,也就是根目录
jwproject_path = os.path.dirname(os.path.dirname(abs_path))
# 通过os.sep的方法来获取log日志目录的全路径
jwconf_path= jwproject_path + os.sep + "log"
#获取yaml文件全路径
yamlpath=jwproject_path+os.sep+"testdata"
# 返回日志目录
def get_log_path():
    return jwconf_path


# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)
# print(abs_path)
# 获取文件所在目录的上一级目录,也就是根目录
jwproject_path = os.path.dirname(os.path.dirname(abs_path))
# print(project_path)
# 通过os.sep的方法来获取config目录的全路径
jwconf_path = jwproject_path + os.sep + "config"
# 通过os.sep的方法来获取log日志目录的全路径
jwconf_path= jwproject_path + os.sep + "log"
# 通过os.sep的方法来获取report报告目录的全路径
jwreport_path = jwproject_path + os.sep + "report"


# 返回日志目录
def get_log_path():
    return jwconf_path
# 返回报告目录
def get_report_path():
    return jwconf_path
# 返回config目录
def get_config_path():
    return jwconf_path

# 占位用，勿删除
class DynamicParam:
    pass


# 测试代码
if __name__ == '__main__':
    print(get_log_path())