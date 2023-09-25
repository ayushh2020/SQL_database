from cProfile import label
from cgi import test
from operator import imod
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from turtle import heading
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

#fuction

def forget_pass():
    def change_pass():
        if user_entry.get()=='' or pass_entry.get()=='' or confmpass_entry.get()=='':
            messagebox.showerror("Error, all fields are required",parent= window)
        elif pass_entry.get() != confmpass_entry.get():
            messagebox.showerror("Error, Mistached password",parent= window)
        else:
            con=pymysql.connect( host='localhost',user='root',password='root')
            mycursor= con.cursor()
            print("hello")

            query= 'use userdata1'
            mycursor.execute(query)

            query= 'select * from data1 where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row= mycursor.fetchone()
            if row==None:
                messagebox.showerror("Invalid username",parent= window)
            else:
                query='update data1 set password = %s where username =%s'
                mycursor.execute(query,(pass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Reset password successful")
                window.destroy()



    window= Toplevel()
    window.title("Change password")
    
    bgpic= ImageTk.PhotoImage(file= 'background.jpg')
    bglabel= Label(window, image=bgpic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font =('arial', '18', 'bold'),
    bg='white', fg='magenta2')
    heading_label.place(x=488, y=60)

    UserLabel = Label(window, text='Username', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    UserLabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0) 
    user_entry.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='orchid1').place (x=470, y=188)

    password_label= Label(window, text='New Password', font=('arial', 12, 'bold'),bd=0,bg='white', fg='orchid1')
    password_label.place(x=470,y=210)
    
    pass_entry= Entry(window,width=25,fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    pass_entry.place(x=470,y=240)
    Frame(window, width=250, height=2, bg='orchid1').place (x=470, y=265)

    
    confmpass_label= Label(window, text='Confirm New Password', font=('arial', 12, 'bold'),bd=0,bg='white', fg='orchid1')
    confmpass_label.place(x=470,y=290)
    
    confmpass_entry= Entry(window,width=25,fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    confmpass_entry.place(x=470,y=320)
    Frame(window, width=250, height=2, bg='orchid1').place (x=470, y=340)

    submit_btn= Button(window, text='Submit',bd=0,bg='magenta2',fg='white', font=('open sans',16,'bold'),cursor='hand2',
    width=19,activebackground='magenta2',activeforeground='white',command=change_pass)
    submit_btn.place(x=470,y=398)

   
                      
    window.mainloop()

def login_btn():
    if userentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror("Error, All fields are required")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root')
            mycursor= con.cursor()
            print("hello")
        except:
            messagebox.showerror("Connectivity issue, try again")
            return

        query= 'use userdata1'
        mycursor.execute(query)
        query= 'select * from data1 where username= %s and password = %s'
        mycursor.execute(query,(userentry.get(),passwordentry.get()))
        row= mycursor.fetchone()
        if row==None:
            messagebox.showerror("Invalid username or password")

        else:
            messagebox.showinfo("Login Successfully")

    

def sign_p():
    root_login.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordentry.config(show='*')
    eyebtn.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordentry.config(show='')
    eyebtn.config(command=hide)



def on_Uenter(event):
    if userentry.get()== 'Username':
        userentry.delete(0,END)

def on_Penter(event):
    if passwordentry.get()== 'Password':
        passwordentry.delete(0,END)

#GUI

root_login = Tk()
root_login.title('Login page')


root_login.geometry('990x690+50+50')
root_login.resizable(0,0)

bg_img= ImageTk.PhotoImage(file= 'bg.jpg')
bglabel= Label(root_login, image= bg_img)
bglabel.place(x=0,y=0)

headinglabel= Label(root_login,text='USER LOGIN',fg='firebrick1',bg='white')
headinglabel.config(font=('microsoft yahei UI Light' ,23,BOLD))
headinglabel.place(x=605,y=120)


#username

userentry= Entry(root_login,width=25,fg='firebrick1',bd=0)
userentry.config(font=('microsoft yahei UI Light' ,11,BOLD))
userentry.place(x=605,y=200)
userentry.insert(0,'Username')

userentry.bind('<FocusIn>',on_Uenter)

frame1= Frame(root_login,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)


#password

passwordentry= Entry(root_login,width=25,fg='firebrick1',bd=0)
passwordentry.config(font=('microsoft yahei UI Light' ,11,BOLD))
passwordentry.place(x=605,y=250)
passwordentry.insert(0,'Password')

passwordentry.bind('<FocusIn>',on_Penter)

frame2= Frame(root_login,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye= PhotoImage(file='openeye.png')
eyebtn= Button(root_login,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebtn.place(x=800,y=255)

forgetbtn= Button(root_login,text='Forget password ? ',bd=0,bg='white',activebackground='white',
fg='firebrick1',activeforeground='firebrick1' ,cursor='hand2',command=forget_pass)
forgetbtn.config(font=('microsoft yahei UI Light' ,9,BOLD))
forgetbtn.place(x=710,y= 300)

loginbtn= Button(root_login,text='LOGIN ', width=22, bd=0,bg='firebrick1',activebackground='firebrick1',
fg='white',activeforeground='firebrick1' ,cursor='hand2',command=login_btn)
loginbtn.config(font=('open sans' ,16,BOLD))
loginbtn.place(x=558,y= 350)

ORLabel= Label(root_login,text='-------------OR-------------',fg='firebrick1',bd=0,bg='white',width=25)
ORLabel.config(font=('open sans',16))
ORLabel.place(x=550,y=400)

facebook= PhotoImage(file='facebook.png')
flabel= Label(root_login,image=facebook,bg='white')
flabel.place(x=640,y=440)

google= PhotoImage(file='google.png')
glabel= Label(root_login,image=google,bg='white')
glabel.place(x=690,y=440)

twitter= PhotoImage(file='twitter.png')
tlabel= Label(root_login,image=twitter,bg='white')
tlabel.place(x=740,y=440)

signlabel= Label(root_login,text='Dont have an account ?',fg='firebrick1',bg='white')
signlabel.config(font=('open sans',9))
signlabel.place(x=580,y=500)

signbtn= Button(root_login,text='Create new account', width=15, bd=0,bg='white',activebackground='white',
fg='blue',activeforeground='firebrick1' ,cursor='hand2',command=sign_p)
signbtn.config(font=('open sans' ,8,BOLD))
signbtn.place(x=716,y= 500)
 
root_login.mainloop()