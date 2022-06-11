from tkinter import *
from tkinter import ttk
from click import command
import mysql.connector
    
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Malik 123",
    database="louvre"
)

cursor1 = db.cursor(buffered=True)
cursor2 = db.cursor(buffered=True)
cursor3 = db.cursor(buffered=True)

def Table1():
    main.destroy()
    import Table1

def Table2():
    main.destroy()
    import Table2

def SearchData():
    main.destroy()
    import SearchData

def register():
    Insert = (
           "INSERT INTO booking(booking_date, metode_pembayaran, jenis_kamar, nomor_kamar, customer_no_pelanggan)"
           "VALUES('"+booking_date.get()+"', '"+metode_pembayaran.get()+"', '"+jenis_kamar.get()+"', '"+nomor_kamar.get()+"', '"+customer_no_pelanggan.get()+"')"
        )
    cursor1.execute(Insert)
    db.commit()
   
def register1():
    Insert1 = (
           "INSERT INTO customer(email, nomor_telepon) VALUES('"+email.get()+"', '"+nomor_telepon.get()+"')")
    cursor2.execute(Insert1)
    db.commit()
    
    

def form():
    global main
    main = Tk()

    main.geometry("1090x500+10+10")
    main.title("Hotel Louvre - Form Database")
    
#-----------------------------Menu Booking---------------------------------#
    global booking_date
    global metode_pembayaran
    global jenis_kamar
    global nomor_kamar
    global customer_no_pelanggan
    metode_pembayaran=StringVar()
    jenis_kamar=StringVar()

    L0 = Label(main, text="Form Booking", bg="orange", fg="white")
    L0.place(x=10, y=5)

    L1 = Label(main, text="Masukkan Tanggal * ")
    L1.place(x=10,y=50)
    booking_date = Entry(main)
    booking_date.place(x=180, y=50)

    L2 = Label(main, text="Metode Pembayaran *")
    L2.place(x=10,y=100)
    monthchoosen = ttk.Combobox(main, width=27, textvariable=metode_pembayaran)
    monthchoosen['values'] = (' Dana',
                              ' ShopeePay',
                              ' GoPay',
                              ' BCA',
                                )
    monthchoosen.current()
    monthchoosen.place(x=180,y=100)

    L3 = Label(main, text="Jenis Kamar *")
    L3.place(x=10, y=150)
    monthchoosen2 = ttk.Combobox(main, width=27, textvariable=jenis_kamar)
    monthchoosen2['values'] = (' Kamar Standar',
                              ' Kamar Deluxe',
                              ' Kamar Superior',
                              ' Presidential Suite',
                                )
    monthchoosen2.current()
    monthchoosen2.place(x=180,y=150)

    L4 = Label(main, text="Nomor Kamar * ")
    L4.place(x=10, y=200)
    nomor_kamar = Entry(main)
    nomor_kamar.place(x=180, y=200)

    L5 = Label(main, text="customer_no_pelanggan * ")
    L5.place(x=10, y=250)
    customer_no_pelanggan = Entry(main)
    customer_no_pelanggan.place(x=180, y=250)

    bt = Button(main, text="Submit", command=register, bg="orange")
    bt.place(x=180, y=300)

#----------------------------Menu Customer-----------------------------------------#

    global email
    global nomor_telepon
    global no_pelanggan

    L8 = Label(main, text="Form Customer", bg="orange", fg="white")
    L8.place(x=460, y=5)

    L6 = Label(main, text="Masukkan Email * ")
    L6.place(x=460,y=50)
    email = Entry(main)
    email.place(x=630,y=50)

    L7 = Label(main, text="Masukkan Nomor Telepon * ")
    L7.place(x=460,y=100)
    nomor_telepon = Entry(main)
    nomor_telepon.place(x=630,y=100)

    bt1 = Button(main, text= "Submit", command=register1, bg="orange")
    bt1.place(x=630,y=150)

#-------------------------Another-------------------------#
    L8 = Label(main, text="Another Page", bg="orange", fg="white")
    L8.place(x=890, y=5)

    bt2 = Button(main, text="Refresh", command=form, bg="orange")
    bt2.place(x=890,y=55)

    bt3 = Button(main, text="Table Customer", command=Table1, bg="orange")
    bt3.place(x=890, y=100)
    
    bt4 = Button(main, text="Table Booking", command=Table2, bg="orange")
    bt4.place(x=890, y=150)

    bt5 = Button(main, text="Search Data", command=SearchData, bg="orange")
    bt5.place(x=890, y=200)

    main.mainloop()

form()
