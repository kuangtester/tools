import os
import time
from win32com.client import Dispatch


def refreash(path_file):
    os.system('taskkill /IM EXCEL.exe /F')    # 杀死正在执行的excel程序,慎用，可不用
    xlapp = Dispatch('Excel.Application')
    xlapp.visible = 1
    wkb = xlapp.Workbooks.open(path_file)
    wkb.RefreshAll()
    time.sleep(20)                           # 如果表格中刷新时间过长，或者有很多计算，建议沉睡一会
    wkb.Save()
    wkb.Close(1)
    xlapp.quit()
    print('自动更新结束')

if __name__ == '__main__':
    path_file = r'E:\测试\ceshi.xlsx'
    refreash(path_file)
