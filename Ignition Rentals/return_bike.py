from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

#window
return_bike=Tk()
return_bike.title("Bike Return")

#sql
db= sqlite3.connect("ignition.db")
cur = db.cursor()

#main frame
frame = LabelFrame(return_bike, padx=50, pady=100)
frame.grid(row=1, column=1, padx=20, pady=20,  sticky="")

#icon
return_bike.iconbitmap(os.getenv('ICON'))

#Logo
my_img = ImageTk.PhotoImage(Image.open(os.getenv('FORM_PNG')))
my_label = Label(frame, image = my_img)
my_label.grid(row=0,column=0, columnspan=3)

def Return():
    global cur
    global input_field_user
    
    u_name = input_field_user.get()
    #sql stuff

    #selecting the name of the bike rented by the user
    cur.execute(f"select bike from customer where name = '{u_name}' ")
    bike = cur.fetchone()
    bike = bike[0]
    
    #updating the bike stocks
    cur.execute(f"update bikes set stock = stock+1 where name = '{bike}' ")

    #deleting the customer data from the table
    cur.execute(f"delete from customer where name = '{u_name}' ")
    
    #comitting the changes made
    db.commit()
    
    #info display
    deet = "Return Successful!"
    info = Label(frame, text=deet)
    info.grid(row=1,column=0, columnspan=3)

#username entry
user = Label(frame, text="Username:").grid(row=2, column=1, sticky="WE")

input_field_user = Entry(frame, width=20)
input_field_user.grid(row=2, column=2, columnspan=1, pady=10, sticky='W')

#button
b_Return = Button(frame, text="Return", command=Return)
b_Return.grid(row=3, column=1, columnspan=2,)

#mainloop
return_bike.mainloop()