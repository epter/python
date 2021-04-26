import tkinter.ttk as ttk
import time
import tkinter.messagebox as msgbox

from tkinter import *

root = Tk()
root.title("route GUI")
root.geometry("640x480")

# btn1=Button(root, text="BTN1")
# btn2=Button(root, text="BTN2")

# # btn1.pack()
# # btn2.pack()

# # btn1.pack(side="left")
# # btn2.pack(side="right")
# btn1.grid(row=0,column=0)
# btn2.grid(row=1,column=1)

btn_f16 = Button(root, text="F16",padx=10, pady=10).grid(row=0,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_f17 = Button(root, text="F17",width=5, height=2).grid(row=0,column=1,sticky=N+E+W+S)
btn_f18 = Button(root, text="F18").grid(row=0,column=2,sticky=N+E+W+S)
btn_f19 = Button(root, text="F19").grid(row=0,column=3,sticky=N+E+W+S)


btn_clear = Button(root, text="clear").grid(row=1,column=0,sticky=N+E+W+S)
btn_equal = Button(root, text="=").grid(row=1,column=1,sticky=N+E+W+S)
btn_div = Button(root, text="/").grid(row=1,column=2,sticky=N+E+W+S)
btn_mul = Button(root, text="*").grid(row=1,column=3,sticky=N+E+W+S)


btn_7 = Button(root, text="7").grid(row=2,column=0,sticky=N+E+W+S)
btn_9 = Button(root, text="8").grid(row=2,column=1,sticky=N+E+W+S)
btn_9 = Button(root, text="9").grid(row=2,column=2,sticky=N+E+W+S)
btn_sub = Button(root, text="-").grid(row=2,column=3,sticky=N+E+W+S)


btn_4 = Button(root, text="4").grid(row=3,column=0,sticky=N+E+W+S)
btn_5 = Button(root, text="5").grid(row=3,column=1,sticky=N+E+W+S)
btn_6 = Button(root, text="6").grid(row=3,column=2,sticky=N+E+W+S)
btn_add = Button(root, text="+").grid(row=3,column=3,sticky=N+E+W+S)

btn_1 = Button(root, text="1").grid(row=4,column=0,sticky=N+E+W+S)
btn_2 = Button(root, text="2").grid(row=4,column=1,sticky=N+E+W+S)
btn_3 = Button(root, text="3").grid(row=4,column=2,sticky=N+E+W+S)
btn_enter = Button(root, text="enter").grid(row=4,column=3,rowspan=2,sticky=N+E+W+S)


btn_0 = Button(root, text="0").grid(row=5,column=0,columnspan=2,sticky=N+E+W+S)
btn_point = Button(root, text=".").grid(row=5,column=2,sticky=N+E+W+S)

root.mainloop()
