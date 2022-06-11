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

def MainMenu1():
    main.destroy()
    import MainMenu1

cursor = db.cursor()

def delete():
    Delete1 = ("DELETE FROM customer WHERE no_pelanggan=('"+no_pelanggan.get()+"')")
    cursor.execute(Delete1)
    db.commit()


def update():
    Update1 = ("UPDATE customer SET email=('"+email.get()+"'), nomor_telepon=('"+nomor_telepon.get()+"') WHERE no_pelanggan=('"+nomor.get()+"')")
    cursor.execute(Update1)
    db.commit()


def showdata():
    global main
    global email
    global nomor_telepon
    global no_pelanggan
    global nomor
    main = Tk()
    
    main.geometry("1080x600+10+10")
    main.title("Table Customer")
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM customer")
    e = Label(main, width=15, text="no_pelanggan",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e = Label(main, width=15, text="email",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e = Label(main, width=15, text="nomor_telepon",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)

    i=1

    for customer in cursor: 
        for j in range(len(customer)):
            e = Label(main,width=15,text=customer[j], relief='ridge',anchor='w') 
            e.grid(row=i, column=j) 
            #e.insert(END, customer[j])
        i=i+1

    L9 = Label(main, text="Form Update Table * ", bg="orange", fg="white")
    L9.place(x=10, y=250)

    L7 = Label(main, text="No_pelanggan * ")
    L7.place(x=10, y=300)
    nomor = Entry(main)
    nomor.place(x=180, y=300)


    L6 = Label(main, text="Update Email")
    L6.place(x=10, y=340)
    email = Entry(main)
    email.place(x=180, y=340)

    L7 = Label(main, text="Update Nomor Telepon * ")
    L7.place(x=10, y=380)
    nomor_telepon = Entry(main)
    nomor_telepon.place(x=180, y=380)

#-------------------------DELETE-------------------------#
    L9 = Label(main, text="Delete Table * ", bg="orange", fg="white")
    L9.place(x=600, y=250)

    L8 = Label(main, text="Masukkan no_pelanggan * ")
    L8.place(x=600, y=300)
    no_pelanggan = Entry(main)
    no_pelanggan.place(x=790, y=300)

    bt = Button(main, text="Update Table", command=update, bg="orange")
    bt.place(x=180,y=420)

    bt = Button(main, text="Refresh Table", command=showdata, bg="orange")
    bt.place(x=280,y=420)

    bt2 = Button(main, text="Main Menu", command=MainMenu1, bg="orange")
    bt2.place(x=390,y=420)

    bt3 = Button(main, text="Delete", command=delete, bg="orange")
    bt3.place(x=790,y=350)


    main.mainloop()

showdata()