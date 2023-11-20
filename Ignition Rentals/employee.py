from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

#sql stuff
userdb = sqlite3.connect("ignition.db")
cur = userdb.cursor()

#screen command
employee = Tk()
employee.title("Employee")
employee.geometry("")

#main frame
frame = LabelFrame(employee, padx=50, pady=100)
frame.grid(row=1, column=1, padx=20, pady=20)

#icon
employee.iconbitmap(os.getenv('ICON'))

#employee image
my_img = ImageTk.PhotoImage(Image.open(os.getenv('EMP_PNG')))
my_label = Label(frame, image = my_img)
my_label.grid(row=0,column=0, columnspan=3)

#Functions
def form():
    employee.destroy()
    exec(open(os.getenv('CUST_FORM'), 'r').read())
    
def Return():
    employee.destroy()
    exec(open(os.getenv('RET_BIKE'), 'r').read())
    
#sql stuff
cur.execute("select u_name from user where tag = 'cust'")
cstmr_list = cur.fetchall()

#Blank Space
info = Label(frame, text="")
info.grid(row=3, column=0, columnspan=3)

#Information Display
    
def deets():
    global info
    global name
    global bike
    global days2
    global pay
        
    cstmr_list = list(var.get())
        
    #removing certain common things
    cstmr_list.remove("(")
    cstmr_list.remove(")")
    cstmr_list.remove("'")
    cstmr_list.remove(",")
    cstmr_list.remove("'")
    
    #empty string
    u_name = ""
    
    #iterating list
    for i in cstmr_list:
        u_name += i

    cur.execute(f"select * from customer where name = '{u_name}'")
    res = cur.fetchone()
    
    if res is not None:
        
        #fetching the values in the list
        name = res[1]
        bike = res[2]
        days2 = res[3]
        pay = res[4]    
        
        #displaying the fetched information
        deet = f"{name} has rented bike {bike} for {days2} days and has agreed to pay Rs{pay}/-"
        info.destroy()
        info = Label(frame, text=deet)
        info.grid(row=3, column=0, columnspan=3)
        
    else:
        
        #making the employee aware of the customer's invalid information
        deet = "one of the information for this customer is empty, kindly fill it beforehand"
        info.destroy()
        info = Label(frame, text=deet)
        info.grid(row=3, column=0, columnspan=3)

#Welcome label
wlcm = Label(frame, text="welcome employee!").grid(row=1, column=1)


#button
enrl = Button(frame, text="Enroll Customer", borderwidth=3, command=form).grid(row=2, column=0)
get = Button(frame, text="Get Details", command = deets ).grid(row=4, column=1)
ret = Button(frame, text="Return Bike", command=Return).grid(row=2, column=2)


#Dropdowm
#customer variable
var = StringVar()
enrl = OptionMenu(frame, var, *cstmr_list).grid(row=2, column=1)

#mainloop
employee.mainloop()
