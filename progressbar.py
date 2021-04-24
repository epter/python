import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title("route GUI")
root.geometry("640x480")

# # progressbar = ttk.Progressbar(root, maximum=100, mode = "indeterminate") # repeat

# progressbar = ttk.Progressbar(root, maximum=100, mode = "determinate")
# progressbar.start(10) #10ms move
# progressbar.pack()


# def btncmd():
#     progressbar.stop()


# btn = Button(root,text="stop", command = btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150 , variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # wait 0.01s

        p_var2.set(i) #progrees bar set
        progressbar2.update() #ui update
        print(p_var2.get()) 


btn2 = Button(root, text = "start", command = btncmd2)
btn2.pack()

root.mainloop()
