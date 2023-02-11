from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk



#create a window
root=Toplevel()
root.geometry("1280x720")
root.title("Accounts")
root.config(bg="lavender")

topcan=Canvas(root,height=80,width=1800,bg="black")
topcan.place(x=0,y=0)

title1=Label(root,text="MUNICIPAL",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title1.place(x=160,y=18)

title2=Label(root,text="PROBLEM",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title2.place(x=330,y=18)

title3=Label(root,text="RESOLVER",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title3.place(x=487,y=18)


#project logo
logo=ImageTk.PhotoImage(Image.open("main_logo.png"))
logo1=Label(root,image=logo,bd=0,bg="black",height=70)
logo1.place(x=640,y=5)

logo_2=ImageTk.PhotoImage(Image.open("second.png"))
logo2=Label(root,image=logo_2,bd=0,bg="black",height=60,width=150)
logo2.place(x=0,y=10)




#Frame for account details
frame=LabelFrame(root, height=450, width=450, bg='skyblue')
frame.place(x=500, y=150)

#label for account details
un=Label(frame,text="User Name:",font=('Arial',10,'bold'),bg='white')
un.place(x=20,y=20)
em=Label(frame,text="Email:",font=('Arial',10,'bold'),bg='white').place(x=240,y=20)
pwd=Label(frame,text="Password:",font=('Arial',10,'bold'),bg='white').place(x=20,y=90)
phn=Label(frame,text="Phone number:",font=('Arial',10,'bold'),bg='white').place(x=20,y=160)
add=Label(frame,text="Address:",font=('Arial',10,'bold'),bg='white').place(x=20,y=230)
ward=Label(frame,text="Ward:",font=('Arial',10,'bold'),bg='white').place(x=20,y=300)
gender=Label(frame,text="Gender",font=('Arial',10,'bold'),bg="white").place(x=20,y=370)


#fetch user data
try:
    conn=sqlite3.connect('registration.db')
    c=conn.cursor()
    c.execute("SELECT * from register WHERE user_status=:act",{'act':True})
    records=c.fetchall()
    a=records[0][0]
    b=records[0][1]
    c=records[0][2]
    d=records[0][3]
    e=records[0][4]
    f=records[0][5]
    g=records[0][6]
    
    conn.commit()
    conn.close()
except:
    a="User name"
    b="Password"
    c="Phone number"
    d="E-mail"
    e="Address"
    f="Ward"
    g="Gender"
    h="OID"

#entry box
un_entry=Entry(frame,font=('Arial',12,'bold'))
un_entry.insert(0,a)
un_entry.place(x=20,y=50)

em_entry=Entry(frame,font=('Arial',12, 'bold'))
em_entry.place(x=240,y=50)
em_entry.insert(0,d)

pwd_entry=Entry(frame,font=('Arial',12,'bold'))
pwd_entry.place(x=20,y=120)
pwd_entry.insert(0,b)

phn_entry=Entry(frame,font=('Arial',12,'bold'))
phn_entry.place(x=20,y=190)
phn_entry.insert(0,c)

add_entry=Entry(frame,font=('Arial',12,'bold'))
add_entry.place(x=20,y=260)
add_entry.insert(0,e)

ward_entry=Entry(frame,font=('Arial',12,'bold'))
ward_entry.place(x=20,y=330)
ward_entry.insert(0,f)

gender_entry=Entry(frame,font=('Arial',12,'bold'))
gender_entry.place(x=20,y=400)
gender_entry.insert(0,g)


#show password functions
# def show():
#     if (showw.get()==1):
#         passwd.config(show='')
#     else:
#         passwd.config(show='*')
# def show2():
#     if (showw2.get()==1):
#         conf_passwd.config(show='')
#     else:
#         conf_passwd.config(show='*')


#Entries for Account


# ward.insert()
# ward.place()


# phone_num=Entry(window)
# phone_num.insert(0,f)
# phone_num.place(x=700,y=565)



#logout function
def logout():
    msb=messagebox.askquestion("Logout","Are you sure you want to logout?")
    if msb=='yes':
        conn=sqlite3.connect('registration.db')
        c=conn.cursor()
        c.execute("""UPDATE register SET
            user_status= :off
            WHERE user_status= :on""",
            {
                'off':False,
                'on':True
            })
        conn.commit()
        conn.close()
        if msb=='yes':
            root.destroy()
            import login
        elif msb=='No':

            import account_view
    
        
  
      

logout_btn=Button(root,text="LOGOUT",font=('Arial',10,'bold'),fg='white',bg="black",width=12,height=2,cursor='hand2',command=logout).place(x=860, y=640) 

#verification for update
 

# #update function
# def update():
#     conn=sqlite3.connect("registration.db")
#     c=conn.cursor()
#     c.execute("""UPDATE register SET 
#         password= :pass,
#         phone_num= :phn,
#         email= :em,
#         address= :addr,
#         ward no= :ward,
#         gender= :gen,
#         WHERE  user_status= :state,""",
#         {
#         'pass':pwd_entry.get(),
#         'phn':phn_entry.get(),
#         'em':em_entry.get(),
#         'addr':add_entry.get(),
#         'ward':ward_entry.get(),
#         'state':True
#         })
 
#     #messagebox after update
#     messagebox.showinfo("Accounts","Updated fields successfully!")
# conn.commit()
# conn.close()

#delete function


#update, delete and logout function


root.mainloop()