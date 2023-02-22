from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry("900x600")
root.title("MUNICIPAL PROBLEM RESOLVER")
root.config(bg="skyblue")
root.maxsize(900,600)
root.minsize(900,600)


# importing main_page inside a function
def overview_page():
    root.destroy()
    import overview
 
# login frame
frame=LabelFrame(root,width=500,height=600,bg="lavender")
frame.place(x=0,y=0)

#logo of login
logo_login=ImageTk.PhotoImage(Image.open("images\\logo-(8).png"))
logo=Label(frame,image=logo_login)
logo.place(x=0,y=0)
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


# hide and show password
# function to change closeeye to openeye
def hide():
    closeeye.config(file='images\\closeeye.png')
    pw_entry.config(show='*')
    eyeButton.config(command=show)

#function to change openeye to closeeye
def show():
    closeeye.config(file='images\\openeye.png')
    pw_entry.config(show='')
    eyeButton.config(command=hide)


closeeye=PhotoImage(file='images\\closeeye.png')
eyeButton=Button(frame,image=closeeye,bd=0,bg='lavender',activebackground='lavender',cursor='hand2',command=show)
eyeButton.place(x=395,y=295)


#===================================================================================================================================
                             #DATABASE CONNECTION for LOGIN PAGE



def login_action():
    if (un_entry.get()=='' or pw_entry.get()==''):
        

        messagebox.showerror("error","one or more fields are empty")
    
    else:

        conn = sqlite3.connect("registration.db")
        c = conn.cursor()
        user = 'SELECT * FROM register WHERE user_name = ? and password = ?'
        c.execute(user, [(un_entry.get()), (pw_entry.get())])
        un=un_entry.get()
        result = c.fetchall()
        if result:
            messagebox.showinfo("Success", 'Logged in Successfully.')
            conn.commit()
            c.execute("""UPDATE register SET
                        user_status= :condition
                        WHERE user_name = :un""",
                        {
                            'condition':True,
                            'un':un
                        })
            conn.commit()
            overview_page()
        

        else:
            messagebox.showerror("Failed", "Wrong Login details, please try again.")
        



#loginbutton
loginButton=Button(frame,text='Login',font=('Open Sans',16,'bold'),fg='deepskyblue2',bg='lavender',activebackground='lavender',activeforeground="lavender",cursor='hand2',width=22,command= login_action)
loginButton.place(x=140,y=400)



##############################################################################################################################################################
                                          #forgot password




def forgotpass():
    login.destroy()
    import forgot_pass
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