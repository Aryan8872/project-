from tkinter import *
import sqlite3
from tkinter import messagebox
def reset_password():

    fp = Toplevel(root)
    fp.title("Reset Password")
    fp.config(bg="lavender")
    fp.maxsize(width=550,height=400)
    fp.minsize(width=550,height=400)

    myLable2 = Label(fp, text="Reset Password",bg="lavender",fg="deepskyblue2",font=("Bold",24))
    myLable2.pack()


    myLable2 = Label(fp, text="Reset your password so that you will be able to access all the features.",bg="lavender",fg="deepskyblue2",font=("Extra Light",13))
    myLable2.pack()

    newpass_label=Label(fp,text="New Password",bg="lavender",fg="deepskyblue2",font=("Medium",12))
    global newpass_entry
    newpass_entry=Entry(fp,bg="white",fg="black")
    newpass_label.place(x=75,y=120)
    newpass_entry.place(x=75,y=150,width=260,height=30)

    confirmpass_label=Label(fp,text="Confirm Password",fg="deepskyblue2",bg="lavender",font=("Medium",12))
    global confirmpass_entry
    confirmpass_entry=Entry(fp,bg="white",fg="black")
    confirmpass_label.place(x=75,y=200)
    confirmpass_entry.place(x=75,y=220,width=260,height=30)


    reset_btn=Button(fp,text="Reset Password",bg="light green",activebackground="lightblue",activeforeground="black",fg="black",font=("Medium",15))
    reset_btn.place(x=150,y=290,width=190,height=50)

root=Tk()
root.title("Forgot Password")
root.config(bg="lavender")
root.maxsize(width=550,height=400)
root.minsize(width=550,height=400)

myLable = Label(root, text="Please enter your email that you have registered with.",fg="deepskyblue2",bg="lavender",font=("Extra Light",16))
myLable.place(x=40,y=50)

email_label=Label(root,text="EMAIL",fg="deepskyblue2",bg="lavender",font=("Bold",13))
email_entry=Entry(root,bg="white",fg="black",font=("Light",13))
email_label.place(x=75,y=150)
email_entry.place(x=70,y=170,width=270,height=36)


def email_check():
    conn=sqlite3.connect("registration.db")
    c=conn.cursor()
    c.execute("SELECT * from register")
    record=c.fetchall()
    if (email_entry.get()==record[0][3]):
        reset_password()
    else:
        messagebox.showinfo('Error!',"Username doesnot exist")


def change_pass():
    em=email_entry.get()
    if newpass_entry.get() == confirmpass_entry.get():
        conn = sqlite3.connect("registration.db")
        c = conn.cursor()
        c.execute("""UPDATE register SET 
            'email'= :email_add,
            password= :passwd
            WHERE email = :em""",
            {'email_add':email_entry.get(),
            'passwd':newpass_entry.get()


        }
  )

        messagebox.showinfo('Congrats', 'Password changed successfully')
    else:
        messagebox.showerror('Error!', "Passwords didn't match")
    conn.commit()
    conn.close()



#save button
save_btn=Button(root,text="Submit",bg="lightgreen",activebackground="lightblue",activeforeground="black",fg="black",font=("Medium",15),command=email_check)
save_btn.place(x=80,y=280,width=190,height=47)

root.mainloop()