from tkinter import *
import tkinter.filedialog

root = Tk()


lb = Label(root,text = '')
lb.pack()
btn = Button(root,text="弹出选择文件对话框")
btn.pack()
root.mainloop()
