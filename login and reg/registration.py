from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.geometry("1845x1070")
root.title("Registration page")
root.config(bg="black")

#background image
bacg=ImageTk.PhotoImage(Image.open("login and reg/bgreg2.jpg"))
bac=Label(root,image=bacg,height=1070,width=1845)
bac.place(x=0,y=0)


#title
title=Label(root,text="MUNICIPAL",font=("Helvetica 50 bold"),fg="black",bg="lightpink1")
title.place(x=100,y=190)
title2=Label(root,text="PROBELM",font=("Helvetica 50 bold"),fg="black",bg="lightpink3")
title2.place(x=100,y=270)
title3=Label(root,text="RESOLVER",font=("Helvetica 50 bold"),fg="black",bg="dodgerblue4")
title3.place(x=250,y=350)

#frame
frame=LabelFrame(root,width=600,height=640,bg="black")
frame.place(x=900,y=120)
#frame bg
bac=ImageTk.PhotoImage(Image.open("login and reg/r3.jpg"))
back=Label(frame,image=bac,height=640,width=600)
back.place(x=0,y=0)

#registration page label
reg_label=Label(frame,text="REGISTRATION",fg="white",bg="black",font=("Helvetica 25 bold"))
reg_label.place(x=180,y=0)
page_label=Label(frame,text="PAGE",bg="black",fg="white",font=("Helvetica 25 bold"))
page_label.place(x=255,y=45)

#username label
un_label=Label(frame,text="USERNAME",bg="#040405",font=("Helvetica 10 bold"),fg="white")

un=Entry(frame,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
un_line=Canvas(frame,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

un.place(x=200,y=210)
un_line.place(x=190,y=234)
un_label.place(x=160,y=190)

#email
email_label=Label(frame,text="E-MAIL",bg="#040405",font=("Helvetica 10 bold"),fg="white")

email=Entry(frame,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
email_line=Canvas(frame,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

email.place(x=200,y=270)
email_line.place(x=190,y=294)
email_label.place(x=160,y=250)

#PASSWORD
passwd_label=Label(frame,text="PASSWORD",bg="#040405",font=("Helvetica 10 bold"),fg="white")

passwd=Entry(frame,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
passwd_line=Canvas(frame,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

passwd.place(x=50,y=330)
passwd_line.place(x=35,y=354)
passwd_label.place(x=20,y=310)

#RE-TYPE PASSWORD
re_passwd_label=Label(frame,text="RE-TYPE PASSWORD",bg="#040405",font=("Helvetica 10 bold"),fg="white")

re_passwd=Entry(frame,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
re_passwd_line=Canvas(frame,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

re_passwd.place(x=340,y=330)
re_passwd_line.place(x=325,y=354)
re_passwd_label.place(x=300,y=310)

#PHONE NUMBER
phn_label=Label(frame,text="PHONE-NUMBER",bg="#040405",font=("Helvetica 10 bold"),fg="white")

phn=Entry(frame,font=("Helvetica 14 bold"),bg="gray11",highlightthickness=0,relief=FLAT,fg="#6b6a69")
phn_line=Canvas(frame,width=260,height=2.0,bg="#bdb9b1",highlightthickness=0)

phn.place(x=200,y=390)
phn_line.place(x=190,y=414)
phn_label.place(x=160,y=370)

#register
img=ImageTk.PhotoImage(Image.open("login and reg/button.png"))
btn_lbl=Label(frame,image=img,bg="gray11")
btn_lbl.place(x=200,y=520)
register=Button(frame,text="REGISTER",fg="white",bg="limegreen",font=("Helvetica 15 bold"),activeforeground="limegreen",width=18,bd=0,cursor="hand2")
register.place(x=221,y=532)

#radio button
gender=Label(frame,text="GENDER",bg="gray11",fg="cyan",font=("Helvetica 10 bold"))
gender.place(x=160,y=430)
gender1=Checkbutton(frame,text="male",bg="gray11",font=("Helvetica 10 bold"))
gender1.place(x=200,y=460)
gender2=Checkbutton(frame,text="female",fg="limegreen",bg="gray11",font=("Helvetica 10 bold"))
gender2.place(x=280,y=460)
gender3=Checkbutton(frame,text="other",fg="blue2",bg="gray11",font=("Helvetica 10 bold"))
gender3.place(x=380,y=460)



#already a member
text=Label(frame,text="ALREADY A MEMBER?",font=("Helvetica 10 bold"),fg="red",bg="gray11")
text2=Button(frame,text="LOGIN",bg="gray11",fg="green",activebackground="gray11",bd=0,cursor="hand2")
text.place(x=220,y=600)
text2.place(x=365,y=600)

#radio button

root.mainloop()