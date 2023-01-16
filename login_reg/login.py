from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("1920x1108")
root.title("Municipal problem resolver")

#background image
bacg=ImageTk.PhotoImage(Image.open("login_reg/6.jpg"))
bac=Label(root,image=bacg,height=1108,width=1920)
bac.place(x=0,y=0)

#frame
frame=LabelFrame(root,width=670,height=500,bg="black")
frame.place(x=520,y=120)


#login in to your account
login=Label(frame,text="LOGIN IN TO YOUR ACCOUNT",fg="white",font=("Helvetica 20 bold"),bg="black")
login.place(x=110,y=30)


#logo
logo=ImageTk.PhotoImage(Image.open("login_reg/logo5.jpg"))
lg=Label(frame,image=logo,bg="purple",width=100,height=100)
lg.place(x=250,y=80)


#username
un_label=Label(frame,text="USERNAME",bg="#040405",font=("Helvetica 10 bold"),fg="#4f4e4d")
un_entry=Entry(frame,font=("Helvetica 14 bold"),bg="#040405",highlightthickness=0,relief=FLAT,fg="#6b6a69")
un_line=Canvas(frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
un_entry.place(x=200,y=200)
un_line.place(x=170,y=225)
un_label.place(x=120,y=180)

un_logo=ImageTk.PhotoImage(Image.open("login_reg/username.png"))
u=Label(frame,image=un_logo,bg="#040405",height=20,width=23)
u.place(x=160,y=200)


#password
pw_label=Label(frame,text="PASSWORD",bg="#040405",font=("Helvetica 10 bold"),fg="#4f4e4d")
pw_entry=Entry(frame,font=("Helvetica 14 bold"),bg="#040405",highlightthickness=0,relief=FLAT,fg="#6b6a69",show="*")
pw_line=Canvas(frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
pw_entry.place(x=200,y=260)
pw_line.place(x=170,y=280)
pw_label.place(x=120,y=235)

pw_logo=ImageTk.PhotoImage(Image.open("login_reg/password.png"))

p=Label(frame,image=pw_logo,bg="#040405",height=20,width=23)
p.place(x=160,y=255)


#forgot password
fp=Button(frame,text="FORGOT PASSWORD?",font=("Helvetica 10 italic"),bg="black",fg="red",activebackground="black",bd=0)
fp.place(x=280,y=290)


#question
ques=Label(frame,text="DONT HAVE AN ACCOUNT YET? ",font=("Helvetica 10 italic"),bg="black",fg="white")
ques.place(x=175,y=390)


#create account
crea=Button(frame,text="create one",font=("Arial 10 bold"),fg="white",bg="black")
crea.place(x=390,y=389)


#about us
au=Label(frame,text="ABOUT US",font=("Helvetica 10 bold"),bg="black",fg="limegreen")
au.place(x=260,y=440)


#===================================================================================================================================
                             #DATABASE CONNECTION



conn=sqlite3.connect('login.db')
c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS login(
    user_name text,
    password string

)""")



def login_action():
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()

    find_user = 'SELECT * FROM login WHERE user_name = ? and password = ?'
    cursor.execute(find_user, [(un_entry.get()), (pw_entry.get())])

    result = cursor.fetchall()
    if result:
        messagebox.showinfo("Success", 'Logged in Successfully.')
    else:
        messagebox.showerror("Failed", "Wrong Login details, please try again.")




#login button
login_b=Button(frame,text="LOGIN",bg="green",fg="white",font=("Helvetica 14 bold"),padx=50,command=login_action,cursor="hand2")
login_b.place(x=220,y=320)







root.mainloop()