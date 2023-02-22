from tkinter import *
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.geometry("1920x1108")

root_bg=ImageTk.PhotoImage(Image.open("images\\logo-white (4).png"))
bg=Label(root,image=root_bg)
bg.place(x=1120,y=0)

#top black canvas
topcan=Canvas(root,height=80,width=1800,bg="black")
topcan.place(x=0,y=0)

#frame for widgets 
frame1=LabelFrame(root,width=1200,height=690,bg="lavender")
frame1.place(x=0,y=80)

#bottom black canvas
bottomcan=Canvas(root,height=50,width=1800,bg="black")
bottomcan.place(x=0,y=750)


#project title on black canvas
title1=Label(root,text="MUNICIPAL",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title1.place(x=160,y=18)

title2=Label(root,text="PROBLEM",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title2.place(x=330,y=18)

title3=Label(root,text="RESOLVER",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title3.place(x=487,y=18)

title4=Label(root,text="ADMIN'S PAGE",bg="black",fg="lavender",font=("Helvetica 20 bold"))
title4.place(x=800,y=18)

#project logo on black canvas
proj_logo=ImageTk.PhotoImage(Image.open("images\\main_logo.png"))
logo_label=Label(root,image=proj_logo,bd=0,bg="black",height=70)
logo_label.place(x=640,y=5)

proj_logo2=ImageTk.PhotoImage(Image.open("images\\second.png"))
logo_label2=Label(root,image=proj_logo2,bd=0,bg="black",height=60,width=150)
logo_label2.place(x=0,y=10)


#Entering problem solved username
Labe1=Label(frame1,text="# CHANGE STATUS",font=("Helvetica 15 bold"),bg="lavender")
Labe1.place(x=60,y=40)

#username label
un_label=Label(frame1,text="Username",font=("Helvetica 13 bold"),bg="lavender")
un_label.place(x=60,y=90)

#username entry
un_entry=Entry(frame1,font=("Helvetica 11 bold"))
un_entry.place(x=60,y=120)

#progress
pg=Label(frame1,text="#Progress",font=("Helvetica 13 bold"),bg="lavender")
pg.place(x=60,y=160)

#progress entry
pg_entry=Entry(frame1,font=("Helvetica 11 bold"))
pg_entry.place(x=60,y=190)

#progress indicator
blue=Label(frame1,bg="blue",text=" ",font=("Helvetica 11 bold"),padx=10)
blue.place(x=250,y=100)
blue_mean=Label(frame1,text="= REPORT RECEIVED",font=("Helvetica 9 bold"),bg="lavender")
blue_mean.place(x=280,y=100)

red=Label(frame1,text=" ",bg="red",font=("Helvetica 11 bold"),padx=10)
red.place(x=250,y=140)
red_mean=Label(frame1,text="= HELP IS ON THE WAY",font=("Helvetica 9 bold"),bg="lavender")
red_mean.place(x=280,y=140)

green=Label(frame1,text=" ",bg="green",font=("Helvetica 11 bold"),padx=10)
green.place(x=250,y=180)
green_mean=Label(frame1,text="= PROBLEM RESOLVED",font=("Helvetica 9 bold"),bg="lavender")
green_mean.place(x=280,y=180)


def refresh():
    root.destroy()
    import admin_control

#refresh button
ref=Button(frame1,text="REFRESH",font=("Helvetica 9 bold"),command=refresh)
ref.place(x=150,y=220)

#problem status label above its table
prob_s=Label(frame1,text="PROBLEM STATUS",font=("Helvetica 15 bold"),fg="green",bg="lavender")
prob_s.place(x=180,y=330)

#registered user label above its table
reg_us=Label(frame1,text="REGISTERED USERS",font=("Helvetica 15 bold"),fg="green",bg="lavender")
reg_us.place(x=780,y=125)

#CONNECTING TO DATABASE AND CHANGING THE PROBLEM'S STATUS
def change():
    col=pg_entry.get()
    conn=sqlite3.connect("registration.db")           
    c=conn.cursor()
    c.execute("SELECT * from register WHERE user_name=?",[(un_entry.get())])  #selecting  data from registration database for verification
    record=c.fetchall()
    if record and 'red' in col or 'green' in col or 'blue' in col :
        conn=sqlite3.connect("status.db")
        c=conn.cursor()
        c.execute("""UPDATE status SET
                problem_status= :sts
                WHERE user_name= :un""",
                {
                    'un':un_entry.get(),
                    'sts':pg_entry.get()
                })
        conn.commit()
        conn.close()
        messagebox.showinfo("success","changed sucessfully!")
    elif not record:
        messagebox.showerror("error!","username doesnot exist")
    elif not('red' in col or 'green' in col or 'blue' in col):
        messagebox.showerror("error!","enter valid color")

#change button
change_btn=Button(frame1,text="Change",font=("Helvetica 9 bold"),command=change)
change_btn.place(x=60,y=220)



#table for problem status
def tbl():
 
    table=LabelFrame(frame1,height=580,width=950,bg='white')
    table.place(x=30,y=360)
  
    try:
        #try fetching data from database
        conn=sqlite3.connect('status.db')
        c=conn.cursor()
        c.execute("SELECT oid ,user_name ,first_name ,last_name, problem_status from status")
        lst=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst=[]
    finally:
        #Table headings
        lst.insert(0,('ID','user_name' ,'first_name' ,'last_name', 'problem_status'))
        print(lst)
    #creating a table
    total_rows =len(lst)
    total_columns=len(lst[0])
    for i in range(total_rows):
        if i==0:
            #table heading
            fontt=('Arial',10,'bold')
            jus=CENTER
            bgc ='#9cc2e5'
        else:
            #table data
            fontt=('Arial',10)
            jus=LEFT
            bgc='white'
        for j in range(total_columns):
            #width for all columns
            if j==0:
                wid=5
            elif j==1 or j==2:
                wid=17
            elif j==3:
                wid=15
            elif j==4:
                wid=20
            elif j==5:
                wid=15
            elif j==6:
                wid=15
            elif j==7:
                wid=15
            elif j==8:
                wid=15
            else:
                wid=5
            e=Entry(
                table,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            e.grid(row=i,column=j)
            e.insert(0,lst[i][j])
            e.config(state=DISABLED)
           

#calling table function
tbl()


#table for registration database
def tbl2():
    table2=LabelFrame(frame1,height=580,width=650,bg='white')
    table2.place(x=620,y=160)

    try:
        #try fetching data from database
        conn=sqlite3.connect('registration.db')
        c=conn.cursor()
        c.execute("SELECT oid ,user_name , phone_num , email, address, ward, gender from register")
        lst2=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst2=[]
    finally:
        #Table headings
        lst2.insert(0,('ID','user_name' , 'phone_num' , 'email', 'address', 'ward', 'gender'))
        print(lst2)
    #creating a table
    total_rows2 =len(lst2)
    total_columns2=len(lst2[0])
    for i in range(total_rows2):
        if i==0:
            #table heading
            fontt=('Arial',10,'bold')
            jus=CENTER
            bgc ='#9cc2e5'
        else:
            #table data
            fontt=('Arial',10)
            jus=LEFT
            bgc='white'
        for j in range(total_columns2):
            #width for all columns
            if j==0:
                wid=5
            elif j==1:
                wid=10
            elif j==2:
                wid=17
            elif j==3:
                wid=15
            elif j==4:
                wid=15
            elif j==5:
                wid=5
            elif j==6:
                wid=8
            elif j==7:
                wid=15
            elif j==8:
                wid=15
            else:
                wid=5
            f=Entry(
                table2,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            f.grid(row=i,column=j)
            f.insert(0,lst2[i][j])
            f.config(state=DISABLED)

#calling table function
tbl2()





def editstatus():
    sts=Toplevel()
    sts.geometry("200x200")
    sts.title("status")

    label1=Label(sts,text="ENTER THE OID")
    label1.place(x=0,y=80)
    entry1=Entry(sts,font=("Helvetica 9 bold"))
    entry1.place(x=0,y=20)

    def del_rec():
        conn=sqlite3.connect("status.db")
        c=conn.cursor()
        c.execute("DELETE from status WHERE oid = " + entry1.get())
        conn.commit()
        conn.close()
        messagebox.showinfo("sucess","deleted sucessfully!")
    btn1=Button(sts,text="DELETE",font=("Helvetica 9 bold"),bg="red",fg="white",command=del_rec)
    btn1.place(x=0,y=40)

edit_sts=Button(root,text="Edit status table",bg="green",fg="white",font=("Helvetica 9 bold"),command=editstatus)
edit_sts.place(x=1220,y=530)



def editreport():
     rept=Toplevel()
     rept.geometry("900x600")
     rept.config(bg="lavender")

     #table for  report database
     def tbl3():
        table3=LabelFrame(rept,height=580,width=650,bg='white')
        table3.place(x=0,y=70)

        try:
            #try fetching data from database
            conn=sqlite3.connect('report.db')
            c=conn.cursor()
            c.execute("SELECT oid,first_name,last_name,ward_no,tole,issue,description,level,date from rep")
            lst3=c.fetchall()
            conn.commit()
            conn.close()
        except:
            #empty list if list doesn't exist
            lst3=[]
        finally:
            #Table headings
            lst3.insert(0,( 'ID','First name','Last name' , 'Ward num' , 'Tole', 'Issue', 'Description', 'Level','Date'))
            print(lst3)
        #creating a table
        total_rows3 =len(lst3)
        total_columns3=len(lst3[0])
        for i in range(total_rows3):
            if i==0:
                #table heading
                fontt=('Arial',10,'bold')
                jus=CENTER
                bgc ='#9cc2e5'
            else:
                #table data
                fontt=('Arial',10)
                jus=LEFT
                bgc='white'
            for j in range(total_columns3):
                #width for all columns
                if j==0:
                    wid=3
                elif j==1:
                    wid=10
                elif j==2:
                    wid=10
                elif j==3:
                    wid=5
                elif j==4:
                    wid=10
                elif j==5:
                    wid=13
                elif j==6:
                    wid=40
                elif j==7:
                    wid=15
                elif j==8:
                    wid=13
                
                else:
                    wid=5
                f=Entry(
                    table3,
                    width=wid,
                    font=fontt,
                    justify=jus,
                    disabledforeground='black',
                    disabledbackground=bgc
                )
                f.grid(row=i,column=j)
                f.insert(0,lst3[i][j])
                f.config(state=DISABLED)

    #calling table function
     tbl3()

     tablelabel=Label(rept,text="REPORTS",font=("Helvetica 15 bold"),fg="green",bg="lavender").place(x=350,y=40)
     label1=Label(rept,text="ENTER THE OID")
     label1.place(x=0,y=390)
     entry1=Entry(rept,font=("Helvetica 9 bold"))
     entry1.place(x=0,y=420)

     def del_rep():
        conn=sqlite3.connect("report.db")
        c=conn.cursor()
        c.execute("DELETE from rep WHERE oid = " + entry1.get())
        conn.commit()
        conn.close()
        messagebox.showinfo("sucess","deleted sucessfully!")
     btn1=Button(rept,text="DELETE",font=("Helvetica 9 bold"),bg="red",fg="white",command=del_rep)
     btn1.place(x=0,y=450)
     def refrept():
        rept.destroy()
        editreport()
     btn2=Button(rept,text="REFRESH",font=("Helvetica 9 bold"),bg="red",fg="white",command=refrept)
     btn2.place(x=60,y=450)

edit_repo=Button(root,text="Edit report table",bg="green",fg="white",font=("Helvetica 9 bold"),command=editreport)
edit_repo.place(x=1350,y=530)




root.mainloop()