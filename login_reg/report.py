from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import font
from tkinter import filedialog
 
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


#buttons
#overviewBUtton
def on_enter(e):
   overview.config(background='black', foreground= "red")

def on_leave(e):
   overview.config(background= 'black', foreground= 'white')

overview=Button(root,text="OVERVIEW",font=("Helvetica 15 bold"),bg="black",command=over_v,fg="white",bd=0)
overview.place(x=890,y=30)

overview.bind('<Enter>', on_enter)
overview.bind('<Leave>', on_leave)

#ReportButton
def on_enter(e):
   report.config(background='black', foreground= "white")

def on_leave(e):
   report.config(background= 'black', foreground= 'red')

report=Button(root,text="REPORT",font=("Helvetica 15 bold"),bg="black",fg="red",command=rep,bd=0)
report.place(x=1050,y=30)

report.bind('<Enter>', on_enter)
report.bind('<Leave>', on_leave)

#StatusButton
def on_enter(e):
   status.config(background='black', foreground= "red")

def on_leave(e):
   status.config(background= 'black', foreground= 'white')
status=Button(root,text="STATUS",font=("Helvetica 15 bold"),bg="black",fg="white",command=sts,bd=0)
status.place(x=1200,y=30)

status.bind('<Enter>', on_enter)
status.bind('<Leave>', on_leave)


rep_frame=LabelFrame(root,width=1920,height=1100,bg="lavender")
rep_frame.place(x=0,y=80)


#middle canvas
middle=Canvas(rep_frame,width=3,height=470,bg="black")
middle.place(x=740,y=100)

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
proj_logo=ImageTk.PhotoImage(Image.open("images\\main_logo.png"))
logo_label=Label(root,image=proj_logo,bd=0,bg="black",height=70)
logo_label.place(x=640,y=5)

proj_logo2=ImageTk.PhotoImage(Image.open("images\\second.png"))
logo_label2=Label(root,image=proj_logo2,bd=0,bg="black",height=60,width=150)
logo_label2.place(x=0,y=10)


#report here
report_label=Label(rep_frame,text="REPORT",fg="deepskyblue2",bg="lavender",font=("Helvetica 35 bold"))
report_label.place(x=650,y=0)

date_sel=Label(rep_frame,text="Date:",fg="deepskyblue2",bg="lavender",font=("Helvetica 25 bold"))
date_sel.place(x=1300,y=50)

cal=DateEntry(rep_frame,selectmode='day')
cal.place(x=1300,y=100)



name=Label(rep_frame,text="Name of the reporter:-",fg="deepskyblue2",bg="lavender",font=("Helvetica 25 bold"))
name.place(x=80,y=100)

fn=Label(rep_frame,text="First Name",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
fn.place(x=80,y=180)

fn_entry=Entry(rep_frame,fg="black",bg="white",bd=0,font=("Helvetica 15 bold"))
fn_entry.place(x=80,y=210)

ln=Label(rep_frame,text="Last Name",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
ln.place(x=360,y=180)

ln_entry=Entry(rep_frame,fg="black",bd=0,font=("Helvetica 15 bold"))
ln_entry.place(x=360,y=210)

locat=Label(rep_frame,text="Location:",fg="deepskyblue2",bg="lavender",font=("Helvetica 25 bold"))
locat.place(x=830,y=100)

ward=Label(rep_frame,text="Ward No.:",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
ward.place(x=830,y=180)

ward_entry=Entry(rep_frame,fg="black",bd=0,font=("Helvetica 15 bold"))
ward_entry.place(x=830,y=210)

tole=Label(rep_frame,text="Tole:",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
tole.place(x=1100,y=180)

tole_entry=Entry(rep_frame,fg="black",bd=0,font=("Helvetica 15 bold"))
tole_entry.place(x=1100,y=210)

issue=Label(rep_frame,text="Issues Related to:",fg="deepskyblue2",bg="lavender",font=("Helvetica 20 bold"))
issue.place(x=80,y=300)

#dropbox
options=[
    "Garbage",
    "Homeless",
    "Road",
    "Managment",
    "Other"
]
click=StringVar()
click.set("Garbage")
drop=OptionMenu(root,click,*options)
drop.place(x=80,y=450)
drop.config(width=25,background='deepskyblue2',foreground="lavender",font=("Helvetica 14 bold"))


level=Label(rep_frame,text="Level of severity:",fg="deepskyblue2",bg="lavender",font=("Helvetica 20 bold"))
level.place(x=830,y=280)


sev = StringVar()
sev.set(" ")

def clicked():
    global sevr
    sevr=sev.get()
Radiobutton(rep_frame,text="Low",font=('Ariel', 17),fg="deepskyblue2",background="lavender",variable=sev,value="LOW",command=clicked).place(x=830,y=330)
Radiobutton(rep_frame,text="Moderate",font=('Ariel', 17),fg="deepskyblue2",background="lavender",variable=sev,value="MODERATE",command=clicked).place(x=940,y=330)
Radiobutton(rep_frame,text="Critical",font=('Ariel', 17),fg="deepskyblue2",background="lavender",variable=sev,value="CRITCIAL",command=clicked).place(x=1100,y=330)

descp=Label(rep_frame,text="Descriptive Explanation",fg="deepskyblue2",background="lavender",font=("Helvetica 20 bold"))
descp.place(x=830,y=400)

box=Text(rep_frame,width=50,height=6,bg="white",font=("Ariel 13 bold"))
box.place(x=830,y=450)



def acc():
    import account_view

account=Button(root,text="ACCOUNT",font=("Helvetica 15 bold"),command=acc,bd=0,fg="blue",bg="black",activebackground="black")
account.place(x=1390,y=30)








conn=sqlite3.connect('report.db')
c=conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS rep(
        first_name text,
        last_name text,
        ward_no integer,
        tole text,
        issue text,
        description text,
        level text,
        date integer

    )""")
def submit():
    conn=sqlite3.connect('report.db')
    c=conn.cursor()
    c.execute("INSERT INTO rep VALUES( :first_name,:last_name,:ward_no,:tole,:issue,:description,:level,:date )",{

          'first_name':fn_entry.get(),
          'last_name':ln_entry.get(),
          'ward_no':ward_entry.get(),
          'tole':tole_entry.get(),
          'issue':click.get(),
          'description':box.get(1.0,END),
          'level':sev.get(),
          'date':cal.get_date()
        })
    conn.commit()
    conn.close()
    messagebox.showinfo("Success",'ReportedSuccessfully!')


submitbtn=Button(root,text="Report",font=("Helvetica 15 bold"),fg="lavender",bg="deepskyblue2",activeforeground="lavender",activebackground="deepskyblue2",width=25,command=submit)
submitbtn.place(x=600,y=680)


root.mainloop()