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
middle=Canvas(root,width=3,height=470,bg="black")
middle.place(x=480,y=220)


#buttons
overview=Button(topcan,text="OVERVIEW",font=("Helvetica 15 bold"),bg="black",command=over_v,fg="red",bd=0)
overview.place(x=890,y=30)

report=Button(root,text="REPORT",font=("Helvetica 15 bold"),bg="black",fg="white",command=rep,bd=0)
report.place(x=1050,y=30)

status=Button(root,text="STATUS",font=("Helvetica 15 bold"),bg="black",fg="white",command=sts,bd=0)
status.place(x=1200,y=30)

ov_line=Canvas(root,width=600,height=3,bg="black",highlightthickness=0)
ov_line.place(x=1000,y=212)

report_line=Canvas(root,width=600,height=3,bg="black",highlightthickness=0)
report_line.place(x=1100,y=292)

status_line=Canvas(root,width=600,height=3,bg="black",highlightthickness=0)
status_line.place(x=1100,y=372)


rep_frame=LabelFrame(root,width=1100,height=690,bg="lavender")
rep_frame.place(x=0,y=80)


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


#report here
report_label=Label(rep_frame,text="REPORT",fg="deepskyblue2",bg="lavender",font=("Helvetica 35 bold"))
report_label.place(x=450,y=0)

date_sel=Label(rep_frame,text="Date:",fg="deepskyblue2",bg="lavender",font=("Helvetica 25 bold"))
date_sel.place(x=950,y=20)

cal=DateEntry(rep_frame,selectmode='day')
cal.place(x=950,y=70)



name=Label(rep_frame,text="Name of the reporter:-",fg="deepskyblue2",bg="lavender",font=("Helvetica 25 bold"))
name.place(x=0,y=80)

fn=Label(rep_frame,text="First Name",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
fn.place(x=0,y=150)

fn_entry=Entry(rep_frame,fg="black",bg="white",bd=0,font=("Helvetica 15 bold"))
fn_entry.place(x=0,y=180)

ln=Label(rep_frame,text="Last Name",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
ln.place(x=250,y=150)

ln_entry=Entry(rep_frame,fg="black",bd=0,font=("Helvetica 15 bold"))
ln_entry.place(x=250,y=180)

locat=Label(rep_frame,text="Location:",fg="deepskyblue2",bg="lavender",font=("Helvetica 25 bold"))
locat.place(x=500,y=80)

ward=Label(rep_frame,text="Ward No.:",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
ward.place(x=500,y=150)

ward_entry=Entry(rep_frame,fg="black",bd=0,font=("Helvetica 15 bold"))
ward_entry.place(x=500,y=180)

tole=Label(rep_frame,text="Tole:",fg="deepskyblue2",bg="lavender",font=("Helvetica 15 bold"))
tole.place(x=780,y=150)

tole_entry=Entry(rep_frame,fg="black",bd=0,font=("Helvetica 15 bold"))
tole_entry.place(x=780,y=180)


issue=Label(rep_frame,text="Issues Related to:",fg="deepskyblue2",bg="lavender",font=("Helvetica 20 bold"))
issue.place(x=0,y=230)

level=Label(rep_frame,text="Level of severity:",fg="deepskyblue2",bg="lavender",font=("Helvetica 20 bold"))
level.place(x=500,y=230)



sev = StringVar()
sev.set(" ")

def clicked():
    global sevr
    sevr=sev.get()
Radiobutton(rep_frame,text="Low",font=('Ariel', 17),fg="deepskyblue2",background="lavender",variable=sev,value="LOW",command=clicked).place(x=500,y=280)
Radiobutton(rep_frame,text="Moderate",font=('Ariel', 17),fg="deepskyblue2",background="lavender",variable=sev,value="MODERATE",command=clicked).place(x=600,y=280)
Radiobutton(rep_frame,text="Critical",font=('Ariel', 17),fg="deepskyblue2",background="lavender",variable=sev,value="CRITCIAL",command=clicked).place(x=760,y=280)

descp=Label(rep_frame,text="Descriptive Explanation",fg="deepskyblue2",background="lavender",font=("Helvetica 20 bold"))
descp.place(x=500,y=350)

box=Text(rep_frame,width=50,height=6,bg="white",font=("Ariel 13 bold"))
box.place(x=500,y=400)





##ACCOUNT VIEWING FEATURE 
conn=sqlite3.connect("issues.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS issues(
    date integer,
    urgency string,
    phone_number integer
    

)""")
def acc():
    import account_view

account=Button(root,text="ACCOUNT",font=("Helvetica 15 bold"),command=acc,bd=0,fg="blue",bg="black",activebackground="black")
account.place(x=1390,y=30)

# textbox=Text(root,width=20,height=20)
# textbox.pack()
# def submit(): 

#     textfile=open("data.txt",'a')
#     saved=textfile.write(textbox.get(1.0,END))
#     textbox.insert(END,saved)
#     global myimage
#     myimage=filedialog.askopenfilename(initialdir="/",filetypes=(("images","*.jpg"),))
#     file_path=myimage
#     imag=PhotoImage(file=file_path)
#     textbox.image_create(END,image=imag)

# butn=Button(root,text="submit",command=submit)
# butn.pack()
root.mainloop()