from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

#screen command
signup = Tk()
signup.title("Signup")
signup.geometry("")

#main frame
frame = LabelFrame(signup, padx=50, pady=100)
frame.grid(row=1, column=1, padx=20, pady=20,  sticky="")

#icon
signup.iconbitmap(os.getenv('ICON'))

#signup image
my_img_signup = ImageTk.PhotoImage(Image.open(os.getenv('SIGNUP_PNG')))
my_label_signup = Label(frame, image = my_img_signup)
my_label_signup.grid(row=0,column=0, columnspan=3)

#mysql stuff
userdb = sqlite3.connect("ignition.db")

cur = userdb.cursor()

#Submit function
def submit():
    global radio
    global cur
    global input_field_user
    global input_field_pssw
    
    #customer employee conditioning
    
    if input_field_user.get() == "":
        uname.destroy()
        uname = Label(frame, text="Input Username")
        uname.grid(row=1, column=0, columnspan=3)

    elif input_field_pssw.get() == "" :
        uname.destroy()
        uname = Label(frame, text="Input Password")
        uname.grid(row=1, column=0, columnspan=3)
    else:
        if radio.get() == "cust":
            #for customer
            cur.execute(f"insert into user values(NULL, '{input_field_user.get()}', '{input_field_pssw.get()}', 'cust')")
            userdb.commit()
            #announcement
            announce = Label(frame, text="you have successfully signed in").grid(row=0, column=0, columnspan=3)
       
        elif radio.get() == "emp":
            #for employees
            cur.execute(f"insert into user values(NULL, '{input_field_user.get()}', '{input_field_pssw.get()}', 'emp')")
            userdb.commit()
            #announcement
            announce = Label(frame, text="you have successfully signed in").grid(row=0, column=0, columnspan=3)       

#Login Function
def login():
    global signup
    signup.destroy()
    exec(open(os.getenv('LOGIN'), 'r').read())
       
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
        b_pass.grid(row=7, column=0)
                
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
        b_pass.grid(row=7, column=0)



#Signup System

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
b_pass.grid(row=7, column=0)
#print(b_pass)

#Employee or customer
radio = StringVar()
Radiobutton(frame, text="Employee",variable=radio, value="emp").grid(row=6, column=0, padx=10, pady=10)
Radiobutton(frame, text="Customer",variable=radio, value="cust").grid(row=6, column=1, padx=10, pady=10)
radio.set(value="cust")

#SIgnup button
b_signup = Button(frame, text="Signup", command=submit)
b_signup.grid(row=7, column=1, pady=0, columnspan=2)

#Login Button
b_login = Button(frame, text="Login", command=login)
b_login.grid(row=8, column=0, columnspan=3, pady=20)

#blank space by Taylor Swift
blank = Label(frame).grid(row=3,column=1)
blank_2 = Label(signup, text="").grid(row=0,column=0)

#mainloop
signup.mainloop()



