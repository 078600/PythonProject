from pyzbar import pyzbar
import cv2
from tkinter import *
import os
from read import *

def load_image(photo_name):
    root= Tk()
    root.geometry("500x400+300+300")
    root.wm_iconbitmap('img1.ico')
    f=os.listdir("/karishma/project")
    root.title('Scanned QR Code')
    photo=PhotoImage(file=photo_name)
    label=Label(root,image=photo,width=600,height=350)
    label.pack(anchor=N)
    r=read(photo_name)
    label_1=Label(root,text="Employee details :{}".format(r),font=("System", 3), justify = 'left')
    label_1.pack(anchor=S)
    root.mainloop()
        
