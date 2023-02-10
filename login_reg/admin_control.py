from tkinter import *
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.geometry("1920x1108")


#top canvas
topcan=Canvas(root,height=80,width=1800,bg="black")
topcan.place(x=0,y=0)


frame1=LabelFrame(root,width=1100,height=690,bg="lavender")
frame1.place(x=0,y=80)


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


#Entering problem solved username
Labe1=Label(frame1,text="# ENTER PROBLEM RESOLVED USER'S USERNAME",font=("Helvetica 15 bold"))
Labe1.place(x=60,y=40)

#username label
un_label=Label(frame1,text="Username",font=("Helvetica 13 bold"))
un_label.place(x=60,y=90)

#username entry
un_entry=Entry(frame1,font=("Helvetica 11 bold"))
un_entry.place(x=60,y=120)

#progress
pg=Label(frame1,text="#Progress",font=("Helvetica 13 bold"))
pg.place(x=60,y=160)

#progress entry
pg_entry=Entry(frame1,font=("Helvetica 11 bold"))
pg_entry.place(x=60,y=190)

#progress indicator
blue=Label(frame1,bg="blue",text="BLUE",font=("Helvetica 11 bold"))
blue.place(x=350,y=200)

blue_mean=Label(frame1,text="--REPORT RECEIVED",font=("Helvetica 9 bold"))
blue_mean.place(x=430,y=200)

red=Label(frame1,text="RED",bg="red",font=("Helvetica 11 bold"))
red.place(x=350,y=240)

red_mean=Label(frame1,text="--HELP IS ON THE WAY",font=("Helvetica 9 bold"))
red_mean.place(x=430,y=240)

green=Label(frame1,text="GREEN",bg="green",font=("Helvetica 11 bold"))
green.place(x=350,y=280)

green_mean=Label(frame1,text="--HELP IS ON THE WAY",font=("Helvetica 9 bold"))
green_mean.place(x=430,y=280)

def change():
    conn=sqlite3.connect("feedback.db")
    c=conn.cursor()
    c.execute("""UPDATE feedback SET
            problem_status= :sts
            WHERE user_name= :un""",
            {
                'un':un_entry.get(),
                'sts':pg_entry.get()
            })
    conn.commit()
    conn.close()
    messagebox.showinfo("success","Submitted sucessfully!")

change_btn=Button(frame1,text="Change",font=("Helvetica 9 bold"),command=change)
change_btn.place(x=60,y=220)
root.mainloop()