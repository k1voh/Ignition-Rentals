from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import os
from dotenv import load_dotenv
import threading
load_dotenv()

#sql stuff
userdb = sqlite3.connect("ignition.db")
cur = userdb.cursor()

#screen command
login = Tk()
login.title("Login")
login.geometry("")

#main frame
frame = LabelFrame(login, padx=50, pady=100)
frame.grid(row=1, column=1, padx=20, pady=20,  sticky="")

#icon
login.iconbitmap(os.getenv('ICON'))

#login image
my_img = ImageTk.PhotoImage(Image.open(os.getenv('LOGIN_PNG')))
my_label = Label(frame, image = my_img)
my_label.grid(row=0,column=0, columnspan=3)

#sql stuff
cur.execute('select u_name, pass from user')
user_table = cur.fetchall()

def submit():
    global input_field_pssw
    global input_field_user
    global user_table
    global cur
    global uname
    
    for i,j in user_table:
        if i == input_field_user.get() and j == input_field_pssw.get():
            cur.execute(f"select tag from user where u_name = '{input_field_user.get()}'")
            tag = cur.fetchone()
            if 'own' in tag:
                login.destroy()
                exec(open(os.getenv('OWNER'), 'r').read())
            elif 'emp' in tag:
                login.destroy()
                exec(open(os.getenv('EMP'), 'r').read())
            elif 'cust' in tag:
                login.destroy()
                exec(open(os.getenv('CUST_BIKE'), 'r').read())
            break
        elif input_field_user.get() == "":
            uname.destroy()
            uname = Label(frame, text="Input Username")
            uname.grid(row=1, column=0, columnspan=3)

        elif input_field_pssw.get() == "" :
            uname.destroy()
            uname = Label(frame, text="Input Password")
            uname.grid(row=1, column=0, columnspan=3)
        
        elif (input_field_pssw.get(),input_field_user.get()) not in user_table:
            uname.destroy()
            uname = Label(frame, text="Information not present in database")
            uname.grid(row=1, column=0, columnspan=3)


#Signup Function
def signup():
    login.destroy()
    exec(open(os.getenv('SIGNUP'), 'r').read())
    


#Function
a = 1

def pssw_show():
    global e
    global a
    global input_field_pssw
    global passw
    

    if a == 1:
        #entry box
        e = input_field_pssw.get()
        input_field_pssw = Entry(frame, width=20, show="")
        input_field_pssw.grid(row=5, column=1, columnspan=2)
        input_field_pssw.insert(0, e)
        #decision variable
        a = 2
        #button
        b_pass = Button(frame, text="Hide Password", command=pssw_show)
        b_pass.grid(row=6, column=0)
                
    else:
        #entry box
        e = input_field_pssw.get()
        input_field_pssw = Entry(frame, width=20, show="*")
        input_field_pssw.grid(row=5, column=1, columnspan=2)
        input_field_pssw.insert(0, e)
        #decision variable
        a = 1
        #button
        b_pass = Button(frame, text="Show Password", command=pssw_show)
        b_pass.grid(row=6, column=0)

#text on screen 

user = Label(frame, text="Username:").grid(row=2, column=0)
pssw = Label(frame, text="Password:").grid(row=5, column=0)

#user input box
input_field_user = Entry(frame, width=20)
input_field_user.grid(row=2, column=1, columnspan=2)

input_field_pssw = Entry(frame, width=20, show="*")
input_field_pssw.grid(row=5, column=1, columnspan=2)


#Show password
b_pass = Button(frame, text="Show Password", command=pssw_show)
b_pass.grid(row=6, column=0)


#login button

b_login = Button(frame, text="Login", command=submit)
b_login.grid(row=6, column=1, pady=30, columnspan=2)

#signup button

b_signup = Button(frame, text="Signup", command=signup)
b_signup.grid(row=7, column=0, columnspan=3)

#blank space by Taylor Swift
blank = Label(frame).grid(row=3,column=1)
blank_2 = Label(login, text="").grid(row=0,column=0)
#Blank Label
uname = Label(frame, text="")
uname.grid(row=1, column=0, columnspan=3)

#mainloop
login.mainloop()