import tkinter.ttk as ttk
import time
import tkinter.messagebox as msgbox

from tkinter import *

root = Tk()
root.title("route GUI")
root.geometry("640x480")

Label(root, text="choice Menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

frame_burger = Frame(root, relief = "solid", bd =1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text = "burger").pack()
Button(frame_burger, text = "cheese burger").pack()
Button(frame_burger, text = "chicken burger").pack()

frame_drink = LabelFrame(root, text = "Drink")
frame_drink.pack(side="right",fill="both",expand =True)

Button(frame_drink, text="cola").pack()
Button(frame_drink, text="cider").pack()

root.mainloop()
