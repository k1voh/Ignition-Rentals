from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()


form_win=Tk()
form_win.title("Form Window")
db=sqlite3.connect("ignition.db")

#main frame
frame = LabelFrame(form_win, padx=50, pady=100)
frame.grid(row=1, column=1, padx=20, pady=20,  sticky="")

#Logo
my_img = ImageTk.PhotoImage(Image.open(os.getenv('SIGNUP_PNG')))
my_label = Label(frame, image = my_img)
my_label.grid(row=0,column=0, columnspan=3)

#Python-based form
def form():
    cur=db.cursor()

    x=model_in.get()
    y=days_in.get()
    
    name=str(name_in.get())
    model=int(x)
    days=int(y)
    days2=str(days)
    bike=0
    
    if model==51:
        pay=str(days*80000)
        bike='Dodge Tomahawk'
    elif model==69:
        pay=str(days*76000)
        bike='Suzuki Hayabusa'
    elif model==328:
        pay=str(days*76000)
        bike='MTT Turbine Superbike Y2K'
    elif model==67:
        pay=str(days*54000)
        bike='Kawasaki Ninja H2R'
    else:
        messagebox.showerror("Error!", 'You have put an invalid model no.')
    
    cur.execute("select stock from bikes where model_no="+str(model))
    stock=cur.fetchone()
    
    if stock[0]>0:
        command="insert into customer values(NULL , '"+name+"', '"+bike+"', "+days2+", "+pay+")"
        update="update bikes set stock=stock-1 where model_no="+str(model)
        
        response = messagebox.askyesno("Ignition Rentals", "Please confirm the following information: You, "+name+", are renting a "+bike+" for "+days2+" days, with a payment of "+pay+"/- rupees.")
    
        if response==True:
            cur.execute(command)
            cur.execute(update)
            db.commit()
            success=Label(frame, text="Registered successfully!!")
            success.grid(row=5, columnspan=2)
    else:
        messagebox.showerror("Error!", 'Selected bike is out of stock. Please select different bike.')
     

#GUI Elements
name=Label(frame, text="Username :")
name_in=Entry(frame)
model=Label(frame, text="Bike Model No. :")
model_in=Entry(frame)
days=Label(frame, text="No. of rent days :")
days_in=Entry(frame)

#GUI Arrangement
name.grid(row=1, column=0, pady=10)
name_in.grid(row=1, column=1, pady=10)
model.grid(row=2, column=0, pady=10)
model_in.grid(row=2, column=1, pady=10)
days.grid(row=3, column=0, pady=10)
days_in.grid(row=3, column=1, pady=10)

#Button
button=Button(frame, text="Submit Form", command=form)
button.grid(row=4, columnspan=2, pady=5)

form_win.mainloop()