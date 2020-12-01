# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()

from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
content = Frame(root)
frame = Frame(content, width=800, height=400)
l1F=Frame(content, width=400, height=50)
l2F=Frame(content, width=400, height=50)
# root.geometry("850x600+600+450")
# root.resizable(width=True, height=True) 
filename=""
def openfn():
    global filename
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    l1F.grid(row=1,column=0,rowspan=3,columnspan=2)
    panel = Label(l1F, image=img)
    panel.image = img
    w = Label(l1F, text="Input Image")
    w.grid(row=0,column=0,columnspan=2)
    panel.grid(row = 1, column = 0, sticky = W,columnspan = 2, rowspan = 2, padx = 5, pady = 5)
    perform_arithmetic_coding()

def open_img_and_reset():
    reset_btn()
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    l1F.grid(row=1,column=0,rowspan=3,columnspan=2)
    panel = Label(l1F, image=img)
    panel.image = img
    w = Label(l1F, text="Input Image")
    w.grid(row=0,column=0,columnspan=2)
    panel.grid(row = 1, column = 0, sticky = W,columnspan = 2, rowspan = 2, padx = 5, pady = 5)
    perform_arithmetic_coding()

def perform_arithmetic_coding():
    x = filename
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    l2F.grid(row=1,column=2,rowspan=3,columnspan=2)
    panel = Label(l2F, image=img)
    panel.image = img
    w = Label(l2F, text="OutPut image")
    w.grid(row=0,column=0,columnspan=2)
    panel.grid(row = 1, column = 0,columnspan = 2, rowspan = 2, padx = 5, pady = 5)
    b1['text']="Reset and browse new image"  
def reset_btn():
    l1F.destroy()
    l2F.destroy()

b1=Button(content, text='Browse image', command=open_img)
content.grid(row=0,column=0)
frame.grid(column=0, row=0, columnspan=4, rowspan=4)
b1.grid(row = 0, column = 0,columnspan = 4, rowspan = 1, pady = 5)

root.mainloop()