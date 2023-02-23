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


def user_check():
    '''checks if the entered username is in the database'''

    un=username_entry.get()
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
         c.execute("""UPDATE register SET              
            password= :passwd
            WHERE user_name = :u""",
            {
            'passwd':newpass_entry.get(),
            'u':un
            })
         conn.commit()
         conn.close()   
         messagebox.showinfo("Congrats!","password changed succesfully")
         root.destroy()
         import login
         
#save button
save_btn=Button(root,text="Submit",bg="lightgreen",activebackground="lightblue",activeforeground="black",
fg="black",font=("Medium",15),command=user_check)
save_btn.place(x=80,y=380,width=190,height=47)


root.mainloop()