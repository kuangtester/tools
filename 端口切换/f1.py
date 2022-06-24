import os
import shutil
filelist=[]
rootdir=r"D:\1"                     
filelist=os.listdir(rootdir)              
for f in filelist:
   filepath = os.path.join( rootdir, f )   
   if os.path.isfile(filepath):
       os.remove(filepath)
       print(str(filepath)+" removed!")
   elif os.path.isdir(filepath):
       os.rmdir(filepath)
       print("dir "+str(filepath)+" removed!")
#shutil.rmtree(rootdir,True)                
print("删除成功")
