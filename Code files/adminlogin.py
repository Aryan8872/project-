from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("1920x1108")
root.title("Admin page")
root.config(bg="powderblue")

#logo of login
logo_login=ImageTk.PhotoImage(Image.open("images\\logo-white (2).png"))
logo=Label(root,image=logo_login)
logo.place(x=800,y=-100)



# importing main_page inside a function
def admin_page():
    root.destroy()
    import admin_control
 
# login frame
frame=LabelFrame(root,width=970,height=1108,bg="lavender")
frame.place(x=0,y=0)

#login in to your account
login=Label(frame,text="ADMIN LOGIN",fg="skyblue",font=("Helvetica 20 bold"),bg="lavender")
login.place(x=420,y=110)

#username
un_entry=Entry(frame,font=("Helvetica 14 bold"),width=25,bd=0,bg="lavender",fg="black")
un_entry.place(x=360,y=255)
un_entry.insert(0,'Username')
un_line=Canvas(frame,width=280,height=2.0,bg="black",highlightthickness=0)
un_line.place(x=360,y=280)

#fucntion to remove "Username" when mouse cursor is clicked in entry box
def on_enter(event):
    if un_entry.get()=='Username':
        un_entry.delete(0,END)
un_entry.bind('<FocusIn>',on_enter)

#fucntion to add "Username" when mouse cursor is unclicked from entry box
def on_exit(event0):
    if un_entry.get()=='':
        un_entry.insert(0,'Username')
un_entry.bind('<FocusOut>',on_exit)


#password
pw_entry=Entry(frame,font=("Helvetica 14 bold"),width=25,bd=0,bg="lavender",fg="black")
pw_entry.place(x=360,y=350)
pw_entry.insert(0,'Password')
pw_line=Canvas(frame,width=280,height=2.0,bg="black",highlightthickness=0)
pw_line.place(x=360,y=375)

#fucntion to remove "Password" when mouse cursor is clicked in entry box
def on_enter1(event1):
    if pw_entry.get()=='Password':
        pw_entry.delete(0,END)
pw_entry.bind('<FocusIn>',on_enter1)

#fucntion to add "Password" when mouse cursor is unclicked from entry box
def on_enter2(event2):
    if pw_entry.get()=='':
        pw_entry.insert(0,'Password')
pw_entry.bind('<FocusOut>',on_enter2)

#hide and show password
#function to change closeeye to openeye
def hide():
    closeeye.config(file='images\\openeye.png')
    pw_entry.config(show='*')
    eyeButton.config(command=show)

#function to change openeye to closeeye
def show():
    closeeye.config(file='images\\closeeye.png')
    pw_entry.config(show='')
    eyeButton.config(command=hide)


closeeye=PhotoImage(file='images\\closeeye.png')
eyeButton=Button(frame,image=closeeye,bd=0,bg='lavender',activebackground='lavender',cursor='hand2',command=hide)
eyeButton.place(x=610,y=345)



#===================================================================================================================================
                             #DATABASE CONNECTION for LOGIN PAGE

conn=sqlite3.connect("admins.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS admin(
    user_name text,
    password text
)""")

# conn=sqlite3.connect("admins.db")
# c=conn.cursor()
# data=("kshitish","ksh321")
# c.execute("INSERT INTO admin(user_name,password)VALUES(?,?)",data)
# conn.commit()
# conn.close()
def login_action():
    conn = sqlite3.connect("admins.db")
    c = conn.cursor()

    user = 'SELECT * FROM admin WHERE user_name = ? and password = ?'
    c.execute(user, [(un_entry.get()), (pw_entry.get())])
    
    result = c.fetchall()
    if result:
        messagebox.showinfo("Success", 'Logged in Successfully.')
       
        admin_page()

    else:
        messagebox.showerror("Failed", "Wrong Login details, please try again.")

#loginbutton
loginButton=Button(frame,text='Login',font=('Open Sans',16,'bold'),fg='black',bg='powderblue',activebackground='lavender',activeforeground="lavender",cursor='hand2',bd=0,width=22,command= login_action)
loginButton.place(x=360,y=460)

root.mainloop()