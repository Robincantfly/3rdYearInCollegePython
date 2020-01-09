import tkinter as tk
import MYFUNC

window = tk.Tk()
window.title('数字与图像处理 结课程序 计算机161 陈田瀚')
window.geometry('900x900')

l=tk.Label(window,text='',bg='yellow')
l.pack()
counter=0
def do_job():
    global counter
    l.config(text='do '+str(counter))
    counter+=1
menubar=tk.Menu(window)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='打开图片',command=do_job)
filemenu.add_command(label='保存',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='关闭',command=window.quit)
editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='编辑',menu=editmenu)
editmenu.add_command(label='彩色图像灰度化',command=do_job)
editmenu.add_command(label='绘制灰度直方图',command=do_job)
editmenu.add_command(label='实现两幅相同大小图像相加',command=do_job)
editmenu.add_command(label='实现对数变换',command=do_job)
editmenu.add_command(label='实现 LoG 算子图像锐化',command=do_job)
editmenu.add_command(label='集成作业实现的 Otsu 图像分割',command=do_job)
submenu=tk.Menu(filemenu)
# filemenu.add_cascade(label='Import',menu=submenu,underline=0)
# submenu.add_command(label='Submenu1',command=do_job)
window.config(menu=menubar)


window.mainloop()

