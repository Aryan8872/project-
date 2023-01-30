from tkinter import *
import sqlite3
from PIL import Image,ImageTk
from tkinter import messagebox


reg=Tk()
reg.geometry("1845x1070")
reg.title("Registration page")
reg.config(bg="lavender")

   
    #frame
frame2=LabelFrame(reg,width=600,height=640,bg="lavender")
frame2.place(x=924,y=100)


photo_frame=LabelFrame(reg,width=900,height=900)
photo_frame.place(x=0,y=0)
photo=ImageTk.PhotoImage(Image.open("123.jpg"))
bg=Label(photo_frame,image=photo)
bg.place(x=0,y=0)
    
   
    #registration page label
reg_label=Label(reg,text="REGISTRATION",fg="black",bg="lavender",font=("Helvetica 25 bold"))
reg_label.place(x=1100,y=0)
page_label=Label(reg,text="PAGE",bg="lavender",fg="black",font=("Helvetica 25 bold"))
page_label.place(x=1175,y=45)

#first name
first_name_label=Label(frame2,text="FIRST NAME",bg="lavender",font=("Helvetica 10 bold"),fg="black")
first_name_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="lavender",highlightthickness=0,relief=FLAT,fg="#6b6a69")
first_name_line=Canvas(frame2,width=220,height=2.0,bg="black",highlightthickness=0)

first_name_ent.place(x=40,y=150)
first_name_line.place(x=40,y=174)
first_name_label.place(x=10,y=130)

#lastname
lastname_label=Label(frame2,text="LAST NAME",bg="lavender",font=("Helvetica 10 bold"),fg="black")
lastname_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="lavender",highlightthickness=0,relief=FLAT,fg="#6b6a69")
lastname_line=Canvas(frame2,width=220,height=2.0,bg="black",highlightthickness=0)

lastname_ent.place(x=350,y=150)
lastname_line.place(x=350,y=174)
lastname_label.place(x=310,y=130)

    #username 
un_label=Label(frame2,text="USERNAME",bg="lavender",font=("Helvetica 10 bold"),fg="black")
un_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="lavender",highlightthickness=0,relief=FLAT,fg="#6b6a69")
un_line=Canvas(frame2,width=260,height=2.0,bg="black",highlightthickness=0)

un_ent.place(x=200,y=210)
un_line.place(x=190,y=234)
un_label.place(x=160,y=190)

    #email
email_label=Label(frame2,text="E-MAIL",bg="lavender",font=("Helvetica 10 bold"),fg="black")

email_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="lavender",highlightthickness=0,relief=FLAT,fg="black")
email_line=Canvas(frame2,width=260,height=2.0,bg="black",highlightthickness=0)

email_ent.place(x=200,y=270)
email_line.place(x=190,y=294)
email_label.place(x=160,y=250)

    #PASSWORD
passwd_label=Label(frame2,text="PASSWORD",bg="lavender",font=("Helvetica 10 bold"),fg="black")
passwd_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="lavender",highlightthickness=0,relief=FLAT,fg="#6b6a69")
passwd_line=Canvas(frame2,width=260,height=2.0,bg="black",highlightthickness=0)

passwd_ent.place(x=50,y=330)
passwd_line.place(x=35,y=354)
passwd_label.place(x=20,y=310)

    #RE-TYPE PASSWORD
re_passwd_label=Label(frame2,text="RE-TYPE PASSWORD",bg="lavender",font=("Helvetica 10 bold"),fg="black")

re_passwd_entry=Entry(frame2,font=("Helvetica 14 bold"),bg="lavender",highlightthickness=0,relief=FLAT,fg="black")
re_passwd_line=Canvas(frame2,width=260,height=2.0,bg="black",highlightthickness=0)

re_passwd_entry.place(x=340,y=330)
re_passwd_line.place(x=325,y=354)
re_passwd_label.place(x=300,y=310)

    #PHONE NUMBER
phn_label=Label(frame2,text="PHONE-NUMBER",bg="lavender",font=("Helvetica 10 bold"),fg="black")

phn_entry=Entry(frame2,font=("Helvetica 14 bold"),bg="lavender",highlightthickness=0,relief=FLAT,fg="black")
phn_line=Canvas(frame2,width=260,height=2.0,bg="black",highlightthickness=0)

phn_entry.place(x=200,y=390)
phn_line.place(x=190,y=414)
phn_label.place(x=160,y=370)


    #radio button to select gender of user
gender=Label(frame2,text="GENDER",bg="lavender",fg="black",font=("Helvetica 10 bold"))
gender.place(x=160,y=430)
gen = StringVar()
gen.set(" ")

def clicked():
    global gend
    gend=gen.get()
Radiobutton(frame2,text="Male",fg="black",bg="lavender",font=("Helvetica 10 bold"),variable=gen,value="Male",command=clicked).place(x=200,y=460)
Radiobutton(frame2,text="Female",fg="black",bg="lavender",font=("Helvetica 10 bold"),variable=gen,value="Female",command=clicked).place(x=280,y=460)
Radiobutton(frame2,text="Other",fg="black",bg="lavender",font=("Helvetica 10 bold"),variable=gen,value="Other",command=clicked).place(x=380,y=460)


def login_open():
        reg.destroy()

def open_login():                 #opens login page after registering account
        reg.destroy()
        import login

#already a member
text=Label(frame2,text="ALREADY A MEMBER?",font=("Helvetica 10 bold"),fg="red",bg="lavender")
btn=Button(frame2,text="LOGIN",bg="lavender",fg="green",activebackground="lavender",bd=0,cursor="hand2",command=open_login)
text.place(x=220,y=600)
btn.place(x=365,y=600)

    #===================================================================================================================================
    #===================================================================================================================================
                                #database connnection
                                

conn=sqlite3.connect('registration.db')
c=conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS register(
        first_name text,
        last_name text,
        user_name text PRIMARY KEY,
        password text,
        email text ,
        phone_num integer,
        gender text
      
    )""")

def add_rec():
    conn=sqlite3.connect('registration.db')
    c=conn.cursor()
    c.execute("INSERT INTO register VALUES( :first_name, :last_name, :user_name, :password, :email, :phone_num, :gender )",{

            'first_name':first_name_ent.get(),
            'last_name':lastname_ent.get(),
            'user_name':un_ent.get(),
            'password':passwd_ent.get(),
            'email':email_ent.get(),
            'phone_num':phn_entry.get(),
            'gender':gend
           
            })
    conn.commit()
    conn.close()
    messagebox.showinfo("Success",'account created Successfully!')
    open_login()

#register button
register=Button(frame2,text="REGISTER",fg="black",bg="limegreen",font=("Helvetica 15 bold"),activeforeground="limegreen",width=18,bd=0,cursor="hand2",command=add_rec)
register.place(x=221,y=532)

reg.mainloop()









