from PIL import Image, ImageDraw, ImageFont
import PIL.Image
image = Image.new('RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import pyqrcode
import csv 
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
from tkinter import messagebox
from fun import *

root =tk.Tk()
root.title('ID Card Generator')
root.geometry("500x400+300+300")
root.configure(background="light blue")
root.wm_iconbitmap('img1.ico')
l1=ttk.Label(root,text="ID Card Generator",font=("Tahoma", 25, 'bold'),background='light blue')
l1.grid(row=0,column=0,sticky=tk.W,pady = (5,5))

com=ttk.Label(root,text="Company Name:",font=("System", 3),background='light blue')
com.grid(row=2,column=0,sticky=tk.W,pady = (5,5))


# adding an unique id number. 
(x, y) = (600, 75)
idno=random.randint(1,1000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)



emp=ttk.Label(root,text="Empolyee Name:",font=("System", 3),background='light blue')
emp.grid(row=4,column=0, sticky=tk.W,pady = (5,5))


#create radiobutton
usertype=tk.StringVar()

lbl=ttk.Label(root,text="Gender",font=("System", 3),background='light blue')
lbl.grid(row=6,column=0, sticky=tk.W)
gen1=ttk.Radiobutton(root,text='Male',value='Male',variable=usertype)
gen2=ttk.Radiobutton(root,text='Female',value='Female',variable=usertype)
gen1.grid(row=6,column=1, sticky=tk.W)
gen2.grid(row=6,column=3, sticky=tk.W)



age=ttk.Label(root,text="Age:",font=("System", 3),background='light blue')
age.grid(row=8,column=0, sticky=tk.W,pady = (5,5))


dob=ttk.Label(root,text="Date of birth:",font=("System", 3),background='light blue')
dob.grid(row=10,column=0, sticky=tk.W,pady = (5,5))

blood=ttk.Label(root,text="Blood:",font=("System", 3),background='light blue')
blood.grid(row=12,column=0, sticky=tk.W,pady = (5,5))

mobile=ttk.Label(root,text="Mobile Number:",font=("System", 3),background='light blue')
mobile.grid(row=14,column=0, sticky=tk.W,pady = (5,5))


city=ttk.Label(root,text="City:",font=("System", 3),background='light blue')
city.grid(row=16,column=0, sticky=tk.W,pady = (5,5))

#creating entrybox
com_var=tk.StringVar()
com_box=ttk.Entry(root,width=16,textvariable=com_var)
com_box.grid(row=2,column=1, sticky=tk.W)

emp_var=tk.StringVar()
emp_box=ttk.Entry(root,width=16,textvariable=emp_var)
emp_box.grid(row=4,column=1, sticky=tk.W)

age_var=tk.StringVar()
age_box=ttk.Entry(root,width=16,textvariable=age_var)
age_box.grid(row=8,column=1, sticky=tk.W)

dob_var=tk.StringVar()
dob_box=ttk.Entry(root,width=16,textvariable=dob_var)
dob_box.grid(row=10,column=1, sticky=tk.W)

blood_var=tk.StringVar()
blood_box=ttk.Entry(root,width=16,textvariable=blood_var)
blood_box.grid(row=12,column=1, sticky=tk.W)

mob_var=tk.StringVar()
num_box=ttk.Entry(root,width=16,textvariable=mob_var)
num_box.grid(row=14,column=1, sticky=tk.W)

city_var=tk.StringVar()
city_box=ttk.Entry(root,width=16,textvariable=city_var)
city_box.grid(row=16,column=1, sticky=tk.W)


def action():
    company=com_var.get()
    employee=emp_var.get()
    gender=usertype.get()
    age=age_var.get()
    birth=dob_var.get()
    blood=blood_var.get()
    mobile=mob_var.get()
    city=city_var.get()

    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=80)
    draw.text((50,50),company, fill=color, font=font)

    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((50,250),employee, fill=color, font=font)

    (x, y) = (50, 350)
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y),blood, fill=color, font=font)

    (x, y) = (50, 450)
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y),mobile, fill=color, font=font)

    image.save(str(employee)+'.png')

    with open('emp_details.csv','a+') as file:
        writer=csv.writer(file)
        if os.stat('emp_details.csv').st_size==0:
            writer.writerow(['ID','Company Name','Emp_Name','Gender','Age','DOB','Blood_Group','Mobile','City'])
        writer.writerow([idno,company,employee,gender,age,birth,blood,mobile,city])

    emp_box.delete(0,tk.END)
    com_box.delete(0,tk.END)
    age_box.delete(0,tk.END)
    dob_box.delete(0,tk.END)
    blood_box.delete(0,tk.END)
    num_box.delete(0,tk.END)
    city_box.delete(0,tk.END)
  
    data=f'''

        Company Name: {company} \n
        Emp_Name: {employee} \n
        Mobile: {mobile} \n
        Blood Group:{blood}\n 
        Age : {age}\n
        DOB : {birth}\n
        City : {city} \n
        '''

    img= pyqrcode.create(data)
    img.png(f"{employee}_{idno}.png",scale='3')
        
    til = PIL.Image.open(employee+'.png')
    im = PIL.Image.open(f"{employee}_{idno}.png") #25x25
    til.paste(im,(600,350))
    til.save(employee+'.png')
    messagebox.showinfo("Information","ID Card Successfully created "+f"{employee}.png")

    #print(('\n\n\nYour ID Card Successfully created in a PNG file '+employee+'.png'))
def call():
    root.destroy()
    root1 =tk.Tk()
    root1.title('ID Card Generator')
    root1.geometry("500x400+300+300")
    l1=ttk.Label(root1,text="ID Card Scanner",font=("Tahoma", 25, 'bold'),background='light blue')
    l1.grid(row=0,column=3)
    root1.configure(background="light blue")
    root1.wm_iconbitmap('img1.ico')

    code=ttk.Label(root1,text="Enter Your ID :",font=("System", 3),background='light blue')
    code.grid(row=1,column=3,sticky=tk.W,pady = (5,5))

    n=ttk.Label(root1,text="Enter Your Name :",font=("System", 3),background='light blue')
    n.grid(row=2,column=3,sticky=tk.W,pady = (5,5))

    n_var=tk.StringVar()
    n_box=ttk.Entry(root1,width=16,textvariable=n_var)
    n_box.grid(row=2,column=4, sticky=tk.W)

    code_var=tk.StringVar()
    code_box=ttk.Entry(root1,width=16,textvariable=code_var)
    code_box.grid(row=1,column=4, sticky=tk.W)


    def qr():
        name=n_var.get()
        c=code_var.get()
        root1.destroy()
        f=os.listdir("/karishma/project")
        print("you are in folder")
        img_file = "{name}_{c}.png".format(name=name, c=c)
        load_image(img_file)

    s=ttk.Button(root1,text="Scan",command=qr)
    s.grid(row=3,column=2, sticky=tk.W)

    root.mainloop()
      

    
sub=ttk.Button(root,text="Submit",command=action)
sub.grid(row=18,column=1, sticky=tk.W)


scn=ttk.Button(root,text="Scan",command=call)
scn.grid(row=22,column=1, sticky=tk.W)
