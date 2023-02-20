from tkinter import *
import sqlite3
from tkinter import messagebox


root=Tk()
root.title("Forgot Password")
root.config(bg="lavender")
root.geometry("600x500")

myLable = Label(root, text="Please enter your username that you have registered with.",fg="deepskyblue2",bg="lavender",font=("Extra Light",16))
myLable.place(x=40,y=50)

username_label=Label(root,text="Username",fg="deepskyblue2",bg="lavender",font=("Bold",13))
username_entry=Entry(root,bg="white",fg="black",font=("Light",10))
username_label.place(x=75,y=130)
username_entry.place(x=70,y=170,width=270)


newpass_label=Label(root,text="New password",fg="deepskyblue2",bg="lavender",font=("Bold",13))
newpass_entry=Entry(root,bg="white",fg="black",font=("Light",10))
newpass_label.place(x=75,y=200)
newpass_entry.place(x=70,y=240,width=270)


confirmpass_label=Label(root,text="Confirm password",fg="deepskyblue2",bg="lavender",font=("Bold",13))
confirmpass_entry=Entry(root,bg="white",fg="black",font=("Light",10))
confirmpass_label.place(x=75,y=280)
confirmpass_entry.place(x=70,y=320,width=270)


def email_check():
    conn=sqlite3.connect("registration.db")
    c=conn.cursor()
    c.execute("SELECT * from register WHERE user_name=?",[(username_entry.get())])
    record=c.fetchall()
    if username_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
        messagebox.showerror("Error","empty fields")
    elif not record:
        messagebox.showerror('Error!',"Username doesnot exist")
    elif newpass_entry.get() != confirmpass_entry.get():
        messagebox.showerror('Error!',"passwords doesnot match")
    
    else:
         conn = sqlite3.connect("registration.db")
         c = conn.cursor()
         c.execute("""UPDATE register SET 
            password= :passwd
            WHERE 'user_name'= :u""",
            {
            'u':username_entry.get(),
            'passwd':newpass_entry.get()
        })
         messagebox.showerror("Congrats!","password changed succesfully")
         root.destroy()
         import login
    conn.commit()
    conn.close()
    





 



#save button
save_btn=Button(root,text="Submit",bg="lightgreen",activebackground="lightblue",activeforeground="black",fg="black",font=("Medium",15),command=email_check)
save_btn.place(x=80,y=380,width=190,height=47)

# def reset_password():

#     fp = Toplevel(root)
#     fp.title("Reset Password")
#     fp.config(bg="lavender")
#     fp.maxsize(width=550,height=400)
#     fp.minsize(width=550,height=400)

#     myLable2 = Label(fp, text="Reset Password",bg="lavender",fg="deepskyblue2",font=("Bold",24))
#     myLable2.pack()


#     myLable2 = Label(fp, text="Reset your password so that you will be able to access all the features.",bg="lavender",fg="deepskyblue2",font=("Extra Light",13))
#     myLable2.pack()

#     newpass_label=Label(fp,text="New Password",bg="lavender",fg="deepskyblue2",font=("Medium",12))
#     global newpass_entry
#     newpass_entry=Entry(fp,bg="white",fg="black")
#     newpass_label.place(x=75,y=120)
#     newpass_entry.place(x=75,y=150,width=260,height=30)

#     confirmpass_label=Label(fp,text="Confirm Password",fg="deepskyblue2",bg="lavender",font=("Medium",12))
#     global confirmpass_entry
#     confirmpass_entry=Entry(fp,bg="white",fg="black")
#     confirmpass_label.place(x=75,y=200)
#     confirmpass_entry.place(x=75,y=220,width=260,height=30)


#     reset_btn=Button(fp,text="Reset Password",bg="light green",activebackground="lightblue",activeforeground="black",fg="black",font=("Medium",15))
#     reset_btn.place(x=150,y=290,width=190,height=50)

root.mainloop()