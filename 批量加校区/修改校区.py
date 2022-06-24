import XG
import juzhong
from tkinter import *
import tkinter.filedialog
import os
if os.path.exists('log')==False:
    os.mkdir('log')
def xz():
    filename = tkinter.filedialog.askopenfilename()
    
    root = Tk()
    juzhong.jz(root)
    
    if filename != '':
        XG.xg(filename)
        lb=Label(root,text=filename+"\n修改完成！！！！");
        lb.pack(pady=200)
        
        #root.mainloop()
    else:
        lb=Label(root,text = "您没有选择任何文件");
root = Tk()
juzhong.jz(root)
btn = Button(root,text="请选择的要修改的文件：",command=xz)
btn.pack(pady=200)

root.mainloop()





