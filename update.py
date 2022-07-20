from tkinter import*
import tkinter.messagebox
import sqlite3

#added r in the below line so that we can convert the text path into a raw string
conn = sqlite3.connect(r"C:\Users\RASIK\Documents\Bill Management Software Python\Database\store.db")
c = conn.cursor()  #made so that we can move around

result = c.execute("Select Max(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master, text="Update to the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=300, y=0)

        # self.i = Label(master,text="ID has reached upto: " + str(id), font = ("arial 18 bold"))
        # self.i.place(x=0,y=40)

        #label and entries for label wrote here forgot to add
        self.id_le = Label(master, text="Enter ID ", font=('arial 18 bold'))
        self.id_le.place(x=0, y=70)

        self.id_leb = Entry(master, font=('arial 18 bold'),width=10)
        self.id_leb.place(x=380, y=70)

        self.btn_search = Button(master, text="Search", width=15, height=2, bg='orange', command=self.search)
        self.btn_search.place(x=550, y=70)

        #labels and entries for the windows

        self.name_l = Label(master,text="Enter your Product Name ", font = ("arial 18 bold"))
        self.name_l.place(x=0,y=120)
        #Keeping a gap of 50
        self.stocks_l = Label(master,text="Enter Stocks", font = ("arial 18 bold"))
        self.stocks_l.place(x=0,y=170)

        self.cp_l = Label(master,text="Enter Cost Price", font = ("arial 18 bold"))
        self.cp_l.place(x=0,y=220) #cp

        self.sp_l = Label(master,text="Enter Selling Price", font=("arial 18 bold"))
        self.sp_l.place(x = 0, y=270) #sp

        self.totalcp_l = Label(master,text="Enter total Cost Price", font=("arial 18 bold"))
        self.totalcp_l.place(x = 0, y=320) #totalcp

        self.totalsp_l = Label(master,text="Enter total Selling Price",font=("arial 18 bold"))
        self.totalsp_l.place(x = 0, y=370) #totalsp

        self.vendor_l = Label(master,text="Enter Vendor Name", font = ("arial 18 bold"))
        self.vendor_l.place(x=0,y=420)#vendor

        self.vendor_phone_l = Label(master,text="Enter Vendor Phone No.", font = ("arial 18 bold"))
        self.vendor_phone_l.place(x=0,y=470) #vendor phone

        # self.id_l = Label(master, text="Enter ID.",font=('arial 18 bold'))
        # self.id_l.place(x=0, y=420)   

        #Entries for label 
        self.name_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.name_e.place(x = 380, y=120)  

        self.stocks_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.stocks_e.place(x = 380, y=170)#stocks

        self.cp_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.cp_e.place(x = 380, y=220) #cp

        self.sp_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.sp_e.place(x = 380, y=270) #spEntry

        self.totalcp_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.totalcp_e.place(x = 380, y=320) #totalcp

        self.totalsp_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.totalsp_e.place(x = 380, y=370) #totalsp

        self.vendor_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.vendor_e.place(x = 380, y=420) #vendorEntry

        self.vendor_phone_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.vendor_phone_e.place(x = 380, y=470) #vendorPhoneEntry

        # self.id_e = Entry(master, width=25, font=("arial 18 bold"))
        # self.id_e.place(x = 380, y=420)

        #button to add to Database
        # add seperately command to get items
        self.btn_add = Button(master, text="Update to Database", width=25, height=2, bg="steelblue", fg="white", command=self.update)
        self.btn_add.place(x =520, y=520)

        #text-box for the log
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x = 750, y =70)
        self.tBox.insert(END, "Id has reached upto: " + str(id))
        # #textbox insert
        # self.tBox.insert(END, "\n\n Inserted "+ str(self.name) + " into database with code. "+ str(self.id_e.get()))

        #Button to clear
        # self.btn_clear = Button(master, text="Clear All Fields",width = 18, height=2, bg="lightgreen",fg = "white")
        # self.btn_clear.place(x = 350, y=520)

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 = r[1] #name
            self.n2 = r[2] #stocks
            self.n3 = r[3] #cp
            self.n4 = r[4] #sp
            self.n5 = r[5] #totalcp
            self.n6 = r[6] #totalsp
            self.n7 = r[7] #assumed_profit
            self.n8 = r[8] #vendor
            self.n9 = r[9] #vendor_phone
        conn.commit()

        #insert into the entries to update
        # self.name_e.insert(self.n1, END) gave str error
        self.name_e.delete(0, END)   #if we don't add this statement then we have to manully erase out the the garbage value or the value which is already in the text field
        self.name_e.insert(0, str(self.n1))

        self.stocks_e.delete(0, END)
        self.stocks_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0,str(self.n4))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendor_phone_e.delete(0, END)
        self.vendor_phone_e.insert(0, str(self.n9))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n5))
        
        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n6))

    def update(self, *args, **kwargs):
        # get all updated entries
        self.u1 = self.name_e.get()
        self.u2 = self.stocks_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_e.get()

        query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phoneno=? WHERE id=?"
        c.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Great Success", "Go to go Update the database")

root = Tk()
b = Database(root)
root.geometry("1366x768+0+0")
root.title("Update to the database")
root.mainloop()