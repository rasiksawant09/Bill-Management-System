#imported all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect(r"C:\Users\RASIK\Documents\Bill Management Software Python\Database\store.db")
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
        
root = Tk()
b = Application(root)

root.geometry("1368x768+0+0")
root.mainloop()
