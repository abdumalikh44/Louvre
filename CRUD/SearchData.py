from tkinter import *
from tkinter import ttk
from colorama import Cursor
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Malik 123",
    database="louvre"
)


cursor = db.cursor()


def MainMenu1():
    main.destroy()
    import MainMenu1

def my_details():
        try:
            cursor.execute("SELECT * FROM booking WHERE booking_date='"+booking_date.get()+"'")
            booking = cursor.fetchone()
            #print(booking)
            my_str.set(booking)
    
        except : 
             my_str.set("Database error")

def Search():
    global main
    global my_str
    global booking_date
    main = Tk()
    main.geometry("500x500")
    main.title("Search Data")

#---------------------------------------UPDATE BOOKING---------------------------#
    L8 = Label(main, text="Search Data Customer", bg="orange", fg="white")
    L8.place(x=10, y=5)

    L1 = Label(main,  text='Masukkan Tanggal Booking * ', width=25 )  
    L1.place(x=10,y=50) 
    booking_date = Entry(main)
    booking_date.place(x=200,y=50)

    b1 = Button(main, text='Show Details', width=15,bg='orange',command= my_details)
    b1.place(x=200, y=100)
    my_str = StringVar()
    # add one Label
    L2 = Label(main,  textvariable=my_str, width=50,fg='black' )   
    L2.place(x=10,y=150)

    bt2 = Button(main, text='Main Menu', width=15,bg='orange',command= MainMenu1)
    bt2.place(x=200, y=200)

    my_str.set("Output") 

    main.mainloop()

Search()



