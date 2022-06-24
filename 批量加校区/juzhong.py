def jz(xx):
    sw =xx.winfo_screenwidth()
    #得到屏幕宽度
    sh =xx.winfo_screenheight()
    #得到屏幕高度
    ww = 500
    wh = 500
    #窗口宽高为100
    x = (sw-ww) / 2
    y = (sh-wh) / 2
    xx.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
    xx.title("批量添加校区工具")
    
    
