from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("Municipal Problem Reporting")
root.configure(background='lavender')
root.geometry("1200x700")
# root.iconbitmap('Capture.ico')
root.configure(background='lavender')


def open_login():
    root.destroy()
    import login

#FRAMES 
frame2=Frame(root,width=400,height=700,highlightbackground="skyblue", highlightthickness=1,background="skyblue")
frame2.place(x=800,y=0)

frame1=Frame(root,width=800,height=700,highlightbackground="lavender", highlightthickness=1,background="lavender")
frame1.place(x=0,y=0)

#labels
registration=Label(frame1,text="Registration",font=('Ariel',35),fg="skyblue",background="lavender")
registration.place(x=75,y=25)

username=Label(frame1,text="User Name",font=('Ariel', 17),fg="skyblue",background="lavender")
username.place(x=45,y=120)

password=Label(frame1,text="Password",font=('Ariel', 17),fg="skyblue",background="lavender")
password.place(x=445,y=110)

phn=Label(frame1,text="Mobile Number",font=('Ariel', 17),fg="skyblue",background="lavender")
phn.place(x=45,y=220)

email1=Label(frame1,text="E-Mail Address",font=('Ariel', 17),fg="skyblue",background="lavender")
email1.place(x=45,y=330)

add=Label(frame1,text="Address",font=('Ariel', 17),fg="skyblue",background="lavender")
add.place(x=445,y=330)


Confirm=Label(frame1,text="Confirm Password",font=('Ariel', 17),fg="skyblue",background="lavender")
Confirm.place(x=445,y=220)

ward=Label(frame1,text="Ward Number",font=('Ariel', 17),fg="skyblue",background="lavender")
ward.place(x=45,y=440)




#ENTRY BOXES
usernam_entry=Entry(frame1,width=35,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="lavender")
usernam_entry.place(x=58,y=165)

pass_entry=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="lavender")
pass_entry.place(x=458,y=165)

confpass_entry=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="lavender")
confpass_entry.place(x=458,y=275)

entryemail=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="lavender")
entryemail.place(x=58,y=385)

addr_ent=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="lavender")
addr_ent.place(x=458,y=385)

entryward=Entry(frame1,width=35,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="lavender")
entryward.place(x=58,y=495)


phn_entry=Entry(frame1,width=25,highlightthickness = 0, borderwidth=0,font=('Ariel', 15),background="lavender")
phn_entry.place(x=58,y=275)





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


proj_logo=ImageTk.PhotoImage(Image.open("images\\logo-white (4).png"))
logo_label=Label(root,image=proj_logo,bd=0,bg="black",height=700, width=400)
logo_label.place(x=800,y=0)



#radio button to select gender of user
gender=Label(frame1,text="GENDER",font=('Ariel', 17),fg="skyblue",background="lavender")
gender.place(x=445,y=440)
gen = StringVar()
gen.set(" ")

def clicked():
    global gend
    gend=gen.get()
Radiobutton(frame1,text="Male",font=('Ariel', 17),fg="skyblue",background="lavender",variable=gen,value="Male",command=clicked).place(x=440,y=500)
Radiobutton(frame1,text="Female",font=('Ariel', 17),fg="skyblue",background="lavender",variable=gen,value="Female",command=clicked).place(x=540,y=500)
Radiobutton(frame1,text="Other",font=('Ariel', 17),fg="skyblue",background="lavender",variable=gen,value="Other",command=clicked).place(x=660,y=500)

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
        address text,
        ward no integer ,
        gender text,
        user_status boolean
      
    )""")

def add_rec():
    #converting default data type of entry box into integer if user inputs integer number
    try:
        global phn
        phn=int(phn_entry.get())       
    except ValueError:
        messagebox.showwarning("error!","phone number is not an integer")

    #getting length of phone number if the phone number is integer
    try:
        global num
        num=len(phn_entry.get())
    except:
        pass

    if  (usernam_entry.get()=='' or pass_entry.get()=='' or phn_entry.get()=='' or entryemail.get()=='' or entryward.get()==''):
         messagebox.showerror("Error","one or more fields are empty")
    elif usernam_entry.get()=='':
        messagebox.showerror("Error","Empty username")
    elif len(pass_entry.get())<=5:
         messagebox.showerror("Error","Password should be more than 5 characters")
    elif '@' not in entryemail.get()  or  ".com" not in entryemail.get():
         messagebox.showerror("Error","Invalid email format")
    elif num!=10:
         messagebox.showerror("Error","Invalid phone number length")
  
    

    #converting default data type of entry box into integer so that  we can verify if the input is integer or not
    try:
        global wd
        wd=int(entryward.get())       
    except ValueError:
        messagebox.showwarning("error!","Please enter integer in ward field")

    else:
        try:
            conn=sqlite3.connect('registration.db')
            c=conn.cursor()
            c.execute("INSERT INTO register VALUES( :username, :password, :phone_num, :email, :add, :ward,  :gender, :user_status )",{

                    'username':usernam_entry.get(),
                    'password':pass_entry.get(),
                    'phone_num':phn_entry.get(),
                    'email':entryemail.get(),
                    'add':addr_ent.get(),
                    'ward':entryward.get(),
                    'gender':gend,
                    'user_status':False
                
                    })
            conn.commit()
            conn.close()
            messagebox.showinfo("Success",'account created Successfully!')
            open_login()
        
        #returns error if the user doesnot input gender
        except NameError: 
            messagebox.showerror("Error","Enter your gender")


#REGISTER BUTTON
loginbotton=Button(frame1,text="Create Account",font=('Ariel', 20),padx=250,pady=4.5,borderwidth=0,bg="skyblue",fg="white",command=add_rec)
loginbotton.place(x=45,y=605)


root.mainloop()