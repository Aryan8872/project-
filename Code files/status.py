from tkinter import *
import sqlite3
from PIL import Image,ImageTk
from tkinter import messagebox

root=Tk()
root.geometry("1920x1108")

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

#project title on top
mun=Label(root,text="MUNICIPAL",bg="black",fg="lavender",font=("Helvetica 20 bold"))
mun.place(x=160,y=18)

prob=Label(root,text="PROBLEM",bg="black",fg="lavender",font=("Helvetica 20 bold"))
prob.place(x=330,y=18)

resl=Label(root,text="RESOLVER",bg="black",fg="lavender",font=("Helvetica 20 bold"))
resl.place(x=487,y=18)

#project logo
proj_logo=ImageTk.PhotoImage(Image.open("images\\main_logo.png"))
logo_label=Label(root,image=proj_logo,bd=0,bg="black",height=70)
logo_label.place(x=640,y=5)

proj_logo2=ImageTk.PhotoImage(Image.open("images\\second.png"))
logo_label2=Label(root,image=proj_logo2,bd=0,bg="black",height=60,width=150)
logo_label2.place(x=0,y=10)

#BUTTONS
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
   report.config(background='black', foreground= "red")

def on_leave(e):
   report.config(background= 'black', foreground= 'white')

report=Button(root,text="REPORT",font=("Helvetica 15 bold"),bg="black",fg="white",command=rep,bd=0)
report.place(x=1050,y=30)

report.bind('<Enter>', on_enter)
report.bind('<Leave>', on_leave)

#StatusButton
def on_enter(e):
   status.config(background='black', foreground= "white")

def on_leave(e):
   status.config(background= 'black', foreground= 'red')
status=Button(root,text="STATUS",font=("Helvetica 15 bold"),bg="black",fg="red",command=sts,bd=0)
status.place(x=1200,y=30)

status.bind('<Enter>', on_enter)
status.bind('<Leave>', on_leave)

def acc():
    root.destroy()
    import account_view

account=Button(root,text="ACCOUNT",font=("Helvetica 15 bold"),command=acc,bd=0,fg="blue",bg="black",activebackground="black")
account.place(x=1390,y=30)

#frame for status feature
st_frame=LabelFrame(root,width=1920,height=200)
st_frame.place(x=0,y=80)

#code for changing background of the frame so that the progress can be shown

def bg_Change():
    if fn_entry.get()=='' or un_entry.get()=='':
        messagebox.showerror("error","one or many fields are empty!")
    else:
        conn=sqlite3.connect("status.db")
        c=conn.cursor()
        c.execute("SELECT * from status WHERE user_name=:user",{'user':un_entry.get()})
        data=c.fetchall()
        conn.commit()
        conn.close()
        global bgc
        bgc=''
        try:
            st_frame.configure(bg=data[0][3])
        except:
            st_frame.configure(bg="yellow")


#button for checking progress
check_prog=Button(st_frame,text="Check",command=bg_Change,bg="green",font=("Helvetica 13 bold"),width=20)
check_prog.place(x=605,y=120)


#firstname
fn_label=Label(root,font=("Helvetica 15 bold"),text="#ENTER YOUR FIRSTNAME")
fn_label.place(x=200,y=100)
fn_entry=Entry(root,font=("Helvetica 12 bold"))
fn_entry.place(x=200,y=140)

#username
un_label=Label(root,font=("Helvetica 15 bold"),text="#ENTER YOUR USERNAME")
un_label.place(x=600,y=100)
un_entry=Entry(root,font=("Helvetica 12 bold"))
un_entry.place(x=620,y=140)

#lastname
ln_label=Label(root,font=("Helvetica 15 bold"),text="#ENTER YOUR LASTNAME")
ln_label.place(x=1000,y=100)
ln_entry=Entry(root,font=("Helvetica 12 bold"))
ln_entry.place(x=1000,y=140)

#bottom canvas
bottomcan=Canvas(root,height=50,width=1800,bg="black")
bottomcan.place(x=0,y=750)

#Guiding lines

label1=Label(root,text="STEP-1: Enter the above mentioned data with a valid username first name and last name",font=("Helvetica 15 bold"))
label1.place(x=100,y=340)

label2=Label(root,text="STEP-2: After entering  valid data, press request status buttton to request status!",font=("Helvetica 15 bold"))
label2.place(x=100,y=390)

label3=Label(root,text="STEP-3: After your request is registered admins will notify you ",font=("Helvetica 15 bold"))
label3.place(x=100,y=440)

label4=Label(root,text="NOTE: You can check status by pressing check button and you can only request once at a time",font=("Helvetica 15 bold"))
label4.place(x=100,y=490)

#color indication
index=Label(root,bg="lavender",text="STATUS INDEX",font=("Helvetica 14 bold"))
index.place(x=1100,y=300)

blue=Label(root,bg="blue",text="BLUE",font=("Helvetica 11 bold"))
blue.place(x=1100,y=340)
blue_mean=Label(root,text="--REPORT RECEIVED",font=("Helvetica 9 bold"))
blue_mean.place(x=1200,y=340)

red=Label(root,text="RED",bg="red",font=("Helvetica 11 bold"))
red.place(x=1100,y=380)
red_mean=Label(root,text="--HELP IS ON THE WAY",font=("Helvetica 9 bold"))
red_mean.place(x=1200,y=380)

green=Label(root,text="GREEN",bg="green",font=("Helvetica 11 bold"))
green.place(x=1100,y=420)
green_mean=Label(root,text="--PROBLEM RESOLVED",font=("Helvetica 9 bold"))
green_mean.place(x=1200,y=420)

yellow=Label(root,text="YELLOW",bg="yellow",font=("Helvetica 11 bold"))
yellow.place(x=1100,y=460)
yellow_mean=Label(root,text="--No data!",font=("Helvetica 9 bold"))
yellow_mean.place(x=1200,y=460)


#creating table for database 
conn=sqlite3.connect("status.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS status(
    user_name text PRIMARY KEY,
    first_name text PRIMARY KEY,
    last_name text PRIMARY KEY,
    problem_status text

)""")
conn.commit()
conn.close()

#inserting data into database so that status can be checked
def change():
    con=sqlite3.connect("report.db")
    d=con.cursor()
    d.execute("SELECT * from rep WHERE first_name=? and last_name=? ",[(fn_entry.get()),(ln_entry.get())])
    report=d.fetchall()
    
    conn=sqlite3.connect("registration.db")           
    c=conn.cursor()
    c.execute("SELECT * from register WHERE user_name=?",[(un_entry.get())])  #selecting all data from registration database for verification
    record=c.fetchall()
    if record and report: 

        try:                                            #if data exists then status can be checked
            conn=sqlite3.connect("status.db")
            c=conn.cursor()
            c.execute("INSERT INTO status VALUES(:username,:firstname,:lastname,:problem_status)",{

                    'username':un_entry.get(),
                    'firstname':fn_entry.get(),
                    'lastname':ln_entry.get(),
                    'problem_status':"blue"           
                })

            conn.commit()
            conn.close()
            messagebox.showinfo('Success',"Request registered!")
        except sqlite3.IntegrityError:
            messagebox.showerror("error","request already exists")
        
    elif not report:
            messagebox.showerror("Error!","Enter valid first name and last name")
    elif not record:
            messagebox.showerror("Error!","Enter valid username")


#request button for requesting status to admins
request=Button(st_frame,text="Request Status",bg="skyblue3",font=("Helvetica 12 bold"),width=15,command=change)
request.place(x=1250,y=120)

def page_ref():            #it refreshes page by destroying window and again opening it
    root.destroy()
    import status
refresh_button=Button(root,text="REFRESH",fg="lavender",bg="green",font=("Helvetica 12 bold"),width=15,command=page_ref)
refresh_button.place(x=500,y=560)
root.mainloop()