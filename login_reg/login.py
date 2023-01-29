from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("1920x1108")
root.title("MUNICIPAL PROBLEM RESOLVER")
root.config(bg="powderblue")

#logo of login
logo_login=ImageTk.PhotoImage(Image.open("logo-white (2).png"))
logo=Label(root,image=logo_login)
logo.place(x=800,y=-100)



# importing main_page inside a function
def main_page():
    root.destroy()
    import main_page
 
# login frame
frame=LabelFrame(root,width=970,height=1108,bg="lavender")
frame.place(x=0,y=0)

#login in to your account
login=Label(frame,text="LOGIN",fg="skyblue",font=("Helvetica 20 bold"),bg="lavender")
login.place(x=450,y=110)

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
    closeeye.config(file='openeye.png')
    pw_entry.config(show='*')
    eyeButton.config(command=show)

#function to change openeye to closeeye
def show():
    closeeye.config(file='closeeye.png')
    pw_entry.config(show='')
    eyeButton.config(command=hide)


closeeye=PhotoImage(file='closeeye.png')
eyeButton=Button(frame,image=closeeye,bd=0,bg='lavender',activebackground='lavender',cursor='hand2',command=hide)
eyeButton.place(x=610,y=345)



#===================================================================================================================================
                             #DATABASE CONNECTION for LOGIN PAGE



def login_action():
    conn = sqlite3.connect("registration.db")
    c = conn.cursor()

    user = 'SELECT * FROM register WHERE user_name = ? and password = ?'
    c.execute(user, [(un_entry.get()), (pw_entry.get())])
    un=un_entry.get()
    result = c.fetchall()
    if result:
        messagebox.showinfo("Success", 'Logged in Successfully.')
        c.execute("""UPDATE register SET
                    status=:inactive
                    WHERE status=:active""",
                    {'inactive':False,
                    'active':True})
        conn.commit()
        c.execute("""UPDATE register SET
                    status= :condition
                    WHERE user_name = :un""",
                    {
                        'condition':True,
                        'un':un
                    })
        conn.commit()
        main_page()

    else:
        messagebox.showerror("Failed", "Wrong Login details, please try again.")



#loginbutton
loginButton=Button(frame,text='Login',font=('Open Sans',16,'bold'),fg='black',bg='powderblue',activebackground='lavender',activeforeground="lavender",cursor='hand2',bd=0,width=22,command= login_action)
loginButton.place(x=360,y=460)

def open_reg():
    root.destroy()
    import registration

#create account
create=Button(frame,text="CREATE ONE",font=("Arial 10 bold"),fg="black",bg="lavender",command=open_reg,activebackground="lavender",bd=0)
create.place(x=390,y=410)



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
    save_btn=Button(fp,text="SAVE",bg="pink",activebackground="pink",activeforeground="pink",fg="green",command=lambda:change_pass())
    save_btn.place(x=10,y=120)
    
#forgot password
forgetButton=Button(frame,text='Forgot Password?',bd=0,font=("Helvetica 10 italic"),fg="black",bg='lavender',activebackground='lavender',activeforeground="black",cursor='hand2',command=forgotpass)
forgetButton.place(x=560,y=395)



##########################################################################################################################################################
                                 #registration page


















##########################################################################################################################################################
##########################################################################################################################################################
                                              #backend
  ##################################                              ########################################









root.mainloop()