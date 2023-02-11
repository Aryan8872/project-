from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("1920x1108")
root.config(bg="skyblue")


def over_v():
    root.destroy()
    import overview

def rep():
    root.destroy()
    import report

def sts():
    root.destroy()
    import status

#top canvas    
topcan=Canvas(root,height=80,width=1800,bg="black")
topcan.place(x=0,y=0)

#bottom canvas
bottomcan=Canvas(root,height=50,width=1800,bg="black")
bottomcan.place(x=0,y=750)

 #project logo
proj_logo=ImageTk.PhotoImage(Image.open("main_logo.png"))
logo_label=Label(root,image=proj_logo,bd=0,bg="black",height=70)
logo_label.place(x=640,y=5)

proj_logo2=ImageTk.PhotoImage(Image.open("second.png"))
logo_label2=Label(root,image=proj_logo2,bd=0,bg="black",height=60,width=150)
logo_label2.place(x=0,y=10)

#buttons
#overviewBUtton
def on_enter(e):
   overview.config(background='black', foreground= "red")

def on_leave(e):
   overview.config(background= 'black', foreground= 'white')

overview=Button(root,text="OVERVIEW",font=("Helvetica 15 bold"),bg="black",command=over_v,fg="white",bd=0)
overview.place(x=890,y=30)

overview.bind('<Enter>', on_enter)
overview.bind('<Leave>', on_leave)

#ReportButton
def on_enter(e):
   report.config(background='black', foreground= "red")

def on_leave(e):
   report.config(background= 'black', foreground= "white")

report=Button(root,text="REPORT",font=("Helvetica 15 bold"),bg="black",fg="white",command=rep,bd=0)
report.place(x=1050,y=30)

report.bind('<Enter>', on_enter)
report.bind('<Leave>', on_leave)

#StatusButton
def on_enter(e):
   status.config(background='black', foreground= "red")

def on_leave(e):
   status.config(background= 'black', foreground= 'white')
status=Button(root,text="STATUS",font=("Helvetica 15 bold"),bg="black",fg="white",command=sts,bd=0)
status.place(x=1200,y=30)

status.bind('<Enter>', on_enter)
status.bind('<Leave>', on_leave)

#account button
def acc():
    import account_view

account=Button(root,text="ACCOUNT",font=("Helvetica 15 bold"),command=acc,bd=0,fg="blue",bg="black",activebackground="black")
account.place(x=1390,y=30)

# #project title
# title1=Label(root,text="MUNICIPAL",bg="skyblue",fg="lavender",font=("Helvetica 13 bold"))
# title1.place(x=160,y=290)

# title2=Label(root,text="PROBLEM",bg="skyblue",fg="lavender",font=("Helvetica 13 bold"))
# title2.place(x=255,y=290)

# title3=Label(root,text="RESOLVER",bg="skyblue",fg="lavender",font=("Helvetica 13 bold"))
# title3.place(x=350,y=290)
#your feed back
text=Label(root,text="YOUR FEEDBACK",bg="skyblue",font=("Helvetica 16 bold"))
text.place(x=450,y=120)


#project title for feedback

mun=Label(root,text="MUNICIPAL",bg="black",fg="lavender",font=("Helvetica 20 bold"))
mun.place(x=160,y=18)

prob=Label(root,text="PROBLEM",bg="black",fg="lavender",font=("Helvetica 20 bold"))
prob.place(x=330,y=18)

resl=Label(root,text="RESOLVER",bg="black",fg="lavender",font=("Helvetica 20 bold"))
resl.place(x=487,y=18)


#canvas
# feedb_line=Canvas(root,height=2.0,width=290,bg="black")
# feedb_line.place(x=160,y=320)

feedb_line2=Canvas(root,height=2.0,width=200)
feedb_line2.place(x=440,y=150)

#feedback appeal
appeal=Label(root,text="WE WOULD LIKE YOUR FEEDBACK TO IMPROVE OUR APPLICATION",font=("Helvetica 14 bold"),bg="skyblue")
appeal.place(x=400,y=190)

appeal2=Label(root,text="WHAT IS YOUR OPINION OF OUR APPLICATION?",font=("Helvetica 14 bold"),bg="skyblue")
appeal2.place(x=480,y=260)

appeal3=Label(root,text="Please leave your feedback below: ",font=("Helvetica 12 bold"),bg="skyblue")
appeal3.place(x=370,y=530)

#username entry
un_label=Label(root,text="Please enter your Username:",font=("Helvetica 12 bold"),bg="skyblue")
un_label.place(x=370,y=410)
un_entry=Entry(root,fg="black",font=("Helvetica 10 "),width=35)
un_entry.place(x=370,y=450)

line=Canvas(root,height=2,width=740)
line.place(x=350,y=390)

#icon buttons
emoji="Happy"
def click(text):
    global emoji
    emoji=text
    em=Label(root,text=emoji,font=("Helvetica 12 bold"),bg="skyblue",width=10)
    em.place(x=650,y=380)
sad_png=PhotoImage(file="fav_icons\\sad.png")
sad=Button(root,image=sad_png,bg="lavender",bd=0,command=lambda:click("Sad"))
sad.place(x=570,y=320)


neutral_png=PhotoImage(file="fav_icons\\neutral.png")
neutral=Button(root,image=neutral_png,bg="lavender",bd=0,command=lambda:click("Neutral"))
neutral.place(x=640,y=320)

satisfied_png=PhotoImage(file="fav_icons\\satis.png")
satisfied=Button(root,image=satisfied_png,bg="lavender",bd=0,command=lambda:click("Satisfied"))
satisfied.place(x=710,y=320)

happy_png=PhotoImage(file="fav_icons\\verhappy.png")
happy=Button(root,image=happy_png,bg="lavender",bd=0,command=lambda:click("Happy"))
happy.place(x=780,y=320)


#text box
txtbox=Text(root,font=("Helvetica 10"),height=5)
txtbox.place(x=370,y=570)

#creating table for database 
conn=sqlite3.connect("feedback.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS feedback(
    user_name text,
    feedback text,
    emoji text
)""")
conn.commit()
conn.close()

#inserting feedback data into database
def submit():

    conn=sqlite3.connect("feedback.db")
    data=txtbox.get(1.0,END)
    c=conn.cursor()
    c.execute("INSERT INTO feedback VALUES(:user_name,:feedback,:emoji)",{
        'user_name':un_entry.get(),
        'feedback':data,
        'emoji':emoji    
    })

    conn.commit()
    conn.close()
    messagebox.showinfo('Success',"Thank you for your feedback!")

#send button
send=Button(root,text="SEND",bg="green",font=("Helvetica 12 bold"),width=15,command=submit)
send.place(x=850,y=700)




root.mainloop()