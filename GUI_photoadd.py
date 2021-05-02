from tkinter import *
import os
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image
root = Tk()
root.title("route GUI")

#file add fun
def add_file():
    files = filedialog.askopenfilenames(title = "choice image file", filetypes=(("png file","*.png"), ("all file", "*.*")), initialdir="C:/")

    for file in files:
        list_file.insert(END, file)
#del fun
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
#save path
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, folder_selected)

#image merge
def merge_image():
    #가로 넓이
    img_width = cmb_width.get()
    if img_width == "원본 유지":
        img_width = -1 #-1일때는 원본 기준
    else:
        img_width = int(img_width)

    #간격
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 30
    elif img_space == "보통":
        img_space = 60
    elif img_space == "넓게":
        img_space = 90
    else: #None
        img_space = 0

    #format
    img_format = cmb_format.get().lower()

    #############################option

    images = [Image.open(x) for x in list_file.get(0,END)]

    #image size list
    image_sizes = []
    if img_width > -1:
        image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
    else:
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    
    widths, heights = zip(*(image_sizes))

    #maximum
    max_width, total_height = max(widths), sum(heights)

    #sketchbook ready
    if img_space > 0:
        total_height += (img_space * (len(images) - 1))

    result_img = Image.new("RGB", (max_width, total_height),(255,255,255))
    y_offset = 0 # y position
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1]

    for idx, img in enumerate(images):
        if img_width > -1:
            img = img.resize(image_sizes[idx])

        result_img.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_space)

        progress = (idx +1) / len(images) * 100 # real percent info
        p_var.set(progress)
        progress_bar.update()

    #format option
    file_name = "route_photo." + img_format
    dest_path = os.path.join(txt_dest_path.get(), file_name)
    result_img.save(dest_path)
    msgbox.showinfo("info", "complete")





#start btn
def start():
    if list_file.size()== 0:
        msgbox.showwarning("Warning", "add image file")
        return
    
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "choice save path")
        return

    #image integrated
    merge_image()


#file frame
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5,pady=5)

btn_add_file = Button(file_frame, padx=5,pady=5,width=12, text="file add", command = add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5,pady=5,width=12, text ="select del", command = del_file)
btn_del_file.pack(side="right")
#list frame
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5,pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame, selectmode="extended", height =15,yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#save path frame
path_frame = LabelFrame(root, text ="path")
path_frame.pack(fill="x",padx=5,pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,padx=5,pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="look for", width = 10, command = browse_dest_path)
btn_dest_path.pack(side ="right",padx=5,pady=5)

#option frame
frame_option = LabelFrame(root, text="option")
frame_option.pack(padx=5,pady=5)

#1 width option
lbl_width = Label(frame_option, text="width", width=8)
lbl_width.pack(side="left",padx=5,pady=5)

#combo
opt_width = ["origin","1024","800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",values=opt_width,width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5,pady=5)

#2 interval

lbl_space = Label(frame_option, text="interval", width=8)
lbl_space.pack(side="left",padx=5,pady=5)
#combo
opt_space = ["None","Narrow","Normal","wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly",values=opt_space,width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5,pady=5)

#3 format
lbl_format = Label(frame_option, text="interval", width=8)
lbl_format.pack(side="left",padx=5,pady=5)
#combo
opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly",values=opt_format,width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5,pady=5)

#progress bar
frame_progress = LabelFrame(root,text="progress")
frame_progress.pack(fill="x")

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")

#frame run
frame_run = Frame(root)
frame_run.pack(fill="x",padx=5,pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="close", width=12,command=root.quit)
btn_close.pack(side="right",padx=5,pady=5)

btn_start = Button(frame_run, padx=5,pady=5,text="start",width=12, command =start)
btn_start.pack(side="right",padx=5,pady=5)


root.resizable(False, False) # 리사이즈 변경 권한 x,y
root.mainloop()
