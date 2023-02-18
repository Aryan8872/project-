from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkcalendar import DateEntry

overview=Tk()
overview.geometry("1920x1108")
overview.config(bg="lavender")



def rep():
    overview.destroy()
    import report

def sts():
    overview.destroy()
    import status

def feedbck():
    overview.destroy()
    import feedback

def acc():
    overview.destroy()
    import account_view


#top canvas
topcan=Canvas(overview,height=80,width=1800,bg="black")
topcan.place(x=0,y=0)

#middle canvas
middle=Canvas(overview,width=3,height=650,bg="black")
middle.place(x=930,y=90)

#bottom canvas
bottomcan=Canvas(overview,height=50,width=1800,bg="black")
bottomcan.place(x=0,y=750)

 
#project title

title1=Label(overview,text="MUNICIPAL",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title1.place(x=160,y=18)

title2=Label(overview,text="PROBLEM",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title2.place(x=330,y=18)

title3=Label(overview,text="RESOLVER",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title3.place(x=487,y=18)

#project logo
proj_logo=ImageTk.PhotoImage(Image.open("images\\main_logo.png"))
logo_label=Label(overview,image=proj_logo,bd=0,bg="black",height=70)
logo_label.place(x=640,y=5)

proj_logo2=ImageTk.PhotoImage(Image.open("images\\second.png"))
logo_label2=Label(overview,image=proj_logo2,bd=0,bg="black",height=60,width=150)
logo_label2.place(x=0,y=10)

myLable = Label(overview,text="Welcome to MPR",font=("Colonna MT",30,"bold"),bg="Lavender",fg="deepskyblue2")
myLable.place(x=70,y=170)


myLable1 = Label(overview,text="Familiar with MPR?",font=("Colonna MT",30,"bold"),bg="Lavender",fg="deepskyblue2")
myLable1.place(x=1000,y=170)

myLable2 = Label(overview, text="Tell us how we can make ourselves \n better for you!",font=("Microsoft Uighur",20),bg="Lavender",fg="deepskyblue2")
myLable2.place(x=1000,y=280)

feedback_btn=Button(overview,text="Feedback",bg="Lavender",activebackground="lavender",activeforeground="deepskyblue2",fg="deepskyblue2",font=("Microsoft Uighur",15),command=feedbck)
feedback_btn.place(x=1100,y=550,width=190,height=47)


myLable2 = Label(overview, text="MPR is a problem resolver site where we take in any of your \n municipal problems and forward them to respective \n authorities who will take action on it right away.",font=("Microsoft Uighur",20),bg="Lavender",fg="deepskyblue2")
myLable2.place(x=70,y=280)
report_button=Button(overview,text="Report",bg="Lavender",activebackground="lavender",activeforeground="deepskyblue2",fg="deepskyblue2",font=("Microsoft Uighur",15),command=rep)
report_button.place(x=150,y=500,width=190,height=47)


status_button=Button(overview,text="Status",bg="Lavender",activebackground="lavender",activeforeground="deepskyblue2",fg="deepskyblue2",font=("Microsoft Uighur",15),command=sts)
status_button.place(x=150,y=600,width=190,height=47)






account=Button(overview,text="ACCOUNT",font=("Helvetica 15 bold"),command=acc,bd=0,fg="blue",bg="black",activebackground="black")
account.place(x=1390,y=30)


overview.mainloop()