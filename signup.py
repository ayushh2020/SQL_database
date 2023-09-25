from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from turtle import clear, heading, st, width
from venv import create
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
#function

def clear():
    emailentry.delete(0,END)
    userentry.delete(0,END)
    passentry.delete(0,END)
    cnfmpassentry.delete(0,END)
    check.set(0)

def connect_database():
    if emailentry.get()=='' or userentry.get()=='' or passentry.get()=='' or cnfmpassentry.get()== '':
        messagebox.showerror("Error,All fields are required")

    elif passentry.get() != cnfmpassentry.get():
        messagebox.showerror("Error, Password Mismatched")

    elif check.get()==0:
        messagebox.showerror("Please accept Terms & conditions")
    
    else:
        try: 
            con=pymysql.connect( host='localhost',user='root',password='root')
            mycursor= con.cursor()
        except:
            messagebox.showerror("Connectivity issue, try again")
            return
        try:
            query= 'create database userdata1'
            mycursor.execute(query)

            query= 'use userdata1'
            mycursor.execute(query)

            query='create table data1(id int auto_inrement primary key not null, Email varchar(50),Username varchar(50), Password varchar(15))'
            mycursor.execute(query)
        
            # query = 'ALTER TABLE data1 MODIFY COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY'
            # mycursor.execute(query)                        
        except:
            mycursor.execute('use userdata1')
        
        query='select * from data1 where username = %s'
        mycursor.execute(query,(userentry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror("Error, Username already exists")

        else:
            query= 'insert into data1(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailentry.get(),userentry.get(),passentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Registration successful")
            clear()
            root_sign.destroy()
            import signin

def login_p():
    root_sign.destroy()
    import signin




root_sign= Tk()

root_sign.title('Sign up page')

root_sign.geometry('990x690+50+50')
root_sign.resizable(0,0)



bg_img= ImageTk.PhotoImage(file= 'bg.jpg')
bglabel= Label(root_sign, image= bg_img)
bglabel.grid()
 
frame = Frame(root_sign,bg='white')
frame.place(x=554,y=100)

headinglabel= Label(frame,text='CREATE NEW ACCOUNT',fg='firebrick1',bg='white',width=20)
headinglabel.config(font=('microsoft yahei UI Light' ,15,BOLD))
headinglabel.grid(row=0,column=0,padx=10,pady=10)

emaillabel= Label(frame,text='Email',fg='firebrick1',bg='white',font=('microsoft yahei UI Light' ,10,BOLD))
emaillabel.grid(row=1,column=0,sticky='w',pady=(10,0),padx=25)

emailentry= Entry(frame,width=30,fg='white',bg='firebrick1',font=('microsoft yahei UI Light' ,10,BOLD))
emailentry.grid(row=2,column=0,sticky='w',padx=25)



usernamelabel= Label(frame,text='Username',fg='firebrick1',bg='white',font=('microsoft yahei UI Light' ,10,BOLD))
usernamelabel.grid(row=3,column=0,sticky='w',pady=(10,0),padx=25)

userentry= Entry(frame,width=30,fg='white',bg='firebrick1',font=('microsoft yahei UI Light' ,10,BOLD))
userentry.grid(row=4,column=0,sticky='w',padx=25)


passwordlabel= Label(frame,text='Password',fg='firebrick1',bg='white',font=('microsoft yahei UI Light' ,10,BOLD))
passwordlabel.grid(row=5,column=0,sticky='w',pady=(10,0),padx=25)

passentry= Entry(frame,width=30,fg='white',bg='firebrick1',font=('microsoft yahei UI Light' ,10,BOLD))
passentry.grid(row=6,column=0,sticky='w',padx=25)


cnfmpasswordlabel= Label(frame,text='Confirm Password',fg='firebrick1',bg='white',font=('microsoft yahei UI Light' ,10,BOLD))
cnfmpasswordlabel.grid(row=7,column=0,sticky='w',pady=(10,0),padx=25)

cnfmpassentry= Entry(frame,width=30,fg='white',bg='firebrick1',font=('microsoft yahei UI Light' ,10,BOLD))
cnfmpassentry.grid(row=8,column=0,sticky='w',padx=25)

check= IntVar()
termsbtn= Checkbutton(frame,text='I agree to terms & conditions',fg='firebrick1',bg='white',font=('open sans' ,8,BOLD),cursor='hand2',
activebackground='white',activeforeground='firebrick1', variable=check)
termsbtn.grid(row=9,column=0,padx=20,pady=10,sticky='w')

signupbtn = Button(frame,text='Sign up',fg='white',bg='firebrick1', bd=0,font=('open sans' ,16,BOLD),cursor='hand2',
activebackground='firebrick1',activeforeground='white',width=15,command=connect_database)
signupbtn.grid(row=10,column=0,pady=10)

signlabel= Label(frame,text='Dont have an account ?',fg='firebrick1',bg='white')
signlabel.config(font=('open sans',9))
signlabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

alreadyaccbtn= Button(frame,text='LOG IN', bd=0,bg='white',activebackground='white',
fg='blue',activeforeground='blue' ,cursor='hand2',command=login_p)
alreadyaccbtn.config(font=('open sans' ,9,BOLD))
alreadyaccbtn.place(x=170,y=396)


root_sign.mainloop()
