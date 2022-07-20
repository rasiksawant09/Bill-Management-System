from tkinter import*
import tkinter.messagebox
import sqlite3
import datetime
import math
import os
import random
# import add_to_db
# from add_to_db import myWindow

def add_to_db():
    conn = sqlite3.connect(r"Enter your path here store.db")
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


    root1 = Tk()
    b = Database(root1)
    root1.geometry("1366x768+0+0")
    root1.title("Add to the database")
    root1.mainloop()

def update():
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

    root2 = Tk()
    b = Database(root2)
    root2.geometry("1366x768+0+0")
    root2.title("Update to the database")
    root2.mainloop()

def main():
    conn = sqlite3.connect(r"Enter store.db path here")
    c = conn.cursor()

    #date
    date = datetime.datetime.now().date()

    #temporary lists like session
    products_list=[]
    products_price = []
    products_quantity = []
    product_id = []
    class Application:
        def __init__(self, master, *args, **kwargs):
            self.master = master
            #frames
            self.left = Frame(master, width=700, height=768, bg="white") #800
            self.left.pack(side=LEFT)

            self.right = Frame(master,width=666, height=768, bg="lightblue") #566
            self.right.pack(side=RIGHT)

            #components
            self.heading = Label(self.left, text="Star SuperMarket", font = ('arial 40 bold'), bg="white")  #heading for this frame
            self.heading.place(x=0,y=0)

            self.date_l = Label(self.right, text="Today's Date: " + str(date), font=("arial 16 bold"), bg="lightblue", fg="white")
            self.date_l.place(x=0,y=0)

            #table invoice----------
            self.product = Label(self.right, text="Products", font = ("arial 18 bold"), bg="lightblue", fg="white")
            self.product.place(x=0,y=60)

            #Quantity
            self.tquantity = Label(self.right, text="Quantity", font=("arial 18 bold"), bg = "lightblue", fg="white")
            self.tquantity.place(x =300, y=60)
            #Amount
            self.tamount = Label(self.right, text="Amount", font=("arial 18 bold"), bg="lightblue", fg="white")
            self.tamount.place(x=500, y=60)

            #enter stuff
            # self.enterid = Label(self.left, text="Enter Product's ID",font=("arial 18 bold"), bg="white")
            self.enterid = Label(self.left, text="Enter Product's Name",font=("arial 18 bold"), bg="white")
            self.enterid.place(x=0, y=80)

            self.enteride = Entry(self.left, width=25, font = ("arial 18 bold"), bg="lightblue")
            self.enteride.place(x=270, y=80)
            self.enteride.focus() #automatically takes cursor to the the id ENTRY

            #search Button
            self.search_btn = Button(self.left, text="Search", width=25, height=2,bg="orange",command=self.ajax)
            self.search_btn.place(x=410,y=120)

            #fill it later by the function ajax
            self.productname = Label(self.left, text="", font=("arial 18 bold"), bg="white", fg="steelblue")
            self.productname.place(x=0, y=250)

            self.pprice = Label(self.left,text="", font=("arial 27 bold"), bg="white", fg="steelblue")
            self.pprice.place(x=0, y=290)

            #total label 
            self.total_l = Label(self.right, text='Total', font=("arial 40 bold"),bg='lightblue', fg="white")
            self.total_l.place(x=0,y=600)

        def ajax(self, *args, **kwargs):  #when serach button will bwe pressed it will give returned you the name of product
            self.get_id12 = self.enteride.get()
            #getting the information with that id and fill it in the labels above
            # query = "SELECT * FROM inventory WHERE id=?" 
            query = "SELECT * FROM inventory WHERE name=?"
            result = c.execute(query, (self.get_id12, ))
            for self.r in result:
                self.get_id = self.r[0]   #to maintain transactions
                self.get_name = self.r[1]
                self.get_price = self.r[4]
                self.get_stock = self.r[2]
            self.productname.configure(text="Product's Name: "+str(self.get_name))
            # self.productname.configure(text="Product's Name: "+str(self.get_id))
            self.pprice.configure(text="Price: Rs. "+str(self.get_price))

            #created the quantity and discount label
            self.quantity_l = Label(self.left, text="Enter Quantity", font=("arial 18 bold"), bg="white")
            self.quantity_l.place(x=0, y=370)

            self.quantity_e = Entry(self.left, width=25, font=("arial 18 bold"), bg="lightblue")
            self.quantity_e.place(x=190, y=370)
            self.quantity_e.focus()

            #label for discount
            self.discount_l = Label(self.left, text="Enter Discount", font=("arial 18 bold"), bg="white")
            self.discount_l.place(x=0, y=410)

            self.discount_e = Entry(self.left, width=25, font=("arial 18 bold"), bg="lightblue")
            self.discount_e.place(x=190, y=410)
            self.discount_e.insert(END,0)

            #add to cart button

            self.add_to_cart_btn = Button(self.left, text="Add to Cart", width=22, height=2, bg="orange",command=self.add_to_cart)  #bug because of color spelling was written wrong typo error orenge
            self.add_to_cart_btn.place(x=350, y=450)
            
            #generatebill and change for time beign i have commented it // Again kept it has it is
            self.change_l = Label(self.left, text="Given Amount", font=("arial 18 bold"), bg="white")
            self.change_l.place(x=0, y=550)

            self.change_e = Entry(self.left, width=25, font=("arial 18 bold"), bg="lightblue")
            self.change_e.place(x=190,y=550)

            #button to change
            self.change_btn = Button(self.left, text="Calculate change", width=22, height=2, bg="orange", command=self.change_func)
            self.change_btn.place(x=350,y=590)

            #generate bill
            self.bill_btn= Button(self.left, text="Generate Bill",width=100, height=2, bg="red",fg="white", command=self.generate_bill)
            self.bill_btn.place(x=0, y=640)
            
        def add_to_cart(self, *args, **kwargs):
            #getting quantity value from the database
            self.quantity_value = int(self.quantity_e.get())
            if self.quantity_value > int(self.get_stock):
                tkinter.messagebox.showinfo("Error","The amount requested is not in the inventory or out of stock")
            else:
                # print("Working great") #Great Success

                #calculate the price
                self.final_price = float(self.quantity_value)*float(self.get_price)-(float(self.discount_e.get()))
                products_list.append(self.get_name)
                products_price.append(self.final_price)
                products_quantity.append(self.quantity_value)
                product_id.append(self.get_id)  # bug due to typo error products->product

                print(products_list)
                print(products_price)
                print(products_quantity)

                self.x_index = 0
                self.y_index = 100
                self.counter = 0  #so that whenever we want to add new items or something 

                for self.p in products_list:
                    self.tempname = Label(self.right,text=str(products_list[self.counter]), font=("arial 18 bold"), bg='lightblue', fg="white")
                    self.tempname.place(x=0,y=self.y_index)

                    self.tempqt = Label(self.right, text=str(products_quantity[self.counter]), font=("arial 18 bold"), bg = "lightblue", fg="white")
                    self.tempqt.place(x=300, y=self.y_index)

                    self.tempprice = Label(self.right, text=str(products_price[self.counter]), font=("arail 18 bold"), bg="lightblue", fg='white')
                    self.tempprice.place(x=500, y=self.y_index)

                    self.y_index+=40
                    self.counter +=1

                    #total configure
                    self.total_l.configure(text="Total Rs." + str(sum(products_price)))

                    #delete
                    self.quantity_l.place_forget()
                    self.quantity_e.place_forget()
                    self.discount_l.place_forget()
                    self.discount_e.place_forget()
                    # self.change_l.place_forget()
                    # self.change_e.place_forget()
                    self.productname.configure(text="")
                    self.pprice.configure(text="")
                    self.add_to_cart_btn.destroy()
                    # self.change_btn.destroy()

                    #autofocus to the enter id 
                    self.enteride.focus()
                    self.enteride.delete(0,END)

        def change_func(self, *args, **kwargs):
            #get the amount by the customer and the amount generated by the computer
            self.amount_given = float(self.change_e.get())
            self.our_total = float(sum(products_price))

            self.to_give = self.amount_given - self.our_total

            #label change
            self.c_amount = Label(self.left,text="Change Rs: " + str(self.to_give), font=("arial 18 bold"), fg="red")
            self.c_amount.place(x=0, y=600)

        def generate_bill(self, *args, **kwargs):
            #We have now create the bill fisrt then we will update the database
            directory = "C:/Users/RASIK/Documents/Bill Management Software Python/Invoice/" + str(date) + "/"  # slash added so that the file goes into the created directory on that date
            if not os.path.exists(directory):
                os.makedirs(directory)

            #TEMPLATE FOR THE BILL
            company = "\t\t\t\tStar SuperMarket \n"
            address = "\t\t\t\tIndiraNagar,Mumbai \n"
            phone = "\t\t\t\t8282101080 \n"
            sample = "\t\t\t\tInvoice \n" 
            dt = "\t\t\t\t" + str(date)

            table_header = "\n\n\t\t\t-------------------------------\n\t\t\tSN.\tProducts\t\tQty\t\tAmount\n\t\t\t-------------------------------"
            final = company+address+phone+sample+dt+"\n"+table_header 

            #open a file to write it to
            file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
            f = open(file_name, 'w') #gave write permission      
            f.write(final)
            #filling the items
            r = 1
            i = 0
            for t in products_list:
                f.write("\n\t\t\t" + str(r) + "\t" + str(products_list[i] + ".......")[:7] + "\t\t" + str(products_quantity[i]) + "\t\t" + str(products_price[i]))
                i +=1
                r += 1

            f.write("\n\n\t\t\tTotal: Rs. " + str(sum(products_price)))
            f.write("\n\t\t\tThanks for Visiting.")
            # os.startfile(file_name,"print") #will print the document 
            f.close()
            #decrease the stock
            self.x = 0

            initial = "SELECT * FROM inventory WHERE id=?"
            result = c.execute(initial, (product_id[self.x],))
            
            for i in products_list:
                for r in result:
                    self.old_stock = r[2]
                self.new_stock = int(self.old_stock)-int(products_quantity[self.x])
                
                #updating the stock
                sql = "UPDATE inventory SET stock=? WHERE id=?"
                c.execute(sql,(self.new_stock, product_id[self.x]))
                conn.commit()

                #insert into the transactions
                sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?,?,?,?)"
                c.execute(sql2, (products_list[self.x],products_quantity[self.x], products_price[self.x], date))
                conn.commit()

                print("Decreased")
                self.x +=1

            tkinter.messagebox.showinfo("Success", "Done Everything smoothly")
            
    root3 = Tk()
    b = Application(root3)

    root3.geometry("1368x768+0+0")
    root3.mainloop()

root = Tk()
h1 = Label(text="Star Supermarket", font = ("arial 18 bold"), fg="steel blue")
h1.place(x=100,y=0)
h2 = Label(text="Please select the below option to perform ", font = ("arial 15 bold"), fg="steel blue")
h2.place(x=0,y=50)
h3 = Label(text="Execution", font = ("arial 15 bold"), fg="steel blue")
h3.place(x=150,y=80)
btn = Button(root,text="1. Add items to Database",width=25, height=2,bg="orange",font=("arial 10 bold"),command=add_to_db)
btn.pack()
btn.place(x=120,y=120)
btn1 = Button(root,text="2. Update database",width=25, height=2,bg="orange",font=("arial 10 bold"),command=update)
btn1.pack()
btn1.place(x=120,y=180)
btn2 = Button(root,text="3. Bill System",width=25, height=2,bg="orange",font=("arial 10 bold"),command=main)
btn2.pack()
btn2.place(x=120,y=240)
btn3 = Button(root,text="Close the Application",width=25, height=2,bg="orange",font=("arial 10 bold"),command=root.destroy)
btn3.pack()
btn3.place(x=120,y=300)
 

root.geometry("400x400")
root.mainloop()
