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

def update():
    UPDATE = (
           "UPDATE booking SET booking_date = ('"+booking_date.get()+"'), metode_pembayaran = ('"+metode_pembayaran.get()+"'), jenis_kamar = ('"+jenis_kamar.get()+"'), nomor_kamar = ('"+nomor_kamar.get()+"'), customer_no_pelanggan = ('"+customer_no_pelanggan.get()+"')"
        )
    cursor.execute(UPDATE)
    db.commit()

def delete():
    Delete1 = ("DELETE FROM booking WHERE booking_id=('"+booking_id.get()+"')")
    cursor.execute(Delete1)
    db.commit()


def showdata():
    global main
    main = Tk()
    global booking_date
    global metode_pembayaran
    global jenis_kamar
    global nomor_kamar
    global customer_no_pelanggan
    global booking_id
    metode_pembayaran=StringVar()
    jenis_kamar=StringVar()

    main.geometry("1080x600+10+10")
    main.title("Table Booking")
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Booking")
    e = Label(main, width=15, text="booking_id",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e = Label(main, width=15, text="booking_date",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e = Label(main, width=17, text="metode_pembayaran",borderwidth=3,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e = Label(main, width=15, text="jenis_kamar",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e = Label(main, width=15, text="nomor_kamar",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e = Label(main, width=20, text="customer_no_pelanggan",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    
    i=1

    for Booking in cursor: 
        for j in range(len(Booking)):
            e = Label(main,width=15,text=Booking[j], relief='ridge',anchor='w') 
            e.grid(row=i, column=j) 
            #e.insert(END, customer[j])
        i=i+1

#-------------------------------UPDATE----------------------------#

    L9 = Label(main, text="Form Update Table * ", bg="orange", fg="white")
    L9.place(x=10, y=250)

    L10 = Label(main, text="Update Tanggal Booking * ")
    L10.place(x=10, y=300)
    booking_date = Entry(main)
    booking_date.place(x=240, y=300)

    L6 = Label(main, text="Update Metode Pembayaran *")
    L6.place(x=10,y=350)
    monthchoosen = ttk.Combobox(main, width=27, textvariable=metode_pembayaran)
    monthchoosen['values'] = (' Dana',
                              ' ShopeePay',
                              ' GoPay',
                              ' BCA',
                                )
    monthchoosen.current()
    monthchoosen.place(x=240,y=350)

    L7 = Label(main, text="Jenis Kamar *")
    L7.place(x=10, y=400)
    monthchoosen2 = ttk.Combobox(main, width=27, textvariable=jenis_kamar)
    monthchoosen2['values'] = (' Kamar Standar',
                              ' Kamar Deluxe',
                              ' Kamar Superior',
                              ' Presidential Suite',
                                )
    monthchoosen2.current()
    monthchoosen2.place(x=240,y=400)

    L8 = Label(main, text="Nomor Kamar * ")
    L8.place(x=10, y=450)
    nomor_kamar = Entry(main)
    nomor_kamar.place(x=240, y=450)

    L9 = Label(main, text="customer_no_pelanggan * ")
    L9.place(x=10, y=500)
    customer_no_pelanggan = Entry(main)
    customer_no_pelanggan.place(x=240, y=500)

    bt1 = Button(main, text="Update", command=update, bg="orange")
    bt1.place(x=240,y=550)

    bt2 = Button(main, text="Main Menu", command=MainMenu1, bg="orange")
    bt2.place(x=325,y=550)

#------------------------------------------DELETE--------------------------------#

    L9 = Label(main, text="Delete Table * ", bg="orange", fg="white")
    L9.place(x=600, y=250)

    L1 = Label(main, text="Masukkan Booking ID * ")
    L1.place(x=600,y=300)
    booking_id = Entry(main)
    booking_id.place(x=790, y=300)

    bt3 = Button(main, text="Delete", command=delete, bg="orange")
    bt3.place(x=790,y=350)

    bt = Button(main, text="Refresh Table", command=showdata, bg="orange")
    bt.place(x=860,y=350)

    main.mainloop()

showdata()



