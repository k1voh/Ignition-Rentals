from tkinter import *
from PIL import ImageTk,Image
import os
from dotenv import load_dotenv
load_dotenv()


#screen command
cust = Tk()
cust.title("Rent A Bike")

#icon
cust.iconbitmap(os.getenv('ICON'))

#fUNCTIONS

#bike form
def bike():
    cust.destroy()
    exec(open(os.getenv('CUST_FORM'), 'r').read())


#Bike 1

#frame

frame1 = LabelFrame(cust, padx=40, pady=10)
frame1.grid(row=1, column=0, padx=20, pady=20)

#image
my_img1 = ImageTk.PhotoImage(Image.open(os.getenv('BIKE1')))
my_label1 = Label(frame1, image = my_img1)
my_label1.grid(row=0,column=0, columnspan=3)

#Specifications
label1 = Label(frame1, text="DODGE TOMAHAWK (Model No. 51)").grid(row=1, column=1)
label2 = Label(frame1, text="This superbike carries within it an 8277CC 10 valve, four stroke engine that is simply a dream.").grid(row=2, column=1)
label3 = Label(frame1, text="It can clock 0-60 somewhere in between 1.75 – 2.5 seconds and hits its max power of 500 HP at 5600 RPM.").grid(row=3, column=1)
    
#Button
btn1 = Button(frame1, text="Rent Now", command=bike).grid(row=4, column=1)

#Bike 2

#frame

frame2 = LabelFrame(cust, padx=115, pady=10)
frame2.grid(row=1, column=1, padx=20, pady=20)

#image
my_img2 = ImageTk.PhotoImage(Image.open(os.getenv('BIKE2')))
my_label2 = Label(frame2, image = my_img2)
my_label2.grid(row=0,column=0, columnspan=3)

#Specifications
label6 = Label(frame2, text="SUZUKI HAYABUSA (Model No. 69)").grid(row=1, column=1)
label7 = Label(frame2, text="1340cc. It is a four-cylinder , short-stroke, DOHC, 16-valve engine that truly lives up to its hype.").grid(row=2, column=1)
label8 = Label(frame2, text="The Suzuki Hayabusa hits 0-60 in 2.6 seconds and its clutch assists system. It hits its max power of 197 HP at 6750 RPM.").grid(row=3, column=1)

    
#Button
btn2 = Button(frame2, text="Rent Now", command=bike).grid(row=4, column=1)

#Bike 3

#frame

frame3 = LabelFrame(cust, padx=100, pady=10)
frame3.grid(row=2, column=0, padx=20, pady=20)

#image
my_img3 = ImageTk.PhotoImage(Image.open(os.getenv('BIKE3')))
my_label3 = Label(frame3, image = my_img3)
my_label3.grid(row=0,column=0, columnspan=3)

#Specifications
label11 = Label(frame3, text="MTT TURBINE SUPERBIKE (Model No. 328)").grid(row=1, column=1)
label12 = Label(frame3, text="features the Rolls-Royce 250-C18 turboshaft engine with a 2-speed semi-automatic transmission.").grid(row=2, column=1)
label13 = Label(frame3, text="his bike can get from 0-60 in just 2.5 seconds, hits its max power of 320 HP at 52000 RPM.").grid(row=3, column=1)
    
#Button
btn3 = Button(frame3, text="Rent Now", command=bike).grid(row=4, column=1)

#Bike 4

#frame

frame4 = LabelFrame(cust, padx=100, pady=10)
frame4.grid(row=2, column=1, padx=20, pady=20)

#image
my_img4 = ImageTk.PhotoImage(Image.open(os.getenv('BIKE4')))
my_label4 = Label(frame4, image = my_img4)
my_label4.grid(row=0,column=0, columnspan=3)

#Specifications
label16 = Label(frame4, text="KAWASAKI NINJA H2R (Model No. 67)").grid(row=1, column=1)
label17 = Label(frame4, text="a 998CC liquid cooled, 4 stroke , in-line four, DOHC, 16-valve engine this thing can go fast, and we mean fast!").grid(row=2, column=1)
label18 = Label(frame4, text="The Kawasaki Ninja H2R hits 60 in a mere 2.5 seconds. Now that is fast! The bike hits it max power of 197.3 bHP at 11,000 RPM.").grid(row=3, column=1)
    
#Button
btn4 = Button(frame4, text="Rent Now", command=bike).grid(row=4, column=1)

#mainloop
cust.mainloop()