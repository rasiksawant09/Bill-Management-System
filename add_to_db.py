from tkinter import*
import tkinter.messagebox
import sqlite3

# def myWindow():
#     top = Toplevel()
#     # top.pack()

#added r in the below line so that we can convert the text path into a raw string
conn = sqlite3.connect(r"Enter your path here")
c = conn.cursor()  #made so that we can move around

result = c.execute("Select Max(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master, text="Add to the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=300, y=0)

        # self.i = Label(master,text="ID has reached upto: " + str(id), font = ("arial 18 bold"))
        # self.i.place(x=0,y=40)

        #labels and entries for the windows

        self.name_l = Label(master,text="Enter your Product Name ", font = ("arial 18 bold"))
        self.name_l.place(x=0,y=70)
        #Keeping a gap of 50
        self.stocks_l = Label(master,text="Enter Stocks", font = ("arial 18 bold"))
        self.stocks_l.place(x=0,y=120)

        self.cp_l = Label(master,text="Enter Cost Price", font = ("arial 18 bold"))
        self.cp_l.place(x=0,y=170) #cp

        self.sp_l = Label(master,text="Enter Selling Price", font = ("arial 18 bold"))
        self.sp_l.place(x=0,y=220) #sp

        self.vendor_l = Label(master,text="Enter Vendor Name", font = ("arial 18 bold"))
        self.vendor_l.place(x=0,y=270)#vendor

        self.vendor_phone_l = Label(master,text="Enter Vendor Phone No.", font = ("arial 18 bold"))
        self.vendor_phone_l.place(x=0,y=320) #vendor phone

        self.id_l = Label(master, text="Enter ID.",font=('arial 18 bold'))
        self.id_l.place(x=0, y=370)   

        #Entries for label 
        self.name_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.name_e.place(x = 380, y=70)  

        self.stocks_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.stocks_e.place(x = 380, y=120)#stocks

        self.cp_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.cp_e.place(x = 380, y=170) #cp

        self.sp_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.sp_e.place(x = 380, y=220) #spEntry

        self.vendor_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.vendor_e.place(x = 380, y=270) #vendorEntry

        self.vendor_phone_e = Entry(master, width = 25,font=("arial 18 bold"))
        self.vendor_phone_e.place(x = 380, y=320) #vendorPhoneEntry

        self.id_e = Entry(master, width=25, font=("arial 18 bold"))
        self.id_e.place(x = 380, y=370)

        #button to add to Database
        # add seperately command to get items
        self.btn_add = Button(master, text="Add to Database", width=25, height=2, bg="steelblue", fg="white",command = self.get_items)
        self.btn_add.place(x =520, y=470)

        #text-box for the log
        self.tBox = Text(master, width=60, height=18)
        self.tBox.place(x = 750, y =70)

        #Button to clear
        self.btn_clear = Button(master, text="Clear All Fields",width = 18, height=2, bg="lightgreen",fg = "white",command = self.clear_all)
        self.btn_clear.place(x = 350, y=470)

        self.tBox.insert(END, "Id has reached upto: " + str(id))

        self.master.bind('<Return>',self.get_items)  #Return will come not returns
        self.master.bind('<Up>',self.clear_all) 
    def get_items(self, *args, **kwargs):
        #get data from entries
        self.name = self.name_e.get()
        self.stocks = self.stocks_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        #dynamic Entries
        self.totalcp =float(self.cp)* float(self.stocks)
        self.totalsp = float(self.sp) * float(self.stocks)
        self.assumed_profit = float(self.totalsp-self.totalcp)

        if self.name == "" or self.stocks == "" or self.cp == "" or self.sp == "":
            tkinter.messagebox.showinfo("E")
        else:
            sql = "INSERT INTO Inventory (name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phoneno ) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.stocks,self.cp,self.sp,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendor_phone))
            conn.commit()

            tkinter.messagebox.showinfo("Succesfully added","Good to Go")

            #textbox insert
            self.tBox.insert(END, "\n\n Inserted "+ str(self.name) + " into database with code. "+ str(self.id_e.get()))

    def clear_all(self,*args,**kwargs):
        num = id+1
        self.name_e.delete(0,END)
        self.stocks_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phone_e.delete(0,END)
        self.id_e.delete(0, END)


        



root = Tk()
b = Database(root)
root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()
