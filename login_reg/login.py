from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("900x600")
root.title("MUNICIPAL PROBLEM RESOLVER")
root.config(bg="skyblue")
root.maxsize(900,600)
root.minsize(900,600)

# #logo of login
# logo_login=ImageTk.PhotoImage(Image.open("logo-white (2).png"))
# logo=Label(root,image=logo_login)
# logo.place(x=800,y=-100)



# importing main_page inside a function
def main_page():
    root.destroy()
    import main_page
 
# login frame
frame=LabelFrame(root,width=500,height=600,bg="lavender")
frame.place(x=0,y=0)

#login in to your account
login=Label(frame,text="LOGIN",fg="deepskyblue2",font=("Helvetica 20 bold"),bg="lavender")
login.place(x=220,y=80)

#username
un_entry=Entry(frame,font=("Helvetica 14 bold"),width=25,bd=0,bg="lavender",fg="deepskyblue2")
un_entry.place(x=140,y=200)
un_entry.insert(0,'Username')
un_line=Canvas(frame,width=280,height=2.0,bg="deepskyblue2",highlightthickness=0)
un_line.place(x=140,y=225)

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
pw_entry=Entry(frame,font=("Helvetica 14 bold"),width=25,bd=0,bg="lavender",fg="deepskyblue2")
pw_entry.place(x=140,y=300)
pw_entry.insert(0,'Password')
pw_line=Canvas(frame,width=280,height=2.0,bg="deepskyblue2",highlightthickness=0)
pw_line.place(x=140,y=325)

#fucntion to remove "Password" when mouse cursor is clicked in entry box
def on_enter1(event1):
    if pw_entry.get()=='Password':
        pw_entry.delete(0,END)
        pw_entry.config(show='*')
pw_entry.bind('<FocusIn>',on_enter1)

#fucntion to add "Password" when mouse cursor is unclicked from entry box
def on_enter2(event2):
    if pw_entry.get()=='':
        pw_entry.insert(0,'Password')
pw_entry.bind('<FocusOut>',on_enter2)


#hide and show password
#function to change closeeye to openeye
def hide():
    closeeye.config(file='closeeye.png')
    pw_entry.config(show='*')
    eyeButton.config(command=show)

#function to change openeye to closeeye
def show():
    closeeye.config(file='openeye.png')
    pw_entry.config(show='')
    eyeButton.config(command=hide)


closeeye=PhotoImage(file='closeeye.png')
eyeButton=Button(frame,image=closeeye,bd=0,bg='lavender',activebackground='lavender',cursor='hand2',command=show)
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
        # c.execute("""UPDATE register SET
        #             status=:inactive
        #             WHERE status=:active""",
        #             {'inactive':False,
        #             'active':True})
        conn.commit()
        c.execute("""UPDATE register SET
                    user_status= :condition
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
loginButton=Button(frame,text='Login',font=('Open Sans',16,'bold'),fg='deepskyblue2',bg='lavender',activebackground='lavender',activeforeground="lavender",cursor='hand2',width=22,command= login_action)
loginButton.place(x=140,y=400)



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
    save_btn=Button(fp,text="SAVE",bg="pink",activebackground="pink",activeforeground="pink",fg="green",command=change_pass)
    save_btn.place(x=10,y=120)
    
#forgot password
forgetButton=Button(frame,text='Forgot Password?',bd=0,font=("Helvetica 10 italic"),fg="deepskyblue2",bg='lavender',activebackground='lavender',activeforeground="deepskyblue2",cursor='hand2',command=forgotpass)
forgetButton.place(x=360,y=345)



##########################################################################################################################################################
                                 #registration page


def open_reg():
    root.destroy()
    import registration

#create account
create=Button(root,text="Create Account",font=('Open Sans',14,'bold'),fg="deepskyblue2",bg="white",command=open_reg,activebackground="skyblue",bd=0,cursor='hand2',width=20)
create.place(x=600,y=300)

#text on registeration template
new=Label(root,text="New here? Join us",font=("Arial 20 bold"),fg="white",bg="skyblue").place(x=600,y=180)
















##########################################################################################################################################################
##########################################################################################################################################################
                                              #backend
  ##################################                              ########################################









root.mainloop()