import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("route GUI")

root.geometry("640x480")

values = [str(i) + "day" for i in range(1,32)] #1~31 in the number
combobox = ttk.Combobox(root, height = 5, values =values) # height = index 5
combobox.pack()
combobox.set ("card payment day") #combobox in the text

#read only ver

# values = [str(i) + "day" for i in range(1,32)] #1~31 in the number
# readonly_combobox = ttk.Combobox(root, height = 10, values =values, state = "readonly") 
# readonly_combobox.current(0) # no 0 choice 
# readonly_combobox.pack()



def btncmd():
    print(combobox.get())
    # print(readonly_combobox.get())

btn = Button(root,text="choice", command = btncmd)
btn.pack()

root.mainloop()
