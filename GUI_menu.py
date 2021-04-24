import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title("route GUI")
root.geometry("640x480")

def create_new_file():
    print("create new file")

menu = Menu(root)

#file menu
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label = "New window")
menu_file.add_separator()
menu_file.add_command(label="open file...")
menu_file.add_separator
menu_file.add_command(label="save all",state="disable") #button disable
menu_file.add_separator
menu_file.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="file", menu=menu_file)

#edit menu
menu.add_cascade(label="Edit")

#add lan menu

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="JAVA")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu =menu_lang)

#add view menu
menu_view = Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="show mimimap")
menu.add_cascade(label="view", menu=menu_view)

root.config(menu=menu)
root.mainloop()
