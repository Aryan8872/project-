from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import font
 
root=Tk()
root.geometry("1920x1108")
root.config(bg="lavender")

def over_v():
    root.destroy()
    import overview

def rep():
    root.destroy()
    import report

def sts():
    root.destroy()
    import status


#top canvas
topcan=Canvas(root,height=80,width=1800,bg="black")
topcan.place(x=0,y=0)




#middle canvas
middle=Canvas(root,width=3,height=650,bg="black")
middle.place(x=930,y=90)

#bottom canvas
bottomcan=Canvas(root,height=50,width=1800,bg="black")
bottomcan.place(x=0,y=750)

 
#project title

title1=Label(root,text="MUNICIPAL",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title1.place(x=160,y=18)

title2=Label(root,text="PROBLEM",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title2.place(x=330,y=18)

title3=Label(root,text="RESOLVER",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title3.place(x=487,y=18)

#project logo
proj_logo=ImageTk.PhotoImage(Image.open("main_logo.png"))
logo_label=Label(root,image=proj_logo,bd=0,bg="black",height=70)
logo_label.place(x=640,y=5)

proj_logo2=ImageTk.PhotoImage(Image.open("second.png"))
logo_label2=Label(root,image=proj_logo2,bd=0,bg="black",height=60,width=150)
logo_label2.place(x=0,y=10)

myLable = Label(root,text="Welcome to MPR",font=("Colonna MT",30,"bold"),bg="Lavender",fg="deepskyblue2")
myLable.place(x=70,y=170)


myLable1 = Label(root,text="Familiar with MPR?",font=("Colonna MT",30,"bold"),bg="Lavender",fg="deepskyblue2")
myLable1.place(x=1000,y=170)

myLable2 = Label(root, text="Tell us how we can make ourselves better for you!",font=("Microsoft Uighur",20),bg="Lavender",fg="deepskyblue2")
myLable2.place(x=1000,y=280)

feedback_btn=Button(root,text="Feedback",bg="Lavender",activebackground="lavender",activeforeground="deepskyblue2",fg="deepskyblue2",font=("Microsoft Uighur",15))
feedback_btn.place(x=1100,y=550,width=190,height=47)


myLable2 = Label(root, text="MPR is a problem resolver site where we take in any of your municipal problems\nand forward them to respective authorities who will take action on it right away.",font=("Microsoft Uighur",20),bg="Lavender",fg="deepskyblue2")
myLable2.place(x=70,y=280)
getstart_btn=Button(root,text="Report",bg="Lavender",activebackground="lavender",activeforeground="deepskyblue2",fg="deepskyblue2",font=("Microsoft Uighur",15))
getstart_btn.place(x=150,y=500,width=190,height=47)


contact_btn=Button(root,text="Status",bg="Lavender",activebackground="lavender",activeforeground="deepskyblue2",fg="deepskyblue2",font=("Microsoft Uighur",15))
contact_btn.place(x=150,y=600,width=190,height=47)



def acc():
    import account_view

account=Button(root,text="ACCOUNT",font=("Helvetica 15 bold"),command=acc,bd=0,fg="blue",bg="black",activebackground="black")
account.place(x=1390,y=30)


root.mainloop()