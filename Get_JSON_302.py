import sys

from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter.constants import ACTIVE, DISABLED, NORMAL
from tkinter.constants import LEFT, BOTTOM
from tkinter import Button, Frame, Tk
from faulthandler import disable
import datetime
import time
from tkinter import END
import cx_Oracle
import PH_login_loop_302
import clock
import json
import requests
import pymysql

db = pymysql.connect('localhost', 'root', '', 'pizzahut')
cursor = db.cursor()


class Gui:
    def json_get(self):

        get = requests.get('http://127.0.0.1:3000/getdata')  # GET request
        self.Order = get.json()

        # with open('Order.json', 'r') as json_file:
        # self.Order = json.load(json_file)


        self.editAreaTable.config(state="normal")
        self.editAreaTable.delete("1.0", END)
        self.editAreaTable.insert(tk.INSERT, self.Order)

        self.editAreaTable.config(state="disabled")

        '''
        while True:
            get = requests.get('http://127.0.0.1:3000/getdata')  # GET request
            self.Order = get.json()

            # with open('Order.json', 'r') as json_file:
            # self.Order = json.load(json_file)



            self.editAreaTable.config(state="normal")
            self.editAreaTable.delete("1.0", END)
            self.editAreaTable.insert(tk.INSERT, self.Order)

            self.editAreaTable.config(state="disabled")
            time.sleep(1)  # then wait one second

        '''
        print(self.Order)

        if isinstance(self.Order["ORDER_PRODUCT_ID"], list) == True:

            cursor.execute(
                "INSERT INTO `order`VALUES ({0},'{4}','{1}',{2},'{3}');".format(
                    self.Order["ORDER_ID"], self.Order["ORDER_TIME"], self.Order["ADDRESS"], self.Order["STATUS"],
                    self.Order["SHOP_ID"]))

            for i in range(0, len(self.Order["ORDER_PRODUCT_ID"])):
                cursor.execute("select order_product_id FROM order_product ")
                for e in cursor.fetchall():
                    pass
                OPI = e[0] + 1

                cursor.execute(
                    "INSERT INTO `order_product` (`ORDER_ID`, `PRODUCT_ID`, `QUANTITY`, `PRICE`, `ORDER_PRODUCT_ID`, `LINK_PRODUCT`) VALUES ({0},'{1}',{2},{3},{4},'{5}');".format(
                        self.Order["ORDER_ID"], self.Order["ORDER_PRODUCT_ID"][i], self.Order["ORDER_QUANTITY"][i],
                        self.Order["PRICE"][i], OPI, self.Order["LINK_PRODUCT"][i]))
        else:

            cursor.execute(
                "INSERT INTO `order` (`ORDER_ID`, `STATUS`, `SHOP_ID`, `ORDER_DATE_TIME`,`ADDRESS_ID`) VALUES ({0}, '{2}','S0001', '{1}',{3});".format(
                    self.Order["ORDER_ID"], self.Order["ORDER_TIME"], self.Order["STATUS"], self.Order["ADDRESS"]))

            for e in cursor.fetchall():
                pass
            OPI = e[0] + 1

            cursor.execute(
                "INSERT INTO `order_product` (`ORDER_ID`, `PRODUCT_ID`, `QUANTITY`, `PRICE`, `ORDER_PRODUCT_ID`, `LINK_PRODUCT`) VALUES ({0},'{1}',{2}, {3},{4},'{5}');".format(
                    self.Order["ORDER_ID"], self.Order["ORDER_PRODUCT_ID"], self.Order["ORDER_QUANTITY"],
                    self.Order["PRICE"], OPI, self.Order["LINK_PRODUCT"]))

        db.commit()

        self.editAreaTable.config(state="normal")

        self.editAreaTable.delete("1.0", END)

        self.editAreaTable.insert(tk.INSERT, "Order Details: ")
        self.editAreaTable.insert(tk.INSERT, "\nORDER ID : ")
        self.editAreaTable.insert(tk.INSERT, self.Order["ORDER_ID"])

        self.editAreaTable.insert(tk.INSERT, "\nORDER_TIME: ")
        self.editAreaTable.insert(tk.INSERT, self.Order["ORDER_TIME"])

        self.editAreaTable.insert(tk.INSERT, "\nLINK_PRODUCT: ")
        self.editAreaTable.insert(tk.INSERT, self.Order["LINK_PRODUCT"])

        self.editAreaTable.insert(tk.INSERT, "\nORDER_PRODUCT_ID  : ")
        self.editAreaTable.insert(tk.INSERT, self.Order["ORDER_PRODUCT_ID"])

        self.editAreaTable.insert(tk.INSERT, "\nORDER_PRODUCT_NAME : ")
        self.editAreaTable.insert(tk.INSERT, self.Order["ORDER_PRODUCT_NAME"])

        self.editAreaTable.insert(tk.INSERT, "\nORDER_QUANTITY : ")
        self.editAreaTable.insert(tk.INSERT, self.Order["ORDER_QUANTITY"])

        self.editAreaTable.insert(tk.INSERT, "\nPRICE: ")
        self.editAreaTable.insert(tk.INSERT, self.Order["PRICE"])

        self.editAreaTable.insert(tk.INSERT, "\nADDRESS: ")
        self.editAreaTable.insert(tk.INSERT, self.Order["ADDRESS"])

        self.editAreaTable.insert(tk.INSERT, "\nSTATUS: ")
        self.editAreaTable.insert(tk.INSERT, self.Order["STATUS"])

        self.editAreaTable.config(state="disabled")

    def order_history(self):

        order = []
        date = []
        address = []
        status = []
        olist = []

        print(
            "select a.ORDER_ID,c.order_date_time,a.LINK_PRODUCT,b.PRODUCT_NAME,a.QUANTITY,a.PRICE,c.address_id,c.status FROM order_product a JOIN product b on a.PRODUCT_ID=b.PRODUCT_ID join `order` c on a.order_id=c.ORDER_ID where c.SHOP_ID='{0}' order by a.ORDER_ID desc, a.ORDER_PRODUCT_ID".format(
                self.id))
        cursor.execute(
            "select a.ORDER_ID,c.order_date_time,a.LINK_PRODUCT,b.PRODUCT_NAME,a.QUANTITY,a.PRICE,c.address_id,c.status FROM order_product a JOIN product b on a.PRODUCT_ID=b.PRODUCT_ID join `order` c on a.order_id=c.ORDER_ID where c.SHOP_ID='{0}' order by a.ORDER_ID desc, a.ORDER_PRODUCT_ID".format(
                self.id))
        for i in cursor.fetchall():
            if i[0] not in order:
                order.append(i[0])
                date.append(i[1])
                address.append(i[6])
                status.append(i[7])
            olist.append(i)

        self.editAreaTable.config(state="normal")
        self.editAreaTable.delete("1.0", END)

        for e in range(0, len(order)):
            self.editAreaTable.insert(tk.INSERT, "Order Details--- ")
            self.editAreaTable.insert(tk.INSERT, "\nORDER ID : ")
            self.editAreaTable.insert(tk.INSERT, str(order[e]))

            if str(address[e]) == "0":
                self.editAreaTable.insert(tk.INSERT, "  [take away]")
            else:
                self.editAreaTable.insert(tk.INSERT, "  [delivery]")

            self.editAreaTable.insert(tk.INSERT, "\nORDER_TIME: ")
            self.editAreaTable.insert(tk.INSERT, str(date[e]))

            self.editAreaTable.insert(tk.INSERT, "\nORDER_STATUS: ")
            self.editAreaTable.insert(tk.INSERT, str(status[e]))

            self.editAreaTable.insert(tk.INSERT, "\n\nNo./Name/Qty/$\n\n")

            no = 0
            for a in range(0, len(olist)):
                if olist[a][0] == order[e]:
                    if olist[a][2] == "/":
                        self.editAreaTable.insert(tk.INSERT, str(no) + ' ')
                        self.editAreaTable.insert(tk.INSERT, olist[a][3])
                        self.editAreaTable.insert(tk.INSERT, ' ')
                        self.editAreaTable.insert(tk.INSERT, olist[a][4])
                        self.editAreaTable.insert(tk.INSERT, ' $')
                        self.editAreaTable.insert(tk.INSERT, olist[a][5])
                        self.editAreaTable.insert(tk.INSERT, '\n')
                    else:
                        self.editAreaTable.insert(tk.INSERT, '     ')
                        self.editAreaTable.insert(tk.INSERT, '-')
                        self.editAreaTable.insert(tk.INSERT, olist[a][3])
                        self.editAreaTable.insert(tk.INSERT, ' $')
                        self.editAreaTable.insert(tk.INSERT, olist[a][5])
                        self.editAreaTable.insert(tk.INSERT, '\n')
                    no += 1
                else:
                    no = 0

            cursor.execute("select sum(price*QUANTITY) from order_product WHERE ORDER_ID={0}".format(order[e]))
            for c in cursor.fetchall():
                total = c[0]

            self.editAreaTable.insert(tk.INSERT, "\nTotal:" + str(total))
            self.editAreaTable.insert(tk.INSERT, "\n\n\n\n")

        self.editAreaTable.config(state="disabled")

    def logout(self):

        PH_login_loop_302.main(self.root)

    def add_page_editarea(self, choice):
        if choice == "del":
            self.ous_list = self.ous_list[:-1]
            self.editAreaTable3.delete("1.0", END)
            self.editAreaTable3.insert(tk.INSERT, self.ous_list)

        elif choice == "Enter":
            self.update_status()


        else:
            self.ous_list += choice
            self.editAreaTable3.insert(tk.INSERT, choice)
            self.editAreaTable3.see("end")

    def update_status(self):

        if self.order_id == '':
            found = False

            cursor.execute(
                "select a.ORDER_ID,c.order_date_time,a.LINK_PRODUCT,b.PRODUCT_NAME,a.QUANTITY,a.PRICE,c.address_id,c.status FROM order_product a JOIN product b on a.PRODUCT_ID=b.PRODUCT_ID join `order` c on a.order_id=c.ORDER_ID  where c.SHOP_ID='{0}' order by a.ORDER_ID".format(
                    self.id))
            for i in cursor.fetchall():
                if str(self.editAreaTable3.get("1.0", END)[0:-1]) == str(i[0]):
                    found = True
                else:
                    pass

            self.order_id = self.editAreaTable3.get("1.0", END)[0:-1]
            self.editAreaTable2.insert(tk.INSERT, self.order_id, '\n')

            if not found:
                self.editAreaTable2.insert(tk.INSERT, '\nNot Found. Try Again:')
                self.order_id = ''
                self.ous_list = ''

            self.editAreaTable3.delete("1.0", END)
            self.editAreaTable3.see("end")
            self.ous_list = ''
        else:
            self.order_status = self.editAreaTable3.get("1.0", END)[0:-1]
            self.editAreaTable2.insert(tk.INSERT, self.order_status)
            self.editAreaTable3.delete("1.0", END)
            self.editAreaTable3.see("end")
            self.ous_list = ''

        if self.order_id != '' and self.order_status == '':
            self.editAreaTable2.insert(tk.INSERT, '\nStatus:')

        if self.order_id != '' and self.order_status != '':
            if str(self.order_status) == 'Prepared' or str(self.order_status) == 'Shipped' or str(
                    self.order_status) == 'Submit':

                cursor.execute(
                    "UPDATE `order` SET `STATUS` = '{1}' WHERE `order`.`ORDER_ID` = {0};".format(self.order_id,
                                                                                                 self.order_status))

                Reply = {
                    "ORDER_ID": self.order_id,
                    "STATUS": self.order_status
                }
                cursor.execute(
                    "UPDATE `order` SET `STATUS` = '{1}' WHERE `order`.`ORDER_ID` = {0};".format(self.order_id,
                                                                                                 self.order_status))
                cursor.execute("commit")

                post = requests.post('http://127.0.0.1:3500/postdata', json=Reply)  # the POST request
                print(post.text)

                self.editAreaTable2.insert(tk.INSERT, '\nDone!')
                self.editAreaTable2.insert(tk.INSERT, '\n')
                self.editAreaTable2.insert(tk.INSERT, 'Other id to update:')
                self.order_id = ''
                self.order_status = ''

                # refresh
                order = []
                date = []
                address = []
                status = []
                olist = []

                cursor.execute(
                    "select a.ORDER_ID,c.order_date_time,a.LINK_PRODUCT,b.PRODUCT_NAME,a.QUANTITY,a.PRICE,c.address_id,c.status FROM order_product a JOIN product b on a.PRODUCT_ID=b.PRODUCT_ID join `order` c on a.order_id=c.ORDER_ID where c.SHOP_ID='{0}' order by a.ORDER_ID desc, a.ORDER_PRODUCT_ID".format(
                        self.id))
                for i in cursor.fetchall():
                    if i[0] not in order:
                        order.append(i[0])
                        date.append(i[1])
                        address.append(i[6])
                        status.append(i[7])
                    olist.append(i)

                self.editAreaTable.config(state="normal")
                self.editAreaTable.delete("1.0", END)

                for e in range(0, len(order)):
                    self.editAreaTable.insert(tk.INSERT, "Order Details--- ")
                    self.editAreaTable.insert(tk.INSERT, "\nORDER ID : ")
                    self.editAreaTable.insert(tk.INSERT, str(order[e]))

                    if str(address[e]) == "0":
                        self.editAreaTable.insert(tk.INSERT, "  [take away]")
                    else:
                        self.editAreaTable.insert(tk.INSERT, "  [delivery]")

                    self.editAreaTable.insert(tk.INSERT, "\nORDER_TIME: ")
                    self.editAreaTable.insert(tk.INSERT, str(date[e]))

                    self.editAreaTable.insert(tk.INSERT, "\nORDER_STATUS: ")
                    self.editAreaTable.insert(tk.INSERT, str(status[e]))

                    self.editAreaTable.insert(tk.INSERT, "\n\nNo./Name/Qty/$\n\n")

                    no = 0
                    for a in range(0, len(olist)):
                        if olist[a][0] == order[e]:
                            if olist[a][2] == "/":
                                self.editAreaTable.insert(tk.INSERT, str(no) + ' ')
                                self.editAreaTable.insert(tk.INSERT, olist[a][3])
                                self.editAreaTable.insert(tk.INSERT, ' ')
                                self.editAreaTable.insert(tk.INSERT, olist[a][4])
                                self.editAreaTable.insert(tk.INSERT, ' $')
                                self.editAreaTable.insert(tk.INSERT, olist[a][5])
                                self.editAreaTable.insert(tk.INSERT, '\n')
                            else:
                                self.editAreaTable.insert(tk.INSERT, '     ')
                                self.editAreaTable.insert(tk.INSERT, '-')
                                self.editAreaTable.insert(tk.INSERT, olist[a][3])
                                self.editAreaTable.insert(tk.INSERT, ' $')
                                self.editAreaTable.insert(tk.INSERT, olist[a][5])
                                self.editAreaTable.insert(tk.INSERT, '\n')
                            no += 1
                        else:
                            no = 0

                    cursor.execute("select sum(price*QUANTITY) from order_product WHERE ORDER_ID={0}".format(order[e]))
                    for c in cursor.fetchall():
                        total = c[0]

                    self.editAreaTable.insert(tk.INSERT, "\nTotal:" + str(total))
                    self.editAreaTable.insert(tk.INSERT, "\n\n\n\n")

                self.editAreaTable.config(state="disabled")

                self.order_status = ''
                self.order_id = ''

                self.ous_list = ''

            else:
                self.order_status = self.editAreaTable3.get("1.0", END)
                self.editAreaTable2.insert(tk.INSERT, self.order_status)
                self.editAreaTable2.insert(tk.INSERT, "It must be 'Prepared'/'Shipped' /'Submit'\nTry Again:")
                self.editAreaTable3.delete("1.0", END)
                self.editAreaTable3.see("end")
                self.order_status = ''
                self.ous_list = ''

    def __init__(self, root, id):
        self.id = id

        self.root = root
        self.root.geometry('1920x1080')

        self.frameRt = tk.Frame(self.root, background="WHITE")
        self.frameRt.pack(fill="both")

        self.right_frame = Frame(self.root, background="WHITE",
                                 borderwidth=5, relief="ridge")
        self.right_frame.pack(side="right", fill="both",
                              )

        self.frameR1 = tk.Frame(self.right_frame)

        self.frameR1.pack()

        self.frameR2 = tk.Frame(self.right_frame)

        self.frameR2.pack()

        self.frameR3 = tk.Frame(self.right_frame)

        self.frameR3.pack()

        self.frameR4 = tk.Frame(self.right_frame)

        self.frameR4.pack()

        self.frameR5 = tk.Frame(self.right_frame)

        self.frameR5.pack()

        self.frameR6 = tk.Frame(self.right_frame)

        self.frameR6.pack()

        self.frameR7 = tk.Frame(self.right_frame)

        self.frameR7.pack()

        self.frameR8 = tk.Frame(self.right_frame)

        self.frameR8.pack()
        self.frameR9 = tk.Frame(self.right_frame)

        self.frameR9.pack()

        cursor.execute("select Shop_location from shop_login WHERE shop_id='{0}'".format(self.id))
        for i in cursor.fetchall():
            print(i, i[0])
            location = i[0]

        self.name_label2 = tk.Label(self.frameRt, text="Pizza Hut  {0}-{1}      ".format(id, location),
                                    font=("times", 15, "bold "), bg='WHITE',
                                    fg="BLACK")

        self.name_label2.pack(side=tk.LEFT)

        self.clock1 = clock.Clock(self.frameRt)
        self.clock1.pack(side=tk.LEFT)
        self.clock1.configure(font=("times", 15, "bold "), bg='WHITE', fg="BLACK")

        tk.Button(self.frameR1, text="refresh", font=("times", 15, "bold "), fg="black", bg="white", width=10,
                  height=2, command=lambda: self.json_get()).pack(side=tk.LEFT)

        tk.Button(self.frameR1, text="order history", font=("times", 15, "bold "), fg="black", bg="white", width=10,
                  height=2, command=lambda: self.order_history()).pack(side=tk.LEFT)

        tk.Button(self.frameR1, text="Logout", font=("times", 15, "bold "), fg="black", bg="white", width=10,
                  height=2, command=lambda: self.logout()).pack(side=tk.LEFT)

        self.editAreaTable2 = tkst.ScrolledText(self.frameR2, height=6, width=30, background="WHITE", fg="black",
                                                font=("courier new", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable2.insert(tk.INSERT, "Please input a order id to update the status:")

        self.editAreaTable3 = tkst.ScrolledText(self.frameR3, height=2, width=30, background="WHITE", fg="black",
                                                font=("courier new", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameR4, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR4, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR4, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("9")).pack(
            side=tk.LEFT)

        tk.Button(self.frameR5, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR5, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR5, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("6")).pack(
            side=tk.LEFT)

        tk.Button(self.frameR6, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR6, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR6, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("3")).pack(
            side=tk.LEFT)

        tk.Button(self.frameR7, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command=lambda: self.add_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=7,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameR7, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=7,
                  height=2, command=lambda: self.add_page_editarea("del")).pack(
            side=tk.LEFT)

        tk.Button(self.frameR8, text="Submit", font=("Helvetica", 20, "bold "), fg="white", bg="green", width=7,
                  height=2, command=lambda: self.add_page_editarea("Submit")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR8, text="Shipped", font=("Helvetica", 20, "bold "), fg="white", bg="green", width=7,
                  height=2, command=lambda: self.add_page_editarea("Shipped")).pack(
            side=tk.LEFT)
        tk.Button(self.frameR8, text="Prepared", font=("Helvetica", 20, "bold "), fg="white", bg="green",
                  width=7,
                  height=2, command=lambda: self.add_page_editarea("Prepared")).pack(
            side=tk.LEFT)

        tk.Button(self.frameR9, text="Enter", font=("Helvetica", 20, "bold "), fg="white", bg="dark orange3", width=22,
                  height=2, command=lambda: self.add_page_editarea("Enter")).pack(
            side=tk.LEFT)

        self.left_frame = Frame(self.root, background="WHITE",
                                borderwidth=5, relief="ridge")
        self.left_frame.pack(side="left", fill="both",
                             )
        self.frameL = tk.Frame(self.left_frame)

        self.frameL.pack()

        self.editAreaTable = tkst.ScrolledText(self.frameL, height=50, width=80, background="white", fg="black",
                                               font=("times", 20, "bold"))

        self.editAreaTable.pack(fill="both", expand="yes", side="left")

        self.ous_list = []
        self.order_id = ''
        self.order_status = ''

        '''
        while True:
            get = requests.get('http://127.0.0.1:3000/getdata')  # GET request
            self.Order = get.json()

            # with open('Order.json', 'r') as json_file:
            # self.Order = json.load(json_file)



            self.editAreaTable.config(state="normal")
            self.editAreaTable.delete("1.0", END)
            self.editAreaTable.insert(tk.INSERT, self.Order)

            self.editAreaTable.config(state="disabled")
            time.sleep(1)  # then wait one second
        '''


def main(id, window):
    root = tk.Tk()
    Gui(root, id)
    window.destroy()
    root.mainloop()


if __name__ == '__main__':
    sys.exit(main())

