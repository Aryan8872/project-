from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("1920x1108")
root.config(bg="lavender")



def over_v():
    root.destroy()
    import overview


def rep():
    root.destroy()
    import report


def sts():
    root.destroy()
    import status

#buttons
overview=Button(root,text="OVERVIEW",font=("Helvetica 25 bold"),bg="lightskyblue",command=over_v,width=22)
overview.place(x=1100,y=140)

report=Button(root,text="REPORT",font=("Helvetica 25 bold"),bg="lightskyblue",command=rep,width=22)
report.place(x=1100,y=220)

status=Button(root,text="STATUS",font=("Helvetica 25 bold"),bg="lightskyblue",command=sts,width=22)
status.place(x=1100,y=300)

ov_line=Canvas(root,width=600,height=3,bg="black",highlightthickness=0)
ov_line.place(x=1000,y=212)

report_line=Canvas(root,width=600,height=3,bg="black",highlightthickness=0)
report_line.place(x=1100,y=292)

status_line=Canvas(root,width=600,height=3,bg="black",highlightthickness=0)
status_line.place(x=1100,y=372)

ov_text=LabelFrame(root,width=1100,height=600,bg="lavender")
ov_text.place(x=0,y=134)

ov=Label(ov_text,text="wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
ov.place(x=0,y=0)

#top canvas
topcan=Canvas(root,height=130,width=1800,bg="black")
topcan.place(x=0,y=0)
#bottom canvas
bottomcan=Canvas(root,height=90,width=1800,bg="black")
bottomcan.place(x=0,y=730)

#project title
title1=Label(root,text="MUNICIPAL",bg="black",fg="lavender",font=("Helvetica 40 bold"))
title1.place(x=30,y=10)

title2=Label(root,text="PROBLEM",bg="black",fg="lavender",font=("Helvetica 40 bold"))
title2.place(x=340,y=30)

title3=Label(root,text="RESOLVER",bg="black",fg="lavender",font=("Helvetica 40 bold"))
title3.place(x=620,y=50)

#project logo
proj_logo=ImageTk.PhotoImage(Image.open("logo-white (3).png"))
logo_label=Label(root,image=proj_logo,bd=0)
logo_label.place(x=930,y=10)












##ACCOUNT VIEWING FEATURE 
conn=sqlite3.connect("issues.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS issues(
    date integer,
    urgency string,
    phone_number integer
    

)""")
def acc():
    import account_view

account=Button(root,text="ACCOUNT",font=("Helvetica 15 bold"),command=acc,bd=0,fg="white",bg="black",activebackground="black")
account.place(x=1390,y=50)

# textbox=Text(root,width=20,height=20)
# textbox.pack()
# def submit(): 

#     textfile=open("data.txt",'a')
#     saved=textfile.write(textbox.get(1.0,END))
#     textbox.insert(END,saved)
#     global myimage
#     myimage=filedialog.askopenfilename(initialdir="/",filetypes=(("images","*.jpg"),))
#     file_path=myimage
#     imag=PhotoImage(file=file_path)
#     textbox.image_create(END,image=imag)

# butn=Button(root,text="submit",command=submit)
# butn.pack()
root.mainloop()