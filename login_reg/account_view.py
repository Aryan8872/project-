from tkinter import *
import sqlite3
from tkinter import messagebox

#create a window
window=Tk()
window.geometry("1280x720")
window.title("Accounts")





#Frame for account details
frame2=LabelFrame(window, height=450, width=378, bg='white').place(x=600, y=220)

#label for account details
fn=Label(window,text="First Name:",font=('Arial',10,'bold'),bg='white').place(x=620,y=240)
ln=Label(window,text="Last Name:",font=('Arial',10,'bold'),bg='white').place(x=790,y=240)
un=Label(window,text="username:",font=('Arial',10,'bold'),bg='white').place(x=620,y=310)
em=Label(window,text="email:",font=('Arial',10,'bold'),bg='white').place(x=620,y=380)
pss=Label(window,text="password",font=('Arial',10,'bold'),bg='white').place(x=620,y=450)
cpss=Label(window,text="confirm Password:",font=('Arial',10,'bold'),bg='white').place(x=790,y=450)
phn=Label(window,text="phone number:",font=('Arial',10,'bold'),bg='white').place(x=700,y=530)

#fetch user data
try:
    conn=sqlite3.connect('registration.db')
    c=conn.cursor()
    c.execute("SELECT * from register WHERE status=:act",{'act':True})
    records=c.fetchall()
    a=records[0][0]
    b=records[0][1]
    c=records[0][2]
    d=records[0][3]
    e=records[0][4]
    f=records[0][5]

    conn.commit()
    conn.close()
except:
    a="First Name"
    b="Last Name"
    c="username"
    d="password"
    e="email"
    f="phone number"


#show password functions
def show():
    if (showw.get()==1):
        passwd.config(show='')
    else:
        passwd.config(show='*')
def show2():
    if (showw2.get()==1):
        conf_passwd.config(show='')
    else:
        conf_passwd.config(show='*')


#Entries for Account

first_name=Entry(window)
first_name.insert(0,a)
first_name.place(x=620,y=265,width=160,height=30)

last_name=Entry(window)
last_name.insert(0,b)
last_name.place(x=790,y=265,width=160,height=30)

user_name=Entry(window)
user_name.insert(0,c)
user_name.place(x=620,y=335,width=330,height=30)

email=Entry(window)
email.insert(0,e)
email.place(x=620,y=405,width=330,height=30)


passwd=Entry(window,show='*')
passwd.insert(0,d)
passwd.place(x=620,y=475,width=160,height=30)
showw=IntVar(value=0)
cb1=Checkbutton(window,text='Show',offvalue=0,variable=showw,bg='white',command=show2)
cb1.place(x=790,y=500)

conf_passwd=Entry(window,show='*')
conf_passwd.insert(0,d)
conf_passwd.place(x=790,y=475,width=160,height=30)
showw2=IntVar(value=0)
cb2=Checkbutton(window,text='Show',offvalue=0,variable=showw2,bg='white',command=show).place(x=620,y=500)

phone_num=Entry(window)
phone_num.insert(0,f)
phone_num.place(x=700,y=565)



#logout function
def logout():
    msb=messagebox.askquestion("Logout","Are you sure you want to logout?")
    if msb=='yes':
          
            window.destroy()
            import login
      
        

#verification for update
 

#update function
def update():
     c.execute("""UPDATE register SET 
        first_name= :first,
        last_name= :last,
        user_name= :user,
        password= :pass,
        phone_num= :phn
        WHERE  email= :em,""",
        {'first':first_name.get(),
        'last':last_name.get(),
        'user' :user_name.get(),
        'pass':passwd.get(),
        'phn':phone_num.get(),
        'em':email.get()
        })
 
    #messagebox after update
     messagebox.showinfo("Accounts","Updated fields successfully!")

#delete function


#update, delete and logout function
Button(window,text="LOGOUT",font=('Arial',10,'bold'),fg='white',bg="black",width=12,height=2,cursor='hand2',command=logout).place(x=860, y=640)


window.mainloop()