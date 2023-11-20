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
owner = Tk()
owner.title("Owner")
owner.geometry("")

#main frame
frame = LabelFrame(owner, padx=50, pady=100)
frame.grid(row=1, column=1, padx=20, pady=20)

#icon
owner.iconbitmap(os.getenv('ICON'))

#owner image
my_img = ImageTk.PhotoImage(Image.open(os.getenv('OWNER_PNG')))
my_label = Label(frame, image = my_img)
my_label.grid(row=0,column=0, columnspan=3)
    
#sql stuff
cur.execute("select u_name from user where tag = 'cust'")
cstmr_list = cur.fetchall()
cstmr_list.insert(0,"None")

cur.execute("select u_name from user where tag = 'emp'")
emp_list = cur.fetchall()
emp_list.insert(0,"None")

#Blank Space
info = Label(frame, text="")
info.grid(row=2, column=0, columnspan=3)
    
def deets():
    #calling global variables
    global info
    global cstmr_list
    global emp_list
    global var_cust
    global var_emp
    global info
    global user_list
    global u_name
    global tag
    
    #sql decision making
    
    if var_cust.get() == "None" and var_emp.get() == "None":
        deet = "both None has been selected in Selection Dropdowns"
        info.destroy()
        info = Label(frame, text=deet)
        info.grid(row=2, column=0, columnspan=3)
           
    elif var_cust.get() == "None":
        user_list = list(var_emp.get())
            
        #removing certain common things
        user_list.remove(")")
        user_list.remove("'")
        user_list.remove(",")
        user_list.remove("'")
        user_list.remove("(")
            
        #empty string
        u_name = ""
            
        #iterating list
        for i in user_list:
            u_name += i
            
        #getting if owner selected an employee or a customer
        cur.execute(f"select tag from user where u_name = '{u_name}'")
        tag = cur.fetchone()
            
    elif var_emp.get() == "None":
        user_list = list(var_cust.get())
    
        #removing certain common things
        user_list.remove(")")
        user_list.remove("'")
        user_list.remove(",")
        user_list.remove("'")
        user_list.remove("(")
            
        #empty string
        u_name = ""
            
        #iterating list
        for i in user_list:
            u_name += i
    
        #getting if owner selected an employee or a customer
        cur.execute(f"select tag from user where u_name = '{u_name}'")
        tag = cur.fetchone()    
   
   
    
    if "cust" in tag:

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
            info.grid(row=2, column=0, columnspan=3)
            
        else:
            
            #making the employee aware of the customer's invalid information
            deet = "one of the information for this customer is empty, kindly fill it beforehand."
            info.destroy()
            info = Label(frame, text=deet)
            info.grid(row=2, column=0, columnspan=3)
        
    elif "emp" in tag:
        
        cur.execute(f"select * from employee where name = '{u_name}'")
        res = cur.fetchone()
        
        if res is not None:
            
            #fetching the values in the list    
            name = res[1]
            date = res[2]
            sal = res[3]
            clnt = res[4]
            
            #information display
            deet = f"employee {name} joined on {date} for a salary of {sal} and has brought {clnt} customers"
            info.destroy()
            info = Label(frame, text=deet)
            info.grid(row=2, column=0, columnspan=3)
            
        else:
            
            #making the employee aware of the customer's invalid information
            deet = "one of the information for this employee is empty, kindly fill it beforehand"
            info.destroy()
            info = Label(frame, text=deet)
            info.grid(row=2, column=0, columnspan=3)

#Welcome label
wlcm = Label(frame, text="Welcome Owner!").grid(row=1, column=1)


#button
get = Button(frame, text="Get Details", command = deets).grid(row=3, column=1)

#Dropdowm

#customer variable
var_cust = StringVar()
cstl = OptionMenu(frame, var_cust, *cstmr_list).grid(row=1, column=2)

#Employee dropdown
var_emp = StringVar()
emp1 = OptionMenu(frame, var_emp, *emp_list).grid(row=1, column=0)


#mainloop
owner.mainloop()