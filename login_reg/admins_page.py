#import modules
import sqlite3
from tkinter import *
from tkinter import messagebox

#create a window
window=Tk()
window.geometry("1280x720")
window.title("Customer Details")


#background image
# photo=PhotoImage(file='background2.png')
# background=Label(window, image=photo).place(x=0,y=0)

#icon for navigation buttons
# icon1=PhotoImage(file='Icons/Room.png')
# icon2=PhotoImage(file='Icons/Customer.png')
# icon3=PhotoImage(file='Icons/Book.png')
# icon4=PhotoImage(file='Icons/Bill.png')
# icon5=PhotoImage(file='Icons/Logout.png')

#connecting page


#navigation panel
Frame(window,height=720,width=350,bg='black').place(x=0,y=0)

#navigation buttons

#value of y for search function
space=295

#search function
def srch():
    #get data from dropdown menu and entry
    Frame(window,height=215,width=20,bg='white').place(x=350,y=295)
    term=clicked.get()
    detail=search.get()

    #database connection
    conn=sqlite3.connect('registration.db')
    c=conn.cursor()
    c.execute("SELECT oid,* from register")
    det=c.fetchall()

    #Searching algorithm
    i=len(det)-1
    while i>=0:
        #searching for customer id
        if term=="Customer ID":
            try:
                #comparing values
                int(detail)
                if det[i][0]!=int(detail):
                    i=i-1
                    if i==-1:
                        break
                else:
                    Label(window,text="\u00BB",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                    break
            except:
                messagebox.showerror("Search","Invalid Customer ID")
                break
        #searching by first name
        elif term=="First Name":
            if det[i][1]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u00BB",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                i=i-1
                if i==-1:
                    break
        #searching by last name
        elif term=="Last Name":
            if det[i][2]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u00BB",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                i=i-1
                if i==-1:
                    break
        #searching by mobile
        elif term=="Mobile":
            if det[i][5]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u00BB",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                break
        #searching by email
        elif term=="Email":
            if det[i][6]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="\u00BB",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=350,y=(space+20*i))
                break
        else:
            pass
    conn.commit()
    conn.close()    

#frame for customer details
Frame(window,height=48,width=930,bg='white').place(x=350,y=150)
Label(window,text='Customer Details',bg='white',font=('Segoe Print',18)).place(x=720,y=150)
Frame(window,bg='white',width=930,height=320).place(x=350,y=190)

#label, dropdown menu for searching
Label(window,text='\u00BB   Search By:',bg='white',font=('Agency FB',16,'bold')).place(x=350,y=198)
clicked=StringVar()
clicked.set("Customer ID")
drop=OptionMenu(window,clicked,"Customer ID","First Name","Last Name","Mobile","Email")
drop.place(x=450,y=198)
drop.config(width=15,background='white')

#entry for searching
search=Entry(window,relief=SOLID)
search.place(x=375,y=235,height=28,width=175)
Button(window, text="Search",font=('Arial',8,'bold'),fg='white',bg="black",width=8,height=1,cursor='hand2',command=srch).place(x=560,y=236)

#table
def tbl():
    table=Frame(window,height=580,width=950,bg='white')
    table.place(x=370,y=280)

    try:
        #try fetching data from database
        conn=sqlite3.connect('registration.db')
        c=conn.cursor()
        c.execute("SELECT oid,first_name,last_name, user_name, email, phone_num from register")
        lst=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst=[]
    finally:
        #Table headings
        lst.insert(0,('ID','First name','Last name','User name','email','phonenumber'))

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

window.mainloop()