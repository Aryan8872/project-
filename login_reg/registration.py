from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.title("Municipal Problem Reporting")
root.configure(background='white')
root.geometry("1200x700")
# root.iconbitmap('Capture.ico')
root.configure(background='white')

def open_login():
    root.destroy()
    import login

#FRAMES 
frame2=Frame(root,width=400,height=700,highlightbackground="skyblue", highlightthickness=1,background="skyblue")
frame2.place(x=800,y=0)

frame1=Frame(root,width=800,height=700,highlightbackground="white", highlightthickness=1,background="white")
frame1.place(x=0,y=0)

#labels
registration=Label(frame1,text="Registration",font=('Ariel',35),fg="skyblue",background="white")
registration.place(x=75,y=25)

username=Label(frame1,text="User Name",font=('Ariel', 17),fg="skyblue",background="white")
username.place(x=45,y=120)

password=Label(frame1,text="Password",font=('Ariel', 17),fg="skyblue",background="white")
password.place(x=445,y=110)

phn=Label(frame1,text="Mobile Number",font=('Ariel', 17),fg="skyblue",background="white")
phn.place(x=45,y=220)

email1=Label(frame1,text="E-Mail Address",font=('Ariel', 17),fg="skyblue",background="white")
email1.place(x=45,y=330)

add=Label(frame1,text="Address",font=('Ariel', 17),fg="skyblue",background="white")
add.place(x=445,y=330)


Confirm=Label(frame1,text="Confirm Password",font=('Ariel', 17),fg="skyblue",background="white")
Confirm.place(x=445,y=220)

ward=Label(frame1,text="Ward Number",font=('Ariel', 17),fg="skyblue",background="white")
ward.place(x=45,y=440)

calls=Label(frame2,text="Contact:",font=('Ariel', 25),fg="white",background="skyblue")
calls.place(x=10,y=510)

num=Label(frame2,text="9862186238",font=('Ariel', 25),fg="white",bg="skyblue")
num.place(x=10,y=550)

#ENTRY BOXES
usernam_entry=Entry(frame1,width=35,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="white")
usernam_entry.place(x=58,y=165)

pass_entry=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="white")
pass_entry.place(x=458,y=165)

confpass_entry=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="white")
confpass_entry.place(x=458,y=275)

entryemail=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="white")
entryemail.place(x=58,y=385)

addr_ent=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="white")
addr_ent.place(x=458,y=385)

entryward=Entry(frame1,width=35,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="white")
entryward.place(x=58,y=495)


phn_entry=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="white")
phn_entry.place(x=58,y=275)
phn_entry.insert(0,"+977")


var=IntVar
c=Checkbutton(frame1,text="Keep Me Logged in",font=('Ariel', 17),variable=var,background="white")
c.place(x=290,y=550)


#canvas lines
mycanvas=Canvas(frame1,width=1,height=450,background="skyblue")
mycanvas.place(x=400,y=80)

mycanvas2=Canvas(frame1,width=1,height=675,background="skyblue")
mycanvas2.place(x=5,y=4)

mycanvas3=Canvas(frame1,width=400,height=1,background="skyblue")
mycanvas3.place(x=5,y=5)

mycanvas4=Canvas(frame1,width=1,height=675,background="skyblue")
mycanvas4.place(x=783,y=4)

mycanvas5=Canvas(frame1,width=400,height=1,background="skyblue")
mycanvas5.place(x=381,y=675)

mycanvas6=Canvas(frame1,width=300,height=1,background="black")
mycanvas6.place(x=50,y=200)

mycanvas7=Canvas(frame1,width=300,height=1,background="black")
mycanvas7.place(x=50,y=310)

mycanvas8=Canvas(frame1,width=300,height=1,background="black")
mycanvas8.place(x=50,y=420)

mycanvas9=Canvas(frame1,width=300,height=1,background="black")
mycanvas9.place(x=50,y=530)

mycanvas10=Canvas(frame1,width=300,height=1,background="black")
mycanvas10.place(x=450,y=200)

mycanvas11=Canvas(frame1,width=300,height=1,background="black")
mycanvas11.place(x=450,y=310)

mycanvas12=Canvas(frame1,width=300,height=1,background="black")
mycanvas12.place(x=450,y=420)


    #radio button to select gender of user
gender=Label(frame1,text="GENDER",font=('Ariel', 17),fg="skyblue",background="white")
gender.place(x=445,y=440)
gen = StringVar()
gen.set(" ")

def clicked():
    global gend
    gend=gen.get()
Radiobutton(frame1,text="Male",font=('Ariel', 17),fg="skyblue",background="white",variable=gen,value="Male",command=clicked).place(x=415,y=495)
Radiobutton(frame1,text="Female",font=('Ariel', 17),fg="skyblue",background="white",variable=gen,value="Female",command=clicked).place(x=520,y=495)
Radiobutton(frame1,text="Other",font=('Ariel', 17),fg="skyblue",background="white",variable=gen,value="Other",command=clicked).place(x=650,y=495)

 #===================================================================================================================================
    #===================================================================================================================================
                                #database connnection
                                

conn=sqlite3.connect('registration.db')
c=conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS register(
        user_name text PRIMARY KEY,
        password text,
        phone_num integer,
        email text,
        ward no integer ,
        gender text
      
    )""")

def add_rec():
    conn=sqlite3.connect('registration.db')
    c=conn.cursor()
    c.execute("INSERT INTO register VALUES( :username, :password, :phone_num, :email, :ward,  :gender )",{

            'username':usernam_entry.get(),
            'password':pass_entry.get(),
            'phone_num':phn_entry.get(),
            'email':entryemail.get(),
            'ward':entryward.get(),
            'gender':gend
           
            })
    conn.commit()
    conn.close()
    messagebox.showinfo("Success",'account created Successfully!')
    open_login()

#REGISTER BUTTON
loginbotton=Button(frame1,text="Create Account",font=('Ariel', 20),padx=250,pady=4.5,borderwidth=0,bg="skyblue",fg="white",command=add_rec)
loginbotton.place(x=45,y=605)
root.mainloop()