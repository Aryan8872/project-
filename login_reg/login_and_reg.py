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
login=Label(frame,text="LOGIN PAGE",fg="white",font=("Helvetica 20 bold"),bg="black")
login.place(x=220,y=30)


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


##############################################################################################################################################################
                                          #forgot password

def forgotpass():
    fp=Toplevel(root)
    fp.config(bg="pink")

    email_label=Label(fp,text="EMAIL",fg="green",bg="pink")
    email_entry=Entry(fp,bg="pink",fg="black")
    email_label.place(x=0,y=1)
    email_entry.place(x=80,y=1)


    newpass_label=Label(fp,text="NEW PASSWORD",bg="pink",fg="green")
    newpass_entry=Entry(fp,bg="pink",fg="red")
    newpass_label.place(x=0,y=30)
    newpass_entry.place(x=100,y=30)

    confirmpass_label=Label(fp,text="CONFIRM PASSWORD",fg="green",bg="pink")
    confirmpass_entry=Entry(fp,bg="pink",fg="red")
    confirmpass_label.place(x=0,y=60)
    confirmpass_entry.place(x=120,y=60)


    oid_label=Label(fp,text="O-ID",fg="green",bg="pink")
    oid_entry=Entry(fp,fg="blue",bg="pink")
    oid_entry.place(x=60,y=90)
    oid_label.place(x=0,y=90)
        
  

    def change_pass():
        if newpass_entry.get() == confirmpass_entry.get():
            conn = sqlite3.connect("registration.db")
            c = conn.cursor()
            record_id=oid_entry.get()
            c.execute("""UPDATE register SET 
                'email'= :email_add,
                password= :passwd
                WHERE oid = :oid""",
                {'email_add':email_entry.get(),
                'passwd':newpass_entry.get(),
                'oid':record_id


            }
    )
            
            messagebox.showinfo('Congrats', 'Password changed successfully')
        else:
            messagebox.showerror('Error!', "Passwords didn't match")
        conn.commit()
        conn.close()


      #save button
    save_btn=Button(fp,text="SAVE",bg="pink",activebackground="pink",activeforeground="pink",fg="green",command=lambda:change_pass())
    save_btn.place(x=10,y=120)
    


#forgot password
fp=Button(frame,text="FORGOT PASSWORD?",font=("Helvetica 10 italic"),bg="black",fg="red",activebackground="black",bd=0,command=forgotpass)
fp.place(x=330,y=290)


#question
ques=Label(frame,text="DONT HAVE AN ACCOUNT YET? ",font=("Helvetica 10 italic"),bg="black",fg="white")
ques.place(x=175,y=410)

#about us
au=Label(frame,text="ABOUT US",font=("Helvetica 10 bold"),bg="black",fg="limegreen")
au.place(x=260,y=440)


#===================================================================================================================================
                             #DATABASE CONNECTION for LOGIN PAGE




def login_action():
    conn = sqlite3.connect("registration.db")
    c = conn.cursor()

    user = 'SELECT * FROM register WHERE user_name = ? and password = ?'
    c.execute(user, [(un_entry.get()), (pw_entry.get())])

    result = c.fetchall()
    if result:
        messagebox.showinfo("Success", 'Logged in Successfully.')
    else:
        messagebox.showerror("Failed", "Wrong Login details, please try again.")





##########################################################################################################################################################
                                 #registration page



def register():

    reg=Toplevel(root)
    reg.geometry("1845x1070")
    reg.title("Registration page")
    reg.config(bg="black")

    #background image
    root_bg=ImageTk.PhotoImage(Image.open("login_reg/bgreg2.jpg"))
    back=Label(reg,image=root_bg,height=1070,width=1845)
    back.place(x=0,y=0)


    #title
    title=Label(reg,text="MUNICIPAL",font=("Helvetica 50 bold"),fg="black",bg="lightpink1")
    title.place(x=100,y=190)
    title2=Label(reg,text="PROBELM",font=("Helvetica 50 bold"),fg="black",bg="lightpink3")
    title2.place(x=100,y=270)
    title3=Label(reg,text="RESOLVER",font=("Helvetica 50 bold"),fg="black",bg="dodgerblue4")
    title3.place(x=250,y=350)

    #frame
    frame2=LabelFrame(reg,width=600,height=640,bg="black")
    frame2.place(x=900,y=120)
    #frame bg
    frame_bg=ImageTk.PhotoImage(Image.open("login_reg/r3.jpg"))
    bacg=Label(frame2,image=frame_bg,height=640,width=600)
    bacg.place(x=0,y=0)

    #registration page label
    reg_label=Label(frame2,text="REGISTRATION",fg="white",bg="black",font=("Helvetica 25 bold"))
    reg_label.place(x=180,y=0)
    page_label=Label(frame2,text="PAGE",bg="black",fg="white",font=("Helvetica 25 bold"))
    page_label.place(x=255,y=45)

    #username label
    un_label=Label(frame2,text="USERNAME",bg="#040405",font=("Helvetica 10 bold"),fg="white")

    un_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
    un_line=Canvas(frame2,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

    un_ent.place(x=200,y=210)
    un_line.place(x=190,y=234)
    un_label.place(x=160,y=190)

    #email
    email_label=Label(frame2,text="E-MAIL",bg="#040405",font=("Helvetica 10 bold"),fg="white")

    email_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
    email_line=Canvas(frame2,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

    email_ent.place(x=200,y=270)
    email_line.place(x=190,y=294)
    email_label.place(x=160,y=250)

    #PASSWORD
    passwd_label=Label(frame2,text="PASSWORD",bg="#040405",font=("Helvetica 10 bold"),fg="white")

    passwd_ent=Entry(frame2,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
    passwd_line=Canvas(frame2,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

    passwd_ent.place(x=50,y=330)
    passwd_line.place(x=35,y=354)
    passwd_label.place(x=20,y=310)

    #RE-TYPE PASSWORD
    re_passwd_label=Label(frame2,text="RE-TYPE PASSWORD",bg="#040405",font=("Helvetica 10 bold"),fg="white")

    re_passwd_entry=Entry(frame2,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
    re_passwd_line=Canvas(frame2,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

    re_passwd_entry.place(x=340,y=330)
    re_passwd_line.place(x=325,y=354)
    re_passwd_label.place(x=300,y=310)

    #PHONE NUMBER
    phn_label=Label(frame2,text="PHONE-NUMBER",bg="#040405",font=("Helvetica 10 bold"),fg="white")

    phn_entry=Entry(frame2,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
    phn_line=Canvas(frame2,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

    phn_entry.place(x=200,y=390)
    phn_line.place(x=190,y=414)
    phn_label.place(x=160,y=370)


    #radio button
    gender=Label(frame2,text="GENDER",bg="gray11",fg="WHITE",font=("Helvetica 10 bold"))
    gender.place(x=160,y=430)
    gen=StringVar
    Radiobutton(frame2,text="Male",fg="DARKGRAY",bg="LAVENDER",font=("Helvetica 10 bold"),variable=gen,value="Male").place(x=200,y=460)
    Radiobutton(frame2,text="Female",fg="DARKGRAY",bg="LAVENDER",font=("Helvetica 10 bold"),variable=gen,value="Female").place(x=280,y=460)
    Radiobutton(frame2,text="Other",fg="DARKGRAY",bg="LAVENDER",font=("Helvetica 10 bold"),variable=gen,value="Other").place(x=380,y=460)



    #already a member
    text=Label(frame2,text="ALREADY A MEMBER?",font=("Helvetica 10 bold"),fg="red",bg="gray11")
    text2=Button(frame2,text="LOGIN",bg="gray11",fg="green",activebackground="gray11",bd=0,cursor="hand2")
    text.place(x=220,y=600)
    text2.place(x=365,y=600)

    #===================================================================================================================================
    #===================================================================================================================================
                                #database connnection
                                

    conn=sqlite3.connect('registration.db')
    c=conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS register(
        user_name text,
        password string,
        email string,
        phone_num integer
    

    )""")

    def add_rec():        
        conn=sqlite3.connect('registration.db')
        c=conn.cursor()

        c.execute("INSERT INTO register VALUES(:user_name, :password, :email, :phone_num )",{
            'user_name':un_ent.get(),
            'password':passwd_ent.get(),
            'email':email_ent.get(),
            'phone_num':phn_entry.get()
            

        })
        conn.commit()
        conn.close()
        messagebox.showinfo("Success",'account created Successfully!')

        reg.destroy()


    #register
    img=ImageTk.PhotoImage(Image.open("login_reg/button.png"))
    btn_lbl=Label(frame2,image=img,bg="gray11")
    btn_lbl.place(x=200,y=520)
    register=Button(frame2,text="REGISTER",fg="white",bg="limegreen",font=("Helvetica 15 bold"),activeforeground="limegreen",width=18,bd=0,cursor="hand2",command=add_rec)
    register.place(x=221,y=532)

#create account
create=Button(frame,text="CREATE ONE",font=("Arial 10 bold"),fg="white",bg="black",command=register)
create.place(x=390,y=410)


#login button
login_b=Button(frame,text="LOGIN",bg="green",fg="white",font=("Helvetica 14 bold"),padx=50,command=login_action,cursor="hand2")
login_b.place(x=220,y=340)





















##########################################################################################################################################################
##########################################################################################################################################################
                                              #backend
  ##################################                              ########################################









root.mainloop()