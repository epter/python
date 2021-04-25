import tkinter.ttk as ttk
import time
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("route GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("allert","successfully Ticketting")

def warn():
    msgbox.showwarning("warning","Sold Out")

def error():
    msgbox.showerror("error","Payment Error")

def okcancel():
    msgbox.askokcancel("OK / Cancel", "Infant companion seat")

def retrycancel():
    msgbox.askretrycancel("retry / Cancel", "Temporary error")

def yesno():
    msgbox.askyesno("Yes / No", "this seat is reverse")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Not Saved\nwould you like to save it?")
# 네 : 저장 후 종료/ 아니요 : 저장하지 않고 종류 / 취소: 종료 취소
    print("response",response)
    if response == 1:
        print("yes")
    elif response == 0:
        print("NO")
    else:
        print("cancel")

        

Button(root, command=info, text="allert").pack()

Button(root, command=warn, text="warning").pack()

Button(root, command=error, text="Error").pack()

Button(root, command=okcancel, text="Verification is cancel").pack()

Button(root, command=retrycancel, text="retrycancel").pack()

Button(root, command=yesno, text="yes no").pack()


Button(root, command=yesnocancel, text="yes no cancel").pack()

root.mainloop()
