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
# import cx_Oracle
import login_loop_302
import clock
import json
import pymysql
import requests


class Gui:
    def last_page(self, page):

        if page == "table_sub":
            self.left_frame.pack_forget()
            self.main_page(1, [], '')
            self.table_id_nm = ""

        elif page == "address_page":
            self.left_frame.pack_forget()
            self.address_list = []
            self.main_page(1, [], '')

        elif page == "check_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            self.main_page(1, [], '')
        else:
            self.address_list = ''
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list=[]
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.delivery_list = []

    def last_page_tb(self, page, table_no):
        if page == "set_tb":
            self.left_frame.pack_forget()

            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_sub(self.table_id_nm, table_no)



        else:
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.address_list = ''
            self.table_sub(self.table_id_nm, table_no)
            self.delivery_list = []

    def last_page_switch(self, table_id, number):
        self.left_frame.pack_forget()

        # self.add_pd_list = []
        # self.add_qty_list = []
        # self.add_link_list = []
        self.add_link_price_list = []
        print(table_id)
        print(number)
        self.table_sub(table_id, int(number))

    def home_page(self, page):

        if page == "add_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.main_page(1, [], '')



        elif page == "check_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            self.main_page(1, [], '')


        elif page == "del_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.main_page(1, [], '')
            self.delivery_list = []
            self.address_list = ''

        else:
            self.left_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.main_page(1, [], '')
            self.delivery_list = []
            self.address_list = ''

    def json_create(self):
        latest_order_id = []
        cur = self.conn.cursor()
        cur.execute("SELECT max(`ORDER_ID`) from `order`")
        for row in cur.fetchall():
            latest_order_id.append(row)

        print(latest_order_id[0])
        # print(str(latest_order_id[0])[19:-1])


        latest_order_pd_id = []
        cur = self.conn.cursor()
        cur.execute("SELECT max(`ORDER_PRODUCT_ID`) from `order_product`")
        for row in cur.fetchall():
            latest_order_pd_id.append(row)

        delivery_fee = []
        cur = self.conn.cursor()
        cur.execute(
            "select delivery_fee from shop where SHOP_ID = '" + str(self.shop_id_choose[0]) + "'")
        for row in cur.fetchall():
            delivery_fee.append(row)

        # print(latest_order_pd_id[0])
        # print(str(latest_order_pd_id[0])[27:-1])
        new_latest_order_id = int(str(latest_order_id[0])[19:-1]) + 1
        new_latest_order_pd_id = int(str(latest_order_pd_id[0])[27:-1]) + 1
        date_string = datetime.datetime.now()
        print(new_latest_order_id)

        if (str(self.user_address[0])[15:-1]) == '0':
            sql = (
                "insert into `order` (`ORDER_ID`,`ORDER_DATE_TIME`,`ORDER_STATUS`,`MEMBER_ID`,`address_id`,`payment_id`,`shop_id`,`delivery_fee`) values (" + str(
                    new_latest_order_id) + ",'" + str(date_string.strftime('%Y/%m/%d %H:%M:%S')) + "','submit','" + str(
                    self.id) + "','" + str(self.user_address[0])[14:-1] + "','" + str(self.user_payment[0])[
                                                                                  14:-1] + "','" + str(
                    self.shop_id_choose[0]) + "'," + '0' + ") ")

        else:
            sql = (
                "insert into `order` (`ORDER_ID`,`ORDER_DATE_TIME`,`ORDER_STATUS`,`MEMBER_ID`,`address_id`,`payment_id`,`shop_id`,`delivery_fee`) values (" + str(
                    new_latest_order_id) + ",'" + str(date_string.strftime('%Y/%m/%d %H:%M:%S')) + "','submit','" + str(
                    self.id) + "','" + str(self.user_address[0])[14:-1] + "','" + str(self.user_payment[0])[
                                                                                  14:-1] + "','" + str(
                    self.shop_id_choose[0]) + "'," + str(delivery_fee[0])[16:-1] + ") ")

        self.cur.execute(sql)
        self.cur.execute("""set session transaction isolation level READ COMMITTED""")
        # self.cur.autocommit(True)


        i = 0
        while i < len(self.add_pd_list):
            if str(self.add_link_list[i]) == "/":
                sql2 = (
                "insert into `order_product` (`ORDER_ID`,`PRODUCT_ID`,`QUANTITY`,`PRICE`,`LINK_PRODUCT`) values (" + str(
                    new_latest_order_id) + ",'" + str(self.add_id_list[i]) + "','" + str(
                    self.add_qty_list[i]) + "','" + str(self.add_price_list[i]) + "','" + str(
                    self.add_link_list[i]) + "') ")
            else:
                sql2 = (
                    "insert into `order_product` (`ORDER_ID`,`PRODUCT_ID`,`QUANTITY`,`PRICE`,`LINK_PRODUCT`) values (" + str(
                        new_latest_order_id) + ",'" + str(self.add_id_list[i]) + "','" + str(
                        self.add_qty_list[i]) + "','" + str(self.add_price_list[i]) + "','" + str(
                        self.add_id_list[i - 1]) + "') ")

            self.cur.execute(sql2)
            self.cur.execute('commit')
            i += 1

        print(str(new_latest_order_id))

        Order = {
            "ORDER_ID": str(new_latest_order_id),
            "ORDER_TIME": str(date_string.strftime('%Y/%m/%d %H:%M:%S')),
            "ORDER_PRODUCT_ID": self.add_id_list,
            "LINK_PRODUCT": self.add_link_list,
            "ORDER_PRODUCT_NAME": self.add_pd_list,
            "ORDER_QUANTITY": self.add_qty_list,
            "PRICE": self.add_price_list,
            "ADDRESS": (str(self.user_address[0])[14:-1]),
            "STATUS": "submit",
            "SHOP_ID":str(self.shop_id_choose[0])
            # "DELIVERY_PRICE": "20",

        }

        post = requests.post('http://127.0.0.1:3000/postdata', json=Order)  # the POST request
        print(post.text)

        '''
        i = 0
        while i < len(self.add_pd_list):
            Order = {
                "ORDER_ID": "O001",
                "ORDER_TIME": str(date_string.strftime('%Y/%m/%d %H:%M:%S')),
                "ORDER_PRODUCT_ID": self.add_id_list[i],
                "LINK_PRODUCT": self.add_link_list[i],
                "ORDER_PRODUCT_NAME": self.add_pd_list[i],
                "ORDER_QUANTITY": self.add_qty_list[i],
                "PRICE": self.add_price_list[i],
                # "DELIVERY_PRICE": "20",

            }
            i += 1
            post = requests.post('http://127.0.0.1:3000/postdata', json=Order)  # the POST request
            print(post.text)
        '''
        # time.sleep(1)
        # with open('Order.json', 'w') as json_file:
        # json.dump(Order, json_file)

        self.date_label.config(
            text='Welcome ' + str(self.user_name[0])[22:-2] + "      " + "Order Submitted" + "      " + str(
                self.date.strftime('%Y/%m/%d') + '      '))

        self.add_id_list = []
        self.add_link_list = []
        self.add_price_list = []
        self.add_qty_list = []
        self.add_pd_list = []
        self.shop_id_choose=[]
        self.left_frame.pack_forget()
        self.middle_frame.pack_forget()
        self.btnbag.config(text="Bag: 0")
        self.main_page(1, [], '')

    def bag(self, check):
        '''
               when button clicked
               '''
        print(self.add_qty_list)
        self.left_frame.pack_forget()
        if check == "2":
            self.middle_frame.pack_forget()
        self.del_list = ''
        self.del_pd_id = ''
        self.del_pd_qty = ''

        section = 'del_pd'

        if section == "del_pd" or section == "del_check":
            self.btnTR1.config(text='Address', command=lambda: self.bag_address(), bg='dark slate gray')

            self.btnTR2.config(text='Payment', command=lambda: self.bag_payment(), bg='dark slate gray')

            self.btnTR3.config(text='', command='', bg='grey20')

            self.btnTR4.config(text='', command='', bg='grey20')

            self.btnTR5.config(text='', command='', bg='grey20')

            self.btnTR6.config(text='', command='', bg='grey20')

            self.btnTR7.config(text='', command='', bg='grey20')

            self.btnTR8.config(text='Submit', command=lambda: self.json_create(), bg='dark green')

        if section == "del_pd":
            self.btnBack.config(command=lambda: self.last_page_tb("del_order"))
        elif section == "del_check":
            self.btnBack.config(command=lambda: self.check_page("add_order"))

        self.btnHome.config(command=lambda: self.home_page("del_order"))
        self.btnBack.config(command=lambda: self.home_page("del_order"))

        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )
        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("courier new", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")

        order_item = []
        order_created_time = []
        order_product_id = []
        product_id = []
        product_name = []
        order_time = []
        order_quantity = []
        order_price = []
        order_link = []

        self.editAreaTable.insert(tk.INSERT, "No./Name/Qty/$\n")
        length = len(self.add_pd_list)
        total_price=0
        i = 0
        while i < length:
            self.add_no_list.append(i)
            if self.add_link_list[i] == "/":
                self.editAreaTable.insert(tk.INSERT, str(i) + ' ')
                # self.editAreaTable.insert(tk.INSERT, self.add_id_list[i])
                # self.editAreaTable.insert(tk.INSERT, ' ')
                self.editAreaTable.insert(tk.INSERT, self.add_pd_list[i])
                self.editAreaTable.insert(tk.INSERT, ' ')
                self.editAreaTable.insert(tk.INSERT, self.add_qty_list[i])
                self.editAreaTable.insert(tk.INSERT, ' $')
                self.editAreaTable.insert(tk.INSERT, self.add_price_list[i])
                total_price+=float(self.add_price_list[i])
                self.editAreaTable.insert(tk.INSERT, '\n')

            else:
                self.editAreaTable.insert(tk.INSERT, '     ')
                # self.editAreaTable.insert(tk.INSERT, self.add_id_list[i])
                self.editAreaTable.insert(tk.INSERT, '-')
                self.editAreaTable.insert(tk.INSERT, self.add_pd_list[i])
                # self.editAreaTable.insert(tk.INSERT, ' ')
                # self.editAreaTable.insert(tk.INSERT, self.add_qty_list[i])
                self.editAreaTable.insert(tk.INSERT, ' $')
                self.editAreaTable.insert(tk.INSERT, self.add_price_list[i])
                total_price += float(self.add_price_list[i])
                self.editAreaTable.insert(tk.INSERT, '\n')
            i += 1

        credit_card = []
        cur = self.conn.cursor()
        # print('test4'+str(self.user_payment[0]))
        # print('test5' + str(self.user_payment[0])[14:-1])
        cur.execute("select Credit_card_number from member_payment where payment_id = '" + str(self.user_payment[0])[
                                                                                           14:-1] + "'")
        for row in cur.fetchall():
            credit_card.append(row)
        print("test6" + str(credit_card[0]))
        address = []
        cur = self.conn.cursor()
        cur.execute(
            "select address from member_address where address_id = '" + str(self.user_address[0])[14:-1] + "'")
        for row in cur.fetchall():
            address.append(row)

        shop_name = []
        cur = self.conn.cursor()
        cur.execute(
            "select SHOP_NAME from shop where SHOP_ID = '" + str(self.shop_id_choose[0]) + "'")
        for row in cur.fetchall():
            shop_name.append(row)

        delivery_fee = []
        cur = self.conn.cursor()
        cur.execute(
            "select delivery_fee from shop where SHOP_ID = '" + str(self.shop_id_choose[0]) + "'")
        for row in cur.fetchall():
            delivery_fee.append(row)

        # print(str(credit_card[0])[36:-2])
        # print(str(address[0])[13:-2])


        # str(self.user_payment[0])[14:-1]
        self.editAreaTable.insert(tk.INSERT, '\n')
        self.editAreaTable.insert(tk.INSERT, '\n')





        if str(self.user_payment[0])[15:-1] == '0':
            self.editAreaTable.insert(tk.INSERT, 'Credit Card: ' + str(credit_card[0])[24:-2] + '\n')
        else:
            self.editAreaTable.insert(tk.INSERT, 'Credit Card: ' + str(credit_card[0])[36:-2] + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Address: ' + str(address[0])[13:-2] + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Shop: ' + str(shop_name[0])[14:-2] + '\n')

        #print('hi' + str(self.user_address[0])[14:-1])


        if (str(self.user_address[0])[15:-1])  == '0':
            self.editAreaTable.insert(tk.INSERT, 'Delivery fee: ' + '0' + '\n')
        else:
            self.editAreaTable.insert(tk.INSERT, 'Delivery fee: ' + str(delivery_fee[0])[16:-1] + '\n')
            total_price += float(str(delivery_fee[0])[16:-1])
        self.editAreaTable.insert(tk.INSERT, '\n')
        self.editAreaTable.insert(tk.INSERT, 'Total: $' + str(total_price) + '\n')

        self.editAreaTable.config(state="disabled")

        self.frameM1 = tk.Frame(self.middle_frame)
        self.frameM1.pack()

        if section == "del_pd" or section == "del_check":
            tk.Label(self.frameM1, bg='black', text='Modify Order',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.frameM1 = tk.Frame(self.middle_frame)
        self.frameM1.pack()
        self.frameM2 = tk.Frame(self.middle_frame)
        self.frameM2.pack()
        self.frameM3 = tk.Frame(self.middle_frame)
        self.frameM3.pack()
        self.frameM4 = tk.Frame(self.middle_frame)
        self.frameM4.pack()
        self.frameM5 = tk.Frame(self.middle_frame)
        self.frameM5.pack()
        self.frameM6 = tk.Frame(self.middle_frame)
        self.frameM6.pack()
        self.frameM7 = tk.Frame(self.middle_frame)
        self.frameM7.pack()
        self.frameM8 = tk.Frame(self.middle_frame)
        self.frameM8.pack()
        self.frameM9 = tk.Frame(self.middle_frame)
        self.frameM9.pack()

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("courier new", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("courier new", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        order_id = self.editAreaTable3.get("1.0", END)[0:-1]
        if section == "del_pd" or section == "del_check":
            tk.Button(self.frameM8, text="-Delete", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                      width=8, height=2, command=lambda: self.delete_from_order(order_id)).pack(
                side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Order_product_id to modify: ')

    def add_order_demo(self, check):
        if check == 'supreme':
            self.editAreaTable.delete("1.0", END)
            self.editAreaTable2.delete("1.0", END)
            self.editAreaTable.insert(tk.INSERT, "1. Supreme ")
            self.editAreaTable2.insert(tk.INSERT, "Input Quantity")
        elif check == 'super_supreme':
            self.editAreaTable.delete("1.0", END)
            self.editAreaTable2.delete("1.0", END)
            self.editAreaTable.insert(tk.INSERT, "1. Super Supreme ")
            self.editAreaTable2.insert(tk.INSERT, "Input Quantity")
        elif check == 'cancel':
            self.editAreaTable.delete("1.0", END)


        elif check == "add":
            self.editAreaTable2.delete("1.0", END)
            self.editAreaTable.delete("1.0", END)
            self.editAreaTable2.insert(tk.INSERT, "Product added to bag")
            print("1")
        elif check == "1":
            self.editAreaTable.delete("1.0", END)
            self.editAreaTable2.delete("1.0", END)
            self.editAreaTable.insert(tk.INSERT, "1. Super Supreme x1 $168")
            self.editAreaTable2.insert(tk.INSERT, "Press Add to confirm")
        pass

    def add_page_editarea(self, choice):
        if choice == "del" and self.add_list != "":

            self.add_list = self.add_list[:-1]
            self.editAreaTable2.delete("1.0", END)
            self.editAreaTable2.insert(tk.INSERT, self.add_list)
        elif choice == "del":
            pass
        elif choice == "Clear":
            """
            self.add_list = ""
            self.editAreaTable2.delete("1.0", END)
            """
            pass
        else:
            self.add_list += choice
            self.editAreaTable2.insert(tk.INSERT, choice)

    def add_to_cart(self, category, section):
        if self.add_list == "":
            pass
        elif self.add_pd_list != "":
            length_pd_list = len(self.add_pd_list)
            length_add_qty_list = len(self.add_qty_list)

            for i in range(0, (length_pd_list - length_add_qty_list)):
                self.add_qty_list.append(self.add_list)

            t = 0
            self.add_price_list = []
            while t < len(self.add_id_list):
                print("t" + str(t))
                crust_list = []
                cur = self.conn.cursor()
                cur.execute(
                    "Select product_price from product where product_id = '" + str(self.add_id_list[t]) + "'")
                for row in cur.fetchall():
                    crust_list.append(row)

                # print(str(crust_list[0])[17:-1])
                # print(float(str(crust_list[0])[17:-1]) * int(self.add_qty_list[t]))
                self.add_price_list.append(float(str(crust_list[0])[17:-1]) * int(self.add_qty_list[t]))
                t += 1

            print(self.add_price_list)
            self.add_list = ""
            self.editAreaTable2.delete("1.0", END)
            self.editAreaTable.delete("1.0", END)
            for i in range(0, length_pd_list):
                self.editAreaTable.insert(tk.INSERT, self.add_id_list[i] + " " + self.add_pd_list[i] + "\n" + " Qty: " +
                                          self.add_qty_list[i] + "\n")
            self.editAreaTable.see("end")

            x = 0
            bag_counter = 0
            while x < len(self.add_link_list):
                print(self.add_link_list[x])
                if self.add_link_list[x] == "/":
                    bag_counter += 1
                x += 1

            self.btnbag.config(text="Bag: " + str(bag_counter))

            self.add_order_pizza(section)

    def add_pd(self, choice, category, section):
        self.editAreaTable2.delete("1.0", END)
        if section == "Add_pd":
            self.btnTR1.config(text='', background="gray20", command='')

            self.btnTR2.config(text='Pizza', background="dark slate gray",
                               command=lambda: self.add_order_pizza(section))

            self.btnTR3.config(text='Pasta/Rice', background="dark slate gray",
                               command=lambda: self.add_order_rice(section))

            self.btnTR4.config(text="", background="gray20", command='')

            self.btnTR5.config(text="", background="gray20", command='')

            self.btnTR6.config(text="", background="gray20", command='')

            self.btnTR7.config(text='', background="gray20", command='')

            self.btnTR8.config(text='', background="gray20",
                               command='')
        '''
        elif section == "Add_pd_p_t" or section == "Add_pd_check" :
            self.btnTR1.config(text='Starter', background="dark slate gray",
                               command=lambda: self.add_order_starter(section))

            self.btnTR2.config(text='Pizza', background="dark slate gray",
                               command=lambda: self.add_order_pizza(section))

            self.btnTR3.config(text='Pasta/Rice', background="dark slate gray",
                               command=lambda: self.add_order_rice_pasta(section))

            self.btnTR4.config(text="Dessert", background="dark slate gray",
                               command=lambda: self.add_order_dessert(section))

            self.btnTR5.config(text="Drinks", background="dark slate gray",
                               command=lambda: self.add_order_drink(section))

            self.btnTR6.config(text="Special", background="dark slate gray",
                               command=lambda: self.add_order_special(section))

            self.btnTR7.config(text='Set', background="dark slate gray", command=lambda: self.add_order_set(section))

            self.btnTR8.config(text='', background="grey20",
                               command='')
        '''
        self.set_option_count = 0
        self.creator_option_count = 0
        id_end = ''
        name_start = ''
        count = 0
        '''
        for e in range(0, len(choice)):
            if choice[e] == "'":
                count += 1
            if id_end == '' and count == 2:
                id_end = e
            if name_start == '' and count == 3:
                name_start = e
        '''
        print(category)
        print('choice' + choice)
        if category == 'pizza':
            choice_id = choice[16:20]
            choice_name = choice[40:-2]
            self.add_link_list.append(str(len(self.add_pd_list) - 1))
            self.add_link_price_list.append('Y')
            self.add_id_list.append(choice_id)
            self.add_pd_list.append(choice_name)

            self.editAreaTable.insert(tk.INSERT, choice_id + " " + choice_name + "\n")

        '''
        elif  category == 'drink':
            print(choice)
            choice_id = choice[2:id_end]
            choice_name = choice[name_start + 1:-2]
            self.add_link_list.append(str(len(self.add_pd_list) - 1))
            self.add_link_price_list.append('Y')
            self.add_pd_list.append(choice)
            self.add_pd_location=''
            self.editAreaTable.insert(tk.INSERT, choice_id + " "+ choice_name + "\n")

        elif category == 'set':
            choice_id = choice[2:id_end]
            choice_name = choice[name_start + 1:-2]
            self.add_link_list.append(self.add_pd_location)
            self.add_link_price_list.append('Y')
            self.add_pd_list.append(choice)

            self.editAreaTable.insert(tk.INSERT, choice_id + " "+ choice_name + "\n")

        elif category == 'creator':
            self.add_pd_location=''
            pass

        elif category != '':
            choice_id = choice[2:id_end]
            choice_name = choice[name_start + 1:-2]
            self.add_pd_list.append(choice)
            self.add_link_list.append('/')
            self.add_link_price_list.append('Y')
            self.editAreaTable.insert(tk.INSERT, choice_id +" "+ choice_name + "\n")
        '''
        self.editAreaTable.insert(tk.INSERT, "\n" + "Quantity?" + "\n")
        self.editAreaTable.see("end")
        self.lable_pd.config(text='')

        for i in range(0, 45):
            self.btn_pd[0][i].config(text=" ", command='')

    def drink(self, choice, section):
        self.btnTR1.config(text='', command='', bg='grey20')

        self.btnTR2.config(text='', command='', bg='grey20')

        self.btnTR3.config(text='', command='', bg='grey20')

        self.btnTR4.config(text='', command='', bg='grey20')

        self.btnTR5.config(text='', command='', bg='grey20')

        self.btnTR6.config(text='', command='', bg='grey20')

        self.btnTR7.config(text='', command='', bg='grey20')

        self.btnTR8.config(text='', command='', bg='grey20')
        choice_id = choice[16:20]
        choice_name = choice[40:-2]
        # print(choice_id)
        # print(choice_name)
        self.add_id_list.append(choice_id)
        self.add_pd_list.append(choice_name)
        self.add_link_list.append('/')
        self.add_link_price_list.append('Y')

        crust_list = []
        self.editAreaTable.insert(tk.INSERT, choice_id + " " + choice_name + "\n")
        self.editAreaTable.see("end")
        cur = self.conn.cursor()
        cur.execute(
            "Select product_id, product_name from product where product_category = 'DRINK' order by product_id")
        for row in cur.fetchall():
            crust_list.append(row)

        self.lable_pd.config(text='Crust')

        length_data = len(crust_list)

        for i in range(0, 45):
            self.btn_pd[0][i].config(text=" ", command='')

        for i in range(0, int(length_data)):
            t_id = str(crust_list[i])
            t_name = str(crust_list[i])
            self.btn_pd[0][i].config(text=(t_id[16:20] + "\n" + t_name[40:-2]),
                                     command=lambda i=i: self.add_pd(str(crust_list[i]), "pizza", section))

    def add_order_rice(self, section):
        '''
        when button clicked
        '''

        pizza_list = []
        cur = self.conn.cursor()
        cur.execute(
            "Select product_id, product_name from product where product_category = 'RICE/PASTA' order by product_id")
        for row in cur.fetchall():
            pizza_list.append(row)

        self.lable_pd.config(text='Rice/Pasta')
        print(pizza_list[0])
        length_data = len(pizza_list)
        for i in range(0, length_data):
            t_id = str(pizza_list[i])
            t_name = str(pizza_list[i])
            self.btn_pd[0][i].config(text=(t_id[16:20] + "\n" + t_name[40:-2]),
                                     command=lambda i=i: self.drink(str(pizza_list[i]), section))

        for i in range(length_data, 45):
            self.btn_pd[0][i].config(text=("\n"), command='')

    def crust(self, choice, section):
        self.btnTR1.config(text='', command='', bg='grey20')

        self.btnTR2.config(text='', command='', bg='grey20')

        self.btnTR3.config(text='', command='', bg='grey20')

        self.btnTR4.config(text='', command='', bg='grey20')

        self.btnTR5.config(text='', command='', bg='grey20')

        self.btnTR6.config(text='', command='', bg='grey20')

        self.btnTR7.config(text='', command='', bg='grey20')

        self.btnTR8.config(text='', command='', bg='grey20')
        choice_id = choice[16:20]
        choice_name = choice[40:-2]
        print(choice_id)
        # print(choice_name)
        self.add_id_list.append(choice_id)
        self.add_pd_list.append(choice_name)
        self.add_link_list.append('/')
        self.add_link_price_list.append('Y')

        crust_list = []
        self.editAreaTable.insert(tk.INSERT, choice_id + " " + choice_name + "\n")
        self.editAreaTable.see("end")
        cur = self.conn.cursor()
        cur.execute(
            "Select product_id, product_name from product where product_category = 'CRUST' order by product_id")
        for row in cur.fetchall():
            crust_list.append(row)

        self.lable_pd.config(text='Crust')

        length_data = len(crust_list)

        for i in range(0, 45):
            self.btn_pd[0][i].config(text=" ", command='')

        for i in range(0, int(length_data)):
            t_id = str(crust_list[i])
            t_name = str(crust_list[i])
            self.btn_pd[0][i].config(text=(t_id[16:20] + "\n" + t_name[40:-2]),
                                     command=lambda i=i: self.add_pd(str(crust_list[i]), "pizza", section))

    def add_order_pizza(self, section):
        '''
        when button clicked
        '''

        pizza_list = []
        cur = self.conn.cursor()
        cur.execute("Select product_id, product_name from product where product_category = 'PIZZA' order by product_id")
        for row in cur.fetchall():
            pizza_list.append(row)

        self.lable_pd.config(text='Pizza')
        print(pizza_list[0])
        length_data = len(pizza_list)
        for i in range(0, length_data):
            t_id = str(pizza_list[i])
            t_name = str(pizza_list[i])
            self.btn_pd[0][i].config(text=(t_id[16:20] + "\n" + t_name[40:-2]),
                                     command=lambda i=i: self.crust(str(pizza_list[i]), section))

        for i in range(length_data, 45):
            self.btn_pd[0][i].config(text=("\n"), command='')

    def add_order_template(self, shop_id):
        '''
        when button clicked
        '''

        if self.shop_id_choose == []:
            self.shop_id_choose.append(shop_id)
        else:
            self.shop_id_choose[0]=(shop_id)

        print(self.shop_id_choose[0])


        self.left_frame.pack_forget()

        section = "Add_pd"

        self.btnbag.config(command=lambda: self.bag("2"))

        if section == "Add_pd":
            self.btnTR1.config(text='', background="gray20",
                               command='')

            self.btnTR2.config(text='Pizza', background="dark slate gray",
                               command=lambda: self.add_order_pizza(section))

            self.btnTR3.config(text='Rice/Pasta', background="dark slate gray",
                               command=lambda: self.add_order_rice(section))

            self.btnTR4.config(text="", background="gray20",
                               command='')

            self.btnTR5.config(text="", background="gray20",
                               command='')

            self.btnTR6.config(text="", background="gray20",
                               command='')

            self.btnTR7.config(text='', background="gray20", command='')

            self.btnTR8.config(text='', background="gray20",
                               command='')

        '''
        elif section == "Add_pd_p_t" or section == "Add_pd_check":

            self.btnTR1.config(text='Starter', background="dark slate gray",
                               command=lambda: self.add_order_starter(section))

            self.btnTR2.config(text='Pizza', background="dark slate gray",
                               command=lambda: self.add_order_pizza(section))

            self.btnTR3.config(text='Pasta/Rice', background="dark slate gray",
                               command=lambda: self.add_order_rice_pasta(section))

            self.btnTR4.config(text="Dessert", background="dark slate gray",
                               command=lambda: self.add_order_dessert(section))

            self.btnTR5.config(text="Drinks", background="dark slate gray",
                               command=lambda: self.add_order_drink(section))

            self.btnTR6.config(text="Special", background="dark slate gray",
                               command=lambda: self.add_order_special(section))

            self.btnTR7.config(text='Set', background="dark slate gray", command=lambda: self.add_order_set(section))

            self.btnTR8.config(text='', background="grey20", command='')


        elif section == 'member' or section == 'member_check':

            self.btnTR1.config(text='Starter', background="dark slate gray",
                               command=lambda: self.add_order_starter_member())

            self.btnTR2.config(text='Pizza', background="dark slate gray",
                               command=lambda: self.add_order_pizza_member())

            self.btnTR3.config(text='Pasta/Rice', background="dark slate gray",
                               command=lambda: self.add_order_rice_pasta_member())

            self.btnTR4.config(text="Dessert", background="dark slate gray",
                               command=lambda: self.add_order_dessert_member())

            self.btnTR5.config(text="Drinks", background="dark slate gray",
                               command=lambda: self.add_order_drink_member())

            self.btnTR6.config(text='', background="grey20", command='')

            self.btnTR7.config(text='', background="grey20", command='')

            self.btnTR8.config(text='', background="grey20", command='')
        '''
        # if section == 'member' or section == "Add_pd":
        # self.btnBack.config(command=lambda: self.last_page_tb("add_order", table_no))
        '''
        elif section == "Add_pd_p_t":
            self.btnBack.config(command=lambda: self.home_page("add_order"))

        elif section == "Add_pd_check" or section == "member_check":
            self.btnBack.config(command=lambda: self.check_page("add_order"))
        '''
        self.btnHome.config(command=lambda: self.home_page("add_order"))
        self.btnBack.config(command=lambda: self.home_page("add_order"))

        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.lable_pd = tk.Label(self.frameL1, bg='black', text='Pizza',
                                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5)
        self.lable_pd.pack()

        self.btn_pd = [[0 for x in range(45)] for y in range(1)]
        for i in range(0, 5):
            self.btn_pd[0][i] = tk.Button(self.frameL3, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20, height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)

        for i in range(5, 10):
            self.btn_pd[0][i] = tk.Button(self.frameL4, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(10, 15):
            self.btn_pd[0][i] = tk.Button(self.frameL5, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(15, 20):
            self.btn_pd[0][i] = tk.Button(self.frameL6, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(20, 25):
            self.btn_pd[0][i] = tk.Button(self.frameL7, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(25, 30):
            self.btn_pd[0][i] = tk.Button(self.frameL8, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(30, 35):
            self.btn_pd[0][i] = tk.Button(self.frameL9, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(35, 40):
            self.btn_pd[0][i] = tk.Button(self.frameL10, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(40, 45):
            self.btn_pd[0][i] = tk.Button(self.frameL11, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)

            self.btn_pd[0][0].config(text="Supreme\n$148", command=lambda: self.add_order_demo("supreme"))
            self.btn_pd[0][1].config(text="Super Supreme\n$168", command=lambda: self.add_order_demo("super_supreme"))

        self.frameM1 = tk.Frame(self.middle_frame)
        self.frameM1.pack()

        if section == "Add_pd" or section == "Add_pd_p_t" or section == "Add_pd_check":
            tk.Label(self.frameM1, bg='black', text='+Add Order',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        if section == "member" or section == 'member_check':
            tk.Label(self.frameM1, bg='black', text='+Member - Table ',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.frameM1 = tk.Frame(self.middle_frame)
        self.frameM1.pack()
        self.frameM2 = tk.Frame(self.middle_frame)
        self.frameM2.pack()
        self.frameM3 = tk.Frame(self.middle_frame)
        self.frameM3.pack()
        self.frameM4 = tk.Frame(self.middle_frame)
        self.frameM4.pack()
        self.frameM5 = tk.Frame(self.middle_frame)
        self.frameM5.pack()
        self.frameM6 = tk.Frame(self.middle_frame)
        self.frameM6.pack()
        self.frameM7 = tk.Frame(self.middle_frame)
        self.frameM7.pack()
        self.frameM8 = tk.Frame(self.middle_frame)
        self.frameM8.pack()
        self.frameM9 = tk.Frame(self.middle_frame)
        self.frameM9.pack()

        self.editAreaTable = tkst.ScrolledText(self.frameM1, height=8, width=40, background="black", fg="white",
                                               font=("courier new", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")

        self.editAreaTable.insert(tk.INSERT, "")

        self.editAreaTable2 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("courier new", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable2.insert(tk.INSERT, 'Please Select Food from left column')

        tk.Button(self.frameM3, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM3, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM3, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM3, text="Cancel", font=("Helvetica", 20, "bold "), fg="white", bg="dark orange3", width=8,
                  height=2, command=lambda: self.add_order_demo("cancel")).pack(
            side=tk.LEFT)

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.add_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        if section == "Add_pd" or section == "Add_pd_p_t" or section == "Add_pd_check":
            tk.Button(self.frameM8, text="+Add", font=("Helvetica", 20, "bold "), fg="white", bg="dark green", width=8,
                      height=2, command=lambda: self.add_to_cart("pizza", section)).pack(
                side=tk.LEFT)
        '''
        elif section == "member" or section == 'member_check':
            tk.Button(self.frameM8, text="+Add", font=("Helvetica", 20, "bold "), fg="white", bg="dark green", width=8,
                      height=2, command=lambda: self.add_to_cart_member("pizza")).pack(
                side=tk.LEFT)
        '''
        if section == "Add_pd" or section == "Add_pd_p_t" or section == "Add_pd_check":
            self.add_order_pizza(section)
        '''
        elif section == 'member' or section == 'member_check':
            self.add_order_pizza_member()
        '''

    def update_name_receive(self):
        ##kenton
        self.create_label1.config(text='Your new surname: ')
        self.create_label2.config(text='Your password: ')

        AAR = 0
        address = []
        pw = []
        cur = self.conn.cursor()
        cur.execute(
            "select CUSTOMER_SURNAME from member_data where member_id  = '" + str(self.id) + "' ")
        for row in cur.fetchall():
            address.append(row)
        print(str(address[0]))
        print(str(address[0])[22:-2])
        print(str(self.create_input1.get()))
        i = 0
        while i < len(address):
            if str(self.create_input1.get()) == (str(address[i])[22:-2]):
                self.create_label1.config(text='(Repeated) Your new user name: ')
                AAR = 1
            i += 1

        cur.execute(
            "select PASSWORD from member_data where member_id  = '" + str(self.id) + "' ")

        for row in cur.fetchall():
            pw.append(row)
        i = 0
        while i < len(address):
            if str(self.create_input2.get()) == (str(pw[i])[14:-2]):
                i += 1
                pass
            else:
                AAR = 1
                self.create_label2.config(text='(Wrong) Your password: ')
                i += 1

        if AAR == 0:
            cur = self.conn.cursor()
            with self.conn.cursor() as cur:
                cur.execute("UPDATE member_data SET CUSTOMER_SURNAME= '" + str(
                    self.create_input1.get()) + "'  where MEMBER_ID = " + str(self.id) + "")
                self.create_label3.config(text='Your user name have been updated!')
            self.conn.commit()
            self.my_account()

            # self.create_submit(command=lambda: self.add_address_receive())

        #self.create_submit(command=lambda:self.my_account())
        self.my_account()

    def update_name(self):
        ##kenton
        self.left_frame.pack_forget()

        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title = tk.Label(self.frameL1, text="Update your surname", font=("Helvetica", 30),
                                     fg="white",
                                     background="black")
        self.create_title.pack(side=tk.LEFT)
        self.create_label1 = tk.Label(self.frameL2, text="Your new surname: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL3, text="Your password ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)
        self.create_input2 = tk.Entry(self.frameL3, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL5, text=" ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_submit = tk.Button(self.frameL7, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.update_name_receive())
        self.create_submit.pack(side=tk.LEFT)

        pass

    def update_email_receive(self):
        ##kenton
        self.create_label1.config(text='Your new email: ')
        self.create_label2.config(text='Your password: ')

        AAR = 0
        address = []
        pw = []
        cur = self.conn.cursor()
        cur.execute(
            "select EMAIL from member_data where member_id  = '" + str(self.id) + "' ")
        for row in cur.fetchall():
            address.append(row)
        print(str(address[0]))
        print(str(address[0])[11:-2])
        print(str(self.create_input1.get()))
        i = 0
        while i < len(address):
            if str(self.create_input1.get()) == (str(address[i])[11:-2]):
                self.create_label1.config(text='(Repeated) Your new email: ')
                AAR = 1
            i += 1

        cur.execute(
            "select PASSWORD from member_data where member_id  = '" + str(self.id) + "' ")

        for row in cur.fetchall():
            pw.append(row)
        i = 0
        while i < len(address):
            if str(self.create_input2.get()) == (str(pw[i])[14:-2]):
                i += 1
                pass
            else:
                AAR = 1
                self.create_label2.config(text='(Wrong) Your password: ')
                i += 1

        if AAR == 0:
            cur = self.conn.cursor()
            with self.conn.cursor() as cur:
                cur.execute("UPDATE member_data SET EMAIL= '" + str(
                    self.create_input1.get()) + "'  where MEMBER_ID = " + str(self.id) + "")
                self.create_label3.config(text='Your user name have been updated!')
            self.conn.commit()
            self.my_account()

        # self.create_submit(command=lambda: self.add_address_receive())

        #self.create_submit(command=lambda: self.update_email_receive())
        self.my_account()

    def update_email(self):
        ##kenton
        self.left_frame.pack_forget()

        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title = tk.Label(self.frameL1, text="Update your email", font=("Helvetica", 30),
                                     fg="white",
                                     background="black")
        self.create_title.pack(side=tk.LEFT)
        self.create_label1 = tk.Label(self.frameL2, text="Your new email: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL3, text="Your password ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)
        self.create_input2 = tk.Entry(self.frameL3, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL5, text=" ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_submit = tk.Button(self.frameL7, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.update_email_receive())
        self.create_submit.pack(side=tk.LEFT)

        pass

    def update_phone_receive(self):
        ##kenton
        self.create_label1.config(text='Your new phone number: ')
        self.create_label2.config(text='Your password: ')

        AAR = 0
        address = []
        pw = []
        cur = self.conn.cursor()
        cur.execute(
            "select PHONE_NUMBER from member_data where member_id  = '" + str(self.id) + "' ")
        for row in cur.fetchall():
            address.append(row)
        print(str(address[0]))
        print(str(address[0])[17:-1])
        print(str(self.create_input1.get()))
        i = 0
        while i < len(address):
            if str(self.create_input1.get()) == (str(address[i])[17:-1]):
                self.create_label1.config(text='(Repeated) Your new email: ')
                AAR = 1
            i += 1

        cur.execute(
            "select PASSWORD from member_data where member_id  = '" + str(self.id) + "' ")

        for row in cur.fetchall():
            pw.append(row)
        i = 0
        while i < len(address):
            if str(self.create_input2.get()) == (str(pw[i])[14:-2]):
                i += 1
                pass
            else:
                AAR = 1
                self.create_label2.config(text='(Wrong) Your password: ')
                i += 1

        if AAR == 0:
            cur = self.conn.cursor()
            with self.conn.cursor() as cur:
                cur.execute("UPDATE member_data SET PHONE_NUMBER= '" + str(
                    self.create_input1.get()) + "'  where MEMBER_ID = " + str(self.id) + "")
                self.create_label3.config(text='Your user name have been updated!')
            self.conn.commit()
            self.my_account()

        # self.create_submit(command=lambda: self.add_address_receive())

        #self.create_submit(command=lambda: self.update_phone_receive())
        self.my_account()

    def update_phone(self):
        ##kenton
        self.left_frame.pack_forget()

        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title = tk.Label(self.frameL1, text="Update your phone number", font=("Helvetica", 30),
                                     fg="white",
                                     background="black")
        self.create_title.pack(side=tk.LEFT)
        self.create_label1 = tk.Label(self.frameL2, text="Your new phone number: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL3, text="Your password ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)
        self.create_input2 = tk.Entry(self.frameL3, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL5, text=" ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_submit = tk.Button(self.frameL7, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.update_phone_receive())
        self.create_submit.pack(side=tk.LEFT)

        pass

    def update_password_receive(self):
        ##kenton
        self.create_label1.config(text='Your new password: ')
        self.create_label2.config(text='Confirm your new password: ')
        self.create_label3.config(text='Your old password: ')

        AAR = 0
        address = []
        pw = []
        cur = self.conn.cursor()
        cur.execute(
            "select PASSWORD from member_data where member_id  = '" + str(self.id) + "' ")
        for row in cur.fetchall():
            address.append(row)
        print(str(address[0]))
        print(str(address[0])[14:-2])
        print(str(self.create_input1.get()))
        i = 0
        while i < len(address):
            if str(self.create_input1.get()) == (str(address[i])[14:-2]):
                self.create_label1.config(text='(Repeated) Your new password: ')
                AAR = 1
            i += 1

        if str(self.create_input2.get()) != str(self.create_input1.get()):
            self.create_label2.config(text='(Wrong) Confirm your new password: ')
            AAR = 1

        cur.execute(
            "select PASSWORD from member_data where member_id  = '" + str(self.id) + "' ")

        for row in cur.fetchall():
            pw.append(row)
        i = 0
        while i < len(address):
            if str(self.create_input3.get()) == (str(pw[i])[14:-2]):
                i += 1
                pass
            else:
                AAR = 1
                self.create_label3.config(text='(Wrong) Your old password: ')
                i += 1

        if AAR == 0:
            cur = self.conn.cursor()
            with self.conn.cursor() as cur:
                cur.execute("UPDATE member_data SET PASSWORD= '" + str(
                    self.create_input1.get()) + "'  where MEMBER_ID = " + str(self.id) + "")
            self.conn.commit()
            self.my_account()

        # self.create_submit(command=lambda: self.add_address_receive())

        #self.create_submit(command=lambda: self.update_password_receive())
        self.my_account()

    def update_password(self):
        ##kenton
        self.left_frame.pack_forget()

        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title = tk.Label(self.frameL1, text="Update your password", font=("Helvetica", 30),
                                     fg="white",
                                     background="black")
        self.create_title.pack(side=tk.LEFT)
        self.create_label1 = tk.Label(self.frameL2, text="Your new password: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL3, text="Confirm your new password ", font=("Helvetica", 20),
                                      fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)
        self.create_input2 = tk.Entry(self.frameL3, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL5, text="Your old password", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)
        self.create_input3 = tk.Entry(self.frameL5, text="", background="white", width=100)
        self.create_input3.pack(side=tk.LEFT)

        self.create_submit = tk.Button(self.frameL7, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.update_password_receive())
        self.create_submit.pack(side=tk.LEFT)

        pass

    def my_account(self):
        '''
        when button clicked
        '''
        number = 1
        if number in range(0, 121):

            self.left_frame.pack_forget()

            self.left_frame = Frame(self.root, background="black",
                                    borderwidth=5, relief="ridge",
                                    width=1000)
            self.left_frame.pack(side="left",
                                 fill="both",
                                 expand="yes",
                                 )

            self.frameL1 = tk.Frame(self.left_frame)
            self.frameL1.pack()

            self.frameL2 = tk.Frame(self.left_frame)
            self.frameL2.pack()

            tk.Label(self.frameL1, bg='black', text=('Table ' + str(number)),
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

            self.editAreaTable2 = tkst.ScrolledText(self.frameL2, height=1, width=100, background="black", fg="white",
                                                    font=("courier new", 15, "bold"))
            self.editAreaTable2.pack(fill="both")
            self.editAreaTable2.delete("1.0", END)

            self.editAreaTable = tkst.ScrolledText(self.frameL2, height=50, width=100, background="black", fg="white",
                                                   font=("courier new", 15, "bold"))
            self.editAreaTable.pack(fill="both")
            self.editAreaTable.delete("1.0", END)

            self.cur.close()
            self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
            self.conn = pymysql.connect(user='root',
                                        password='',
                                        db='ubereat',
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.db.cursor()

            username = []
            email = []
            phone = []

            cur = self.conn.cursor()
            cur.execute(
                "select customer_surname from member_data where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                username.append(row)
            # print(str(username[0])[22:-2])

            cur = self.conn.cursor()
            cur.execute(
                "select phone_number from member_data where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                phone.append(row)
            # print(str(phone[0])[16:-1])

            cur = self.conn.cursor()
            cur.execute(
                "select email from member_data where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                email.append(row)
            # print(str(email[0])[11:-2])

            self.editAreaTable.insert(tk.INSERT, "Customer Surname: " + str(username[0])[22:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, "Phone Number: " + str(phone[0])[16:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT, "Email: " + str(email[0])[11:-2] + '\n')

            self.btnTR1.config(text='Update name', font=("Helvetica", 20, "bold "), bg="forest green",
                               command=lambda: self.update_name())
            self.btnTR2.config(text='Update email', font=("Helvetica", 20, "bold "), bg="forest green",
                               command=lambda: self.update_email())
            self.btnTR3.config(text='Update phone', font=("Helvetica", 20, "bold "), bg="forest green",
                               command=lambda: self.update_phone())
            self.btnTR4.config(text='Update pw', font=("Helvetica", 20, "bold "), bg="forest green",
                               command=lambda: self.update_password())
            self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

            self.editAreaTable.config(state="disabled")

            self.btnBack.config(command=lambda: self.last_page("table_sub"))
            self.btnHome.config(command=lambda: self.home_page("table_sub"))

    def add_address_receive(self):
        self.create_label1.config(text='Address')

        AAR = 0
        address = []
        cur = self.conn.cursor()
        cur.execute(
            "select address from member_address where member_id  = '" + str(self.id) + "' ")
        for row in cur.fetchall():
            address.append(row)
        print(str(address[0]))
        print(str(address[0])[13:-2])
        print(str(self.create_input1.get()))
        i = 0
        while i < len(address):
            if str(self.create_input1.get()) == (str(address[i])[13:-2]):
                self.create_label1.config(text='Repeated address')
                AAR = 1
            i += 1

        if AAR == 0:
            cur = self.conn.cursor()
            with self.conn.cursor() as cur:
                cur.execute("INSERT INTO member_address(Address, member_id) VALUES ('" + str(
                    self.create_input1.get()) + "','" + str(self.id) + "')")
                self.conn.commit()

                # self.create_submit(command=lambda: self.add_address_receive())

        self.my_address()

    def add_address(self):

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title = tk.Label(self.frameL1, text="Please input the followings", font=("Helvetica", 30),
                                     fg="white",
                                     background="black")
        self.create_title.pack(side=tk.LEFT)
        self.create_label1 = tk.Label(self.frameL2, text="Address: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_submit = tk.Button(self.frameL3, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.add_address_receive())
        self.create_submit.pack(side=tk.LEFT)

        pass

    def add_payment_receive(self):
        self.create_label1.config(text='Credit card number:')
        self.create_label2.config(text='CSV:')
        self.create_label3.config(text='Name:')
        self.create_label4.config(text='Expiry date:')

        AAR = 0
        Cnumber = []
        csv = []
        name = []
        Edate = []
        cur = self.conn.cursor()
        cur.execute(
            "select Credit_card_number from member_payment where member_id  = '" + str(self.id) + "' ")
        for row in cur.fetchall():
            Cnumber.append(row)
        print(str(Cnumber[0]))
        print(str(Cnumber[0])[24:-2])
        print(str(self.create_input1.get()))
        i = 0
        while i < len(Cnumber):
            if str(self.create_input1.get()) == (str(Cnumber[i])[24:-2]):
                self.create_label1.config(text='Repeated credit card number')
                AAR = 1
            i += 1

        if AAR == 0:
            cur = self.conn.cursor()
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO member_payment(Credit_card_number, CSV,  Expiry_date, Credit_card_name, member_id) VALUES ('" + str(
                        self.create_input1.get()) + "','" + str(self.create_input2.get()) + "','" + str(
                        self.create_input4.get()) + "','" + str(self.create_input3.get()) + "','" + str(self.id) + "')")
                self.conn.commit()

                # self.create_submit(command=lambda: self.add_payment_receive())

        self.my_payment()

    def add_payment(self):

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title = tk.Label(self.frameL1, text="Please input the followings", font=("Helvetica", 30),
                                     fg="white",
                                     background="black")
        self.create_title.pack(side=tk.LEFT)
        self.create_label1 = tk.Label(self.frameL2, text="Credit card number: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL3, text="CSV: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)
        self.create_input2 = tk.Entry(self.frameL3, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL4, text="Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)
        self.create_input3 = tk.Entry(self.frameL4, text="", background="white", width=100)
        self.create_input3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL5, text="Expiry Date: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)
        self.create_input4 = tk.Entry(self.frameL5, text="", background="white", width=100)
        self.create_input4.pack(side=tk.LEFT)

        self.create_submit = tk.Button(self.frameL7, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.add_payment_receive())
        self.create_submit.pack(side=tk.LEFT)

        pass

    def update_payment(self, id_value, card_number, csv, expiry, name):
        # print(new_address)
        # print(id_value)
        cur = self.conn.cursor()
        cur.execute(
            "update member_payment set `Credit_card_number` = '" + str(card_number) + "' where`payment_id` ='" + str(
                id_value) + "'")
        cur.execute("commit")
        cur = self.conn.cursor()
        cur.execute(
            "update member_payment set `CSV` = '" + str(csv) + "' where`payment_id` ='" + str(
                id_value) + "'")
        cur.execute("commit")
        cur = self.conn.cursor()
        cur.execute(
            "update member_payment set `Expiry_date` = '" + str(expiry) + "' where`payment_id` ='" + str(
                id_value) + "'")
        cur.execute("commit")
        cur = self.conn.cursor()
        cur.execute(
            "update member_payment set `Credit_card_name` = '" + str(name) + "' where`payment_id` ='" + str(
                id_value) + "'")
        cur.execute("commit")
        self.cur.close()
        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='ubereat',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()

        self.date_label.config(
            text='Welcome ' + str(self.user_name[0])[22:-2] + "      " + 'Credit card updated' + "      " + str(
                self.date.strftime('%Y/%m/%d') + '      '))
        self.my_payment()

    def update_address(self, new_address, id_value):
        # print(new_address)
        # print(id_value)
        cur = self.conn.cursor()
        cur.execute("update member_address set `Address` = '" + str(new_address) + "' where`address_id` ='" + str(
            id_value) + "'")
        cur.execute("commit")
        self.cur.close()
        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='ubereat',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()

        self.date_label.config(
            text='Welcome ' + str(self.user_name[0])[22:-2] + "      " + 'Address updated' + "      " + str(
                self.date.strftime('%Y/%m/%d') + '      '))
        self.my_address()

    def sub_address(self, id_value):
        # print("id"+str(id_value))
        address_list = []
        cur = self.conn.cursor()
        cur.execute(
            "select Address from member_address where address_id = '" + str(id_value) + "' ")
        for row in cur.fetchall():
            address_list.append(row)
        # print(str(address_list[0])[13:-2])


        self.btnBack.config(command=lambda: self.my_address())

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()
        self.create_label1 = tk.Label(self.frameL2, text="Address: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, background="white", fg="black", width=100)
        self.create_input1.pack(side=tk.LEFT)
        self.create_input1.insert(END, str(address_list[0])[13:-2])
        self.create_submit = tk.Button(self.frameL3, text='Modify', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2,
                                       command=lambda: self.update_address(str(self.create_input1.get()), id_value))
        self.create_submit.pack(side=tk.LEFT)
        '''
        self.create_submit = tk.Button(self.frameL3, text='Delete', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="red",
                                       width=12, height=2, command=lambda: self.create_account())
        self.create_submit.pack(side=tk.LEFT)
        '''

        pass

    def choose_address(self, id_value):

        New_address = []

        print(self.user_address[0])

        cur = self.conn.cursor()
        cur.execute(
            "select address_id from member_address where address_id = '" + str(id_value) + "' ")
        for row in cur.fetchall():
            New_address.append(row)
            # print(str(address_list[0])[12:-2])
        self.user_address[0] = New_address[0]
        print(self.user_address[0])

        self.bag('1')

        pass

    def bag_address(self):
        '''
        when button clicked
        '''
        number = 1
        if number in range(0, 121):

            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()

            self.left_frame = Frame(self.root, background="black",
                                    borderwidth=5, relief="ridge",
                                    width=1000)
            self.left_frame.pack(side="left",
                                 fill="both",
                                 expand="yes",
                                 )

            self.frameL1 = tk.Frame(self.left_frame)
            self.frameL1.pack()
            self.frameL2 = tk.Frame(self.left_frame)
            self.frameL2.pack()
            self.frameL3 = tk.Frame(self.left_frame)
            self.frameL3.pack()
            self.frameL4 = tk.Frame(self.left_frame)
            self.frameL4.pack()
            self.frameL5 = tk.Frame(self.left_frame)
            self.frameL5.pack()
            self.frameL6 = tk.Frame(self.left_frame)
            self.frameL6.pack()
            self.frameL7 = tk.Frame(self.left_frame)
            self.frameL7.pack()
            self.frameL8 = tk.Frame(self.left_frame)
            self.frameL8.pack()
            self.frameL9 = tk.Frame(self.left_frame)
            self.frameL9.pack()
            self.frameL10 = tk.Frame(self.left_frame)
            self.frameL10.pack()
            self.frameL11 = tk.Frame(self.left_frame)
            self.frameL11.pack()

            tk.Label(self.frameL1, bg='black', text=('Saved Address'),
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

            self.btn_pd = [[0 for x in range(11)] for y in range(1)]
            for i in range(0, 1):
                self.btn_pd[0][i] = tk.Button(self.frameL3,
                                              text="Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK",
                                              font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150, height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)

            for i in range(1, 2):
                self.btn_pd[0][i] = tk.Button(self.frameL4, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(2, 3):
                self.btn_pd[0][i] = tk.Button(self.frameL5, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(3, 4):
                self.btn_pd[0][i] = tk.Button(self.frameL6, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(4, 5):
                self.btn_pd[0][i] = tk.Button(self.frameL7, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(5, 6):
                self.btn_pd[0][i] = tk.Button(self.frameL8, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(6, 7):
                self.btn_pd[0][i] = tk.Button(self.frameL9, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(7, 8):
                self.btn_pd[0][i] = tk.Button(self.frameL10, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(9, 10):
                self.btn_pd[0][i] = tk.Button(self.frameL11, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)

            self.btnTR1.config(text='Take Away', font=("Helvetica", 20, "bold "), bg="grey20",
                               command=lambda i=i: self.choose_address(str('0')))
            self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

            self.editAreaTable.config(state="disabled")

            address_list = []
            address_id_list = []
            cur = self.conn.cursor()
            cur.execute(
                "select Address from member_address where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                address_list.append(row)
            # print(str(address_list[0])[12:-2])


            cur = self.conn.cursor()
            cur.execute(
                "select address_id from member_address where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                address_id_list.append(row)
            # print(str(address_id_list[0])[15:-1])
            print(len(address_list))
            print(len(address_id_list))

            t_id_list = []
            for i in range(0, len(address_list)):

                t_id = str(address_id_list[i])
                t_id_list.append(t_id[15:-1])
                if i == 0:
                    self.btn_pd[0][i].config(text="Default: " + str(address_list[i])[13:-2],
                                             command=lambda i=i: self.choose_address(str(t_id_list[i])))
                else:
                    self.btn_pd[0][i].config(text=str(address_list[i])[13:-2],
                                             command=lambda i=i: self.choose_address(str(t_id_list[i])))

            # self.btnBack.config(command=lambda: self.last_page("table_sub"))
            self.btnHome.config(command=lambda: self.home_page("table_sub"))

    def sub_payment(self, id_value):

        # print("id"+str(id_value))
        Credit_card_number = []
        cur = self.conn.cursor()
        cur.execute(
            "select Credit_card_number from member_payment where payment_id = '" + str(id_value) + "' ")
        for row in cur.fetchall():
            Credit_card_number.append(row)
        # print(str(Credit_card_number[0])[36:-2])

        CSV = []
        cur = self.conn.cursor()
        cur.execute(
            "select CSV from member_payment where payment_id = '" + str(id_value) + "' ")
        for row in cur.fetchall():
            CSV.append(row)
        # print(str(CSV[0])[8:-2])

        expiry_date = []
        cur = self.conn.cursor()
        cur.execute(
            "select expiry_date from member_payment where payment_id = '" + str(id_value) + "' ")
        for row in cur.fetchall():
            expiry_date.append(row)
        # print(str(expiry_date[0])[16:-2])

        Credit_card_name = []
        cur = self.conn.cursor()
        cur.execute(
            "select Credit_card_name from member_payment where payment_id = '" + str(id_value) + "' ")
        for row in cur.fetchall():
            Credit_card_name.append(row)
        # print(str(Credit_card_name[0])[21:-2])


        self.btnBack.config(command=lambda: self.my_payment())

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()
        self.create_label1 = tk.Label(self.frameL2, text="Card Number: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, background="white", fg="black", width=100)
        self.create_input1.pack(side=tk.LEFT)
        self.create_input1.insert(END, "************" + str(Credit_card_number[0])[36:-2])

        self.create_label2 = tk.Label(self.frameL3, text="CSV: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)
        self.create_input2 = tk.Entry(self.frameL3, background="white", fg="black", width=100)
        self.create_input2.pack(side=tk.LEFT)
        self.create_input2.insert(END, str(CSV[0])[9:-2])

        self.create_label3 = tk.Label(self.frameL4, text="Expiry Date: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)
        self.create_input3 = tk.Entry(self.frameL4, background="white", fg="black", width=100)
        self.create_input3.pack(side=tk.LEFT)
        self.create_input3.insert(END, str(expiry_date[0])[17:-2])

        self.create_label4 = tk.Label(self.frameL5, text="Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)
        self.create_input4 = tk.Entry(self.frameL5, background="white", fg="black", width=100)
        self.create_input4.pack(side=tk.LEFT)
        self.create_input4.insert(END, str(Credit_card_name[0])[22:-2])

        self.create_submit = tk.Button(self.frameL6, text='Modify', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2,
                                       command=lambda: self.update_payment(id_value, self.create_input1.get(),
                                                                           self.create_input2.get(),
                                                                           self.create_input3.get(),
                                                                           self.create_input4.get()))
        self.create_submit.pack(side=tk.LEFT)
        '''
        self.create_submit = tk.Button(self.frameL6, text='Delete', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="red",
                                       width=12, height=2, command=lambda: self.create_account())
        self.create_submit.pack(side=tk.LEFT)
        '''

        pass

    def my_payment(self):
        '''
        when button clicked
        '''
        number = 1
        if number in range(0, 121):

            self.left_frame.pack_forget()

            self.left_frame = Frame(self.root, background="black",
                                    borderwidth=5, relief="ridge",
                                    width=1000)
            self.left_frame.pack(side="left",
                                 fill="both",
                                 expand="yes",
                                 )

            self.frameL1 = tk.Frame(self.left_frame)
            self.frameL1.pack()
            self.frameL2 = tk.Frame(self.left_frame)
            self.frameL2.pack()
            self.frameL3 = tk.Frame(self.left_frame)
            self.frameL3.pack()
            self.frameL4 = tk.Frame(self.left_frame)
            self.frameL4.pack()
            self.frameL5 = tk.Frame(self.left_frame)
            self.frameL5.pack()
            self.frameL6 = tk.Frame(self.left_frame)
            self.frameL6.pack()
            self.frameL7 = tk.Frame(self.left_frame)
            self.frameL7.pack()
            self.frameL8 = tk.Frame(self.left_frame)
            self.frameL8.pack()
            self.frameL9 = tk.Frame(self.left_frame)
            self.frameL9.pack()
            self.frameL10 = tk.Frame(self.left_frame)
            self.frameL10.pack()
            self.frameL11 = tk.Frame(self.left_frame)
            self.frameL11.pack()

            tk.Label(self.frameL1, bg='black', text=('Saved Credit Card'),
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

            self.btn_pd = [[0 for x in range(11)] for y in range(1)]
            for i in range(0, 1):
                self.btn_pd[0][i] = tk.Button(self.frameL3,
                                              text="visa ***2345",
                                              font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150, height=4, command=lambda: self.sub_payment())
                self.btn_pd[0][i].pack(side=tk.LEFT)

            for i in range(1, 2):
                self.btn_pd[0][i] = tk.Button(self.frameL4, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(2, 3):
                self.btn_pd[0][i] = tk.Button(self.frameL5, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(3, 4):
                self.btn_pd[0][i] = tk.Button(self.frameL6, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(4, 5):
                self.btn_pd[0][i] = tk.Button(self.frameL7, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(5, 6):
                self.btn_pd[0][i] = tk.Button(self.frameL8, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(6, 7):
                self.btn_pd[0][i] = tk.Button(self.frameL9, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(7, 8):
                self.btn_pd[0][i] = tk.Button(self.frameL10, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(9, 10):
                self.btn_pd[0][i] = tk.Button(self.frameL11, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)

            self.btnTR1.config(text='Add', font=("Helvetica", 20, "bold "), bg="forest green",
                               command=lambda: self.add_payment())
            self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

            self.cur.close()
            self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
            self.conn = pymysql.connect(user='root',
                                        password='',
                                        db='ubereat',
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.db.cursor()

            card_no = []
            payment_id = []
            cur = self.conn.cursor()
            cur.execute(
                "select credit_card_number from member_payment where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                card_no.append(row)
            # print(str(card_no[0])[36:-2])


            cur = self.conn.cursor()
            cur.execute(
                "select payment_id from member_payment where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                payment_id.append(row)
            # print(str(payment_id[0])[15:-1])

            '''
            x = 0
            while x < 9 and x < len(card_no):
                self.btn_pd[0][x].config(text="Credit Card: "+str(card_no[x])[36:-2],
                                         command=lambda: self.add_address(str(payment_id[x])[15:-1]))
                # print(str(payment_id[x])[14:-1])
                x += 1
            '''
            t_id_list = []
            for i in range(0, len(card_no)):

                t_id = str(payment_id[i])
                t_id_list.append(t_id[15:-1])
                if i == 0:
                    self.btn_pd[0][i].config(text="Default: " + str(card_no[i])[36:-2],
                                             command=lambda i=i: self.sub_payment(str(t_id_list[i])))
                else:
                    self.btn_pd[0][i].config(text=str(card_no[i])[36:-2],
                                             command=lambda i=i: self.sub_payment(str(t_id_list[i])))

            self.btnBack.config(command=lambda: self.last_page("table_sub"))
            self.btnHome.config(command=lambda: self.home_page("table_sub"))

    def choose_payment(self, id_value):

        New_payment = []
        # print("test"+id_value)
        # print("test2"+str(self.user_payment[0]))

        cur = self.conn.cursor()
        cur.execute(
            "select payment_id from member_payment where payment_id = '" + str(id_value) + "' ")
        for row in cur.fetchall():
            New_payment.append(row)
            # print(str(address_list[0])[12:-2])
        self.user_payment[0] = New_payment[0]
        # print("test3"+str(self.user_payment[0]))

        self.bag('1')

        pass

    def bag_payment(self):
        '''
        when button clicked
        '''
        number = 1
        if number in range(0, 121):

            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()

            self.left_frame = Frame(self.root, background="black",
                                    borderwidth=5, relief="ridge",
                                    width=1000)
            self.left_frame.pack(side="left",
                                 fill="both",
                                 expand="yes",
                                 )

            self.frameL1 = tk.Frame(self.left_frame)
            self.frameL1.pack()
            self.frameL2 = tk.Frame(self.left_frame)
            self.frameL2.pack()
            self.frameL3 = tk.Frame(self.left_frame)
            self.frameL3.pack()
            self.frameL4 = tk.Frame(self.left_frame)
            self.frameL4.pack()
            self.frameL5 = tk.Frame(self.left_frame)
            self.frameL5.pack()
            self.frameL6 = tk.Frame(self.left_frame)
            self.frameL6.pack()
            self.frameL7 = tk.Frame(self.left_frame)
            self.frameL7.pack()
            self.frameL8 = tk.Frame(self.left_frame)
            self.frameL8.pack()
            self.frameL9 = tk.Frame(self.left_frame)
            self.frameL9.pack()
            self.frameL10 = tk.Frame(self.left_frame)
            self.frameL10.pack()
            self.frameL11 = tk.Frame(self.left_frame)
            self.frameL11.pack()

            tk.Label(self.frameL1, bg='black', text=('Saved Address'),
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

            self.btn_pd = [[0 for x in range(11)] for y in range(1)]
            for i in range(0, 1):
                self.btn_pd[0][i] = tk.Button(self.frameL3,
                                              text="visa ***2345",
                                              font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150, height=4, command=lambda: self.sub_payment())
                self.btn_pd[0][i].pack(side=tk.LEFT)

            for i in range(1, 2):
                self.btn_pd[0][i] = tk.Button(self.frameL4, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(2, 3):
                self.btn_pd[0][i] = tk.Button(self.frameL5, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(3, 4):
                self.btn_pd[0][i] = tk.Button(self.frameL6, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(4, 5):
                self.btn_pd[0][i] = tk.Button(self.frameL7, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(5, 6):
                self.btn_pd[0][i] = tk.Button(self.frameL8, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(6, 7):
                self.btn_pd[0][i] = tk.Button(self.frameL9, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(7, 8):
                self.btn_pd[0][i] = tk.Button(self.frameL10, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(9, 10):
                self.btn_pd[0][i] = tk.Button(self.frameL11, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)

            self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20",
                               command='')
            self.btnTR2.config(text='Cash', font=("Helvetica", 20, "bold "), bg="grey20",
                               command=lambda: self.choose_payment("0"))
            self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

            self.editAreaTable.config(state="disabled")

            card_no = []
            payment_id = []
            cur = self.conn.cursor()
            cur.execute(
                "select credit_card_number from member_payment where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                card_no.append(row)
            # print(str(card_no[0])[36:-2])


            cur = self.conn.cursor()
            cur.execute(
                "select payment_id from member_payment where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                payment_id.append(row)
            # print(str(payment_id[0])[15:-1])

            '''
            x = 0
            while x < 9 and x < len(card_no):
                self.btn_pd[0][x].config(text="Credit Card: "+str(card_no[x])[36:-2],
                                         command=lambda: self.add_address(str(payment_id[x])[15:-1]))
                # print(str(payment_id[x])[14:-1])
                x += 1
            '''
            t_id_list = []
            for i in range(0, len(card_no)):

                t_id = str(payment_id[i])
                t_id_list.append(t_id[15:-1])
                if i == 0:
                    self.btn_pd[0][i].config(text="Default: " + str(card_no[i])[36:-2],
                                             command=lambda i=i: self.choose_payment(str(t_id_list[i])))
                else:
                    self.btn_pd[0][i].config(text=str(card_no[i])[36:-2],
                                             command=lambda i=i: self.choose_payment(str(t_id_list[i])))

            # self.btnBack.config(command=lambda: self.last_page("table_sub"))
            self.btnHome.config(command=lambda: self.home_page("table_sub"))

    def my_address(self):
        '''
        when button clicked
        '''
        number = 1
        if number in range(0, 121):

            self.left_frame.pack_forget()

            self.left_frame = Frame(self.root, background="black",
                                    borderwidth=5, relief="ridge",
                                    width=1000)
            self.left_frame.pack(side="left",
                                 fill="both",
                                 expand="yes",
                                 )

            self.frameL1 = tk.Frame(self.left_frame)
            self.frameL1.pack()
            self.frameL2 = tk.Frame(self.left_frame)
            self.frameL2.pack()
            self.frameL3 = tk.Frame(self.left_frame)
            self.frameL3.pack()
            self.frameL4 = tk.Frame(self.left_frame)
            self.frameL4.pack()
            self.frameL5 = tk.Frame(self.left_frame)
            self.frameL5.pack()
            self.frameL6 = tk.Frame(self.left_frame)
            self.frameL6.pack()
            self.frameL7 = tk.Frame(self.left_frame)
            self.frameL7.pack()
            self.frameL8 = tk.Frame(self.left_frame)
            self.frameL8.pack()
            self.frameL9 = tk.Frame(self.left_frame)
            self.frameL9.pack()
            self.frameL10 = tk.Frame(self.left_frame)
            self.frameL10.pack()
            self.frameL11 = tk.Frame(self.left_frame)
            self.frameL11.pack()

            tk.Label(self.frameL1, bg='black', text=('Saved Address'),
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

            self.btn_pd = [[0 for x in range(11)] for y in range(1)]
            for i in range(0, 1):
                self.btn_pd[0][i] = tk.Button(self.frameL3,
                                              text="Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK",
                                              font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150, height=4, command=lambda: self.sub_address())
                self.btn_pd[0][i].pack(side=tk.LEFT)

            for i in range(1, 2):
                self.btn_pd[0][i] = tk.Button(self.frameL4, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(2, 3):
                self.btn_pd[0][i] = tk.Button(self.frameL5, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(3, 4):
                self.btn_pd[0][i] = tk.Button(self.frameL6, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(4, 5):
                self.btn_pd[0][i] = tk.Button(self.frameL7, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(5, 6):
                self.btn_pd[0][i] = tk.Button(self.frameL8, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(6, 7):
                self.btn_pd[0][i] = tk.Button(self.frameL9, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(7, 8):
                self.btn_pd[0][i] = tk.Button(self.frameL10, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)
            for i in range(9, 10):
                self.btn_pd[0][i] = tk.Button(self.frameL11, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                              bg="grey20", width=150,
                                              height=4, command='')
                self.btn_pd[0][i].pack(side=tk.LEFT)

            self.btnTR1.config(text='Add', font=("Helvetica", 20, "bold "), bg="forest green",
                               command=lambda: self.add_address())
            self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20", command='')
            self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20", command='')
            self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20", command='')
            self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20", command='')
            self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20", command='')
            self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20", command='')
            self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20", command='')

            self.cur.close()
            self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
            self.conn = pymysql.connect(user='root',
                                        password='',
                                        db='ubereat',
                                        cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.db.cursor()

            address_list = []
            address_id_list = []
            cur = self.conn.cursor()
            cur.execute(
                "select Address from member_address where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                address_list.append(row)
            # print(str(address_list[0])[12:-2])


            cur = self.conn.cursor()
            cur.execute(
                "select address_id from member_address where member_id = '" + str(self.id) + "' ")
            for row in cur.fetchall():
                address_id_list.append(row)
            # print(str(address_id_list[0])[15:-1])
            print(len(address_list))
            print(len(address_id_list))

            t_id_list = []
            for i in range(0, len(address_list)):

                t_id = str(address_id_list[i])
                t_id_list.append(t_id[15:-1])
                if i == 0:
                    self.btn_pd[0][i].config(text="Default: " + str(address_list[i])[13:-2],
                                             command=lambda i=i: self.sub_address(str(t_id_list[i])))
                else:
                    self.btn_pd[0][i].config(text=str(address_list[i])[13:-2],
                                             command=lambda i=i: self.sub_address(str(t_id_list[i])))

            self.btnBack.config(command=lambda: self.last_page("table_sub"))
            self.btnHome.config(command=lambda: self.home_page("table_sub"))

    def my_order(self):

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("courier new", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")
        '''
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O001\n\nOrder time: 2/2/2020 11:11:11\n\nSuper Supreme x1 $168\nDelivery fee: $20\nTotal $188\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time: 30 min\n\n\n")
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O124\n\nOrder time: 1/2/2020 11:11:11\n\nSupreme x2 $296\nDelivery fee: $20\nTotal $316\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time:1/2/2020 11:33:11")
        '''

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20",
                           command='')
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.last_page("table_sub"))
        self.btnHome.config(command=lambda: self.home_page("table_sub"))

        order_id = []
        order_status = []
        order_date_time = []
        order_payment = []
        order_address = []
        order_shop = []

        cur = self.conn.cursor()
        cur.execute("select `ORDER_ID` from `order` where `MEMBER_ID` = '" + str(self.id) + "'")

        for row in cur.fetchall():
            order_id.append(row)
        # print(str(order_id[0])[12:-1])

        cur = self.conn.cursor()
        cur.execute("select `ORDER_STATUS` from `order` where `MEMBER_ID` = '" + str(self.id) + "'")

        for row in cur.fetchall():
            order_status.append(row)
        # print(str(order_status[0])[17:-2])

        cur = self.conn.cursor()
        cur.execute("select `ORDER_DATE_TIME` from `order` where `MEMBER_ID` = '" + str(self.id) + "'")

        for row in cur.fetchall():
            order_date_time.append(row)
        # print(str(order_date_time[0])[20:-2])

        cur = self.conn.cursor()
        cur.execute("select `address_id` from `order` where `MEMBER_ID` = '" + str(self.id) + "'")

        for row in cur.fetchall():
            order_address.append(row)
        # print(str(order_address[0])[14:-1])

        cur = self.conn.cursor()
        cur.execute("select `payment_id` from `order` where `MEMBER_ID` = '" + str(self.id) + "'")

        for row in cur.fetchall():
            order_payment.append(row)
        # print(str(order_payment[0])[14:-1])

        cur = self.conn.cursor()
        cur.execute("select `payment_id` from `order` where `MEMBER_ID` = '" + str(self.id) + "'")

        for row in cur.fetchall():
            order_payment.append(row)
        # print(str(order_payment[0])[14:-1])

        cur = self.conn.cursor()
        cur.execute("select `shop_id` from `order` where `MEMBER_ID` = '" + str(self.id) + "'")

        for row in cur.fetchall():
            order_shop.append(row)
            #print(str(order_shop[0])[13:-2])



        x = 0
        while x < len(order_id):
            self.editAreaTable.insert(tk.INSERT, 'Order id: ' + str(order_id[x])[12:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Order status: ' + str(order_status[x])[18:-2] + '\n')

            # print('test')
            # print(str(order_address[0])[14:-1])

            address_name = []
            cur = self.conn.cursor()
            cur.execute(
                "select `Address` from `member_address` where `address_id` = '" + str(order_address[x])[14:-1] + "'")
            for row in cur.fetchall():
                address_name.append(row)
            # print(str(address_name[0]))

            self.editAreaTable.insert(tk.INSERT, 'Order address: ' + str(address_name[0])[11:-2] + '\n')

            total_price = 0
            delivery_fee = []
            cur = self.conn.cursor()
            cur.execute(
                "select `delivery_fee` from `order` where `order_id` = '" + str(order_id[x])[12:-1] + "'")
            for row in cur.fetchall():
                delivery_fee.append(row)
            # print(str(address_name[0]))

            self.editAreaTable.insert(tk.INSERT, 'Delivery fee: $' + str(delivery_fee[0])[16:-1] + '\n')
            total_price += float(str(delivery_fee[0])[16:-1])

            shop = []
            cur = self.conn.cursor()
            cur.execute(
                "select `shop_name` from `shop` where `shop_id` = '" + str(order_shop[x])[13:-2] + "'")
            for row in cur.fetchall():
                shop.append(row)
            # print(str(address_name[0]))

            self.editAreaTable.insert(tk.INSERT, 'Shop: ' + str(shop[0])[13:-1] + '\n')


            payment_name = []
            cur = self.conn.cursor()
            cur.execute(
                "select `Credit_card_number` from `member_payment` where `payment_id` = '" + str(order_payment[x])[
                                                                                             14:-1] + "'")
            for row in cur.fetchall():
                payment_name.append(row)
            # print(str(payment_name[0]))

            self.editAreaTable.insert(tk.INSERT, 'Order address: ' + str(payment_name[0])[36:-2] + '\n')

            # print("test2"+str(order_id[x])[12:-1])
            order_product_id = []
            cur = self.conn.cursor()
            cur.execute(
                "select `order_product_id` from `order_product` where `order_id` = '" + str(order_id[x])[12:-1] + "'")
            for row in cur.fetchall():
                order_product_id.append(row)
            print(str(order_product_id[0])[20:-1])

            self.editAreaTable.insert(tk.INSERT, 'Order product (No./Name/Qty/Price): ' + '\n')



            y = 0
            while y < len(order_product_id):

                product_id = []
                cur = self.conn.cursor()
                cur.execute(
                    "select `product_id` from `order_product` where `order_product_id` = '" + str(order_product_id[y])[
                                                                                              20:-1] + "'")
                for row in cur.fetchall():
                    product_id.append(row)
                # print(str(product_id[0])[16:-2])

                product_name = []
                cur = self.conn.cursor()
                cur.execute(
                    "select `product_name` from `product` where `product_id` = '" + str(product_id[0])[16:-2] + "'")
                for row in cur.fetchall():
                    product_name.append(row)
                # print(str(product_name[0])[18:-2])


                product_quantity = []
                cur = self.conn.cursor()
                cur.execute(
                    "select `quantity` from `order_product` where `order_product_id` = '" + str(order_product_id[y])[
                                                                                            20:-1] + "'")
                for row in cur.fetchall():
                    product_quantity.append(row)
                # print(str(product_quantity[0])[12:-1])

                product_price = []
                cur = self.conn.cursor()
                cur.execute(
                    "select `price` from `order_product` where `order_product_id` = '" + str(order_product_id[y])[
                                                                                         20:-1] + "'")
                for row in cur.fetchall():
                    product_price.append(row)
                # print(str(product_price[0])[9:-1])
                total_price += float(str(product_price[0])[9:-1])

                product_link = []
                cur = self.conn.cursor()
                cur.execute(
                    "select `LINK_PRODUCT` from `order_product` where `order_product_id` = '" + str(
                        order_product_id[y])[20:-1] + "'")
                for row in cur.fetchall():
                    product_link.append(row)
                print(str(product_link[0])[18:-2])

                if str(product_link[0])[18:-2] == '/':
                    self.editAreaTable.insert(tk.INSERT, str(y) + ' ' + str(product_name[0])[18:-2] + "   " + str(
                        product_quantity[0])[12:-1] + "   $" + str(product_price[0])[9:-1] + '\n')
                else:
                    self.editAreaTable.insert(tk.INSERT,
                                              '      -' + str(product_name[0])[18:-2] + "          " + "   $" + str(
                                                  product_price[0])[9:-1] + '\n')

                y += 1
            self.editAreaTable.insert(tk.INSERT, 'Total: $' + str(total_price) + '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1

        pass

    def logout(self):

        login_loop_302.main(self.root)

    def main_page_table(self):
        table_name_list = []
        table_id_list = []

        cur = self.conn.cursor()
        cur.execute("select SHOP_NAME from shop  order by SHOP_ID")
        for row in cur.fetchall():
            table_name_list.append(row)

        cur = self.conn.cursor()
        cur.execute("select SHOP_ID from shop  order by SHOP_ID")
        for row in cur.fetchall():
            table_id_list.append(row)


        #print(str(table_name_list[0])[15:-2])
        #print(str(table_id_list[0])[13:-2])
        length_data = len(table_name_list)

        t_name_list = []
        t_id_list = []
        for i in range(0, length_data):
            t_name = str(table_name_list[i])[15:-2]
            t_id = str(table_id_list[i])[13:-2]

            t_name_list.append(t_name)
            t_id_list.append(t_id)
            self.btn_tb[0][i].config(text=(t_name),command=lambda i=i:self.add_order_template(t_id_list[i]))

    def test_reply(self):
        get = requests.get('http://127.0.0.1:3500/getdata')  # GET request
        self.reply = get.json()
        print(self.reply)

        print(self.reply["ORDER_ID"])
        print(self.reply["STATUS"])

        cur = self.conn.cursor()
        cur.execute(
            "update `order` set `ORDER_STATUS` = '" + str(self.reply["STATUS"]) + "' where`ORDER_id` ='" + str(
                self.reply["ORDER_ID"]) + "'")
        cur.execute("commit")

        self.cur.close()
        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='ubereat',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()

    def main_page(self, section, order_id, table_id):

        self.cur.close()
        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='ubereat',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()

        # print(self.id)
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)

        self.frameL1.pack()

        self.frameL2 = tk.Frame(self.left_frame)

        self.frameL2.pack()

        self.frameL3 = tk.Frame(self.left_frame)

        self.frameL3.pack()

        self.frameL4 = tk.Frame(self.left_frame)

        self.frameL4.pack()

        self.frameL5 = tk.Frame(self.left_frame)

        self.frameL5.pack()

        self.frameL6 = tk.Frame(self.left_frame)

        self.frameL6.pack()

        self.frameL7 = tk.Frame(self.left_frame)

        self.frameL7.pack()

        self.frameL8 = tk.Frame(self.left_frame)

        self.frameL8.pack()

        self.frameL9 = tk.Frame(self.left_frame)

        self.frameL9.pack()

        self.frameL10 = tk.Frame(self.left_frame)

        self.frameL10.pack()

        self.frameTablelabel = tk.Frame(self.left_frame)
        self.frameTablelabel.pack()

        if section == 1:
            tk.Label(self.frameL1, bg='black', text='Restaurant list',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        elif section == 2:
            tk.Label(self.frameL1, bg='black', text='Switch table',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.btn_tb = [[0 for x in range(100)] for y in range(1)]
        for i in range(0, 5):
            self.btn_tb[0][i] = tk.Button(self.frameL3, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)

        for i in range(6, 11):
            self.btn_tb[0][i] = tk.Button(self.frameL4, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(11, 16):
            self.btn_tb[0][i] = tk.Button(self.frameL5, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(16, 21):
            self.btn_tb[0][i] = tk.Button(self.frameL6, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(21, 26):
            self.btn_tb[0][i] = tk.Button(self.frameL7, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(26, 31):
            self.btn_tb[0][i] = tk.Button(self.frameL8, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)

        self.btn_tb[0][0].config(text="pizzaHut 30min", command=lambda: self.add_order_template())

        self.btnTR1.config(text='My Order', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_order())

        self.btnTR2.config(text='My Account', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_account())

        self.btnTR3.config(text='My Address', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_address())

        self.btnTR4.config(text='My Payment', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_payment())

        self.btnTR5.config(text='', background="grey20", font=("Helvetica", 20, "bold "), command='')

        self.btnTR6.config(text='', background="grey20", command='')

        self.btnTR7.config(text='', background="grey20", command='')

        self.btnTR8.config(text='LogOut', bg='red4', command=lambda: self.logout())

        self.btnBack.config(command=lambda: self.last_page("table_sub"))
        self.btnHome.config(command=lambda: self.home_page("table_sub"))

        self.btnbag.config(command=lambda: self.bag("1"))
        self.btnrefresh.config(command=lambda: self.test_reply())

        if section == 1:
            pass
            self.main_page_table()

        elif section == 2:
            self.switch_table(order_id, table_id)

    def del_page_editarea(self, choice):
        if choice == "del":
            self.del_list = self.del_list[:-1]
            self.editAreaTable3.delete("1.0", END)
            self.editAreaTable3.insert(tk.INSERT, self.del_list)

        elif choice == "Clear":
            pass
        else:
            self.del_list += choice
            self.editAreaTable3.insert(tk.INSERT, choice)
            self.editAreaTable3.see("end")

    def delete_from_order(self, order_id):

        self.add_no_list = []
        for e in range(0, len(self.add_pd_list)):
            self.add_no_list.append(e)

        if self.del_pd_id == '':
            found = False
            for e in self.add_no_list:
                if str(self.editAreaTable3.get("1.0", END)[0:-1]) == str(e) and self.add_link_list[e] == '/':
                    found = True
                else:
                    pass

            if not found:
                self.editAreaTable2.insert(tk.INSERT, self.del_pd_id)
                self.editAreaTable2.insert(tk.INSERT, '\nNot Found. Try Again:')
                self.editAreaTable3.delete("1.0", END)
                self.editAreaTable3.see("end")
                self.del_list = ''
            else:
                self.del_pd_id = self.editAreaTable3.get("1.0", END)
                self.editAreaTable2.insert(tk.INSERT, self.del_pd_id)
                self.editAreaTable3.delete("1.0", END)
                self.editAreaTable3.see("end")
                self.del_list = ''
        else:
            self.del_pd_qty = self.editAreaTable3.get("1.0", END)
            self.editAreaTable2.insert(tk.INSERT, self.del_pd_qty)
            self.editAreaTable3.delete("1.0", END)
            self.editAreaTable3.see("end")
            self.del_list = ''

        if self.del_pd_id != '' and self.del_pd_qty == '':
            self.editAreaTable2.insert(tk.INSERT, 'Quantity:')

        if self.del_pd_id != '' and self.del_pd_qty != '':

            print(1, self.add_no_list, self.add_link_list, self.add_id_list, self.add_pd_list, self.add_qty_list,
                  self.add_price_list)

            for e in range(0, len(self.add_no_list)):
                if str(self.del_pd_id[0:-1]) == str(self.add_no_list[e]) or str(self.del_pd_id[0:-1]) == str(
                        self.add_link_list[e]):
                    self.add_qty_list[e] = str(int(self.del_pd_qty[0:-1]))

            for e in range(0, len(self.add_qty_list)):
                if int(self.add_qty_list[e]) <= 0:
                    self.add_qty_list[e] = '-'
                    self.add_no_list[e] = '-'
                    self.add_link_list[e] = '-'
                    self.add_id_list[e] = '-'
                    self.add_pd_list[e] = '-'
                    self.add_price_list[e] = '-'

            print(2, self.add_no_list, self.add_link_list, self.add_id_list, self.add_pd_list, self.add_qty_list,
                  self.add_price_list)

            x = self.add_qty_list.count('-')
            for e in range(0, x):
                self.add_qty_list.remove("-")
                self.add_no_list.remove("-")
                self.add_link_list.remove("-")
                self.add_id_list.remove("-")
                self.add_pd_list.remove("-")
                self.add_price_list.remove("-")

            print(3, self.add_no_list, self.add_link_list, self.add_id_list, self.add_pd_list, self.add_qty_list,
                  self.add_price_list)

            self.editAreaTable2.insert(tk.INSERT, 'Done!')
            self.editAreaTable2.insert(tk.INSERT, '\n')
            self.editAreaTable2.insert(tk.INSERT, 'Other id to modiffy:')
            self.del_pd_id = ''
            self.del_pd_qty = ''

            self.add_no_list = []

            self.editAreaTable.config(state="normal")
            self.editAreaTable.delete("1.0", END)

            self.editAreaTable.insert(tk.INSERT, "No./Name/Qty/$\n")
            length = len(self.add_pd_list)
            i = 0
            while i < length:
                self.add_no_list.append(i)
                if self.add_link_list[i] == "/":
                    l = i
                    self.editAreaTable.insert(tk.INSERT, str(i) + ' ')
                    # self.editAreaTable.insert(tk.INSERT, self.add_id_list[i])
                    # self.editAreaTable.insert(tk.INSERT, ' ')
                    self.editAreaTable.insert(tk.INSERT, self.add_pd_list[i])
                    self.editAreaTable.insert(tk.INSERT, ' ')
                    self.editAreaTable.insert(tk.INSERT, self.add_qty_list[i])
                    self.editAreaTable.insert(tk.INSERT, ' $')
                    self.editAreaTable.insert(tk.INSERT, self.add_price_list[i])
                    self.editAreaTable.insert(tk.INSERT, '\n')

                else:
                    self.add_link_list[i] = l
                    self.editAreaTable.insert(tk.INSERT, '     ')
                    # self.editAreaTable.insert(tk.INSERT, self.add_id_list[i])
                    self.editAreaTable.insert(tk.INSERT, '-')
                    self.editAreaTable.insert(tk.INSERT, self.add_pd_list[i])
                    # self.editAreaTable.insert(tk.INSERT, ' ')
                    # self.editAreaTable.insert(tk.INSERT, self.add_qty_list[i])
                    self.editAreaTable.insert(tk.INSERT, ' $')
                    self.editAreaTable.insert(tk.INSERT, self.add_price_list[i])
                    self.editAreaTable.insert(tk.INSERT, '\n')
                i += 1

            credit_card = []
            cur = self.conn.cursor()
            cur.execute(
                "select Credit_card_number from member_payment where payment_id = '" + str(self.user_payment[0])[
                                                                                       14:-1] + "'")
            for row in cur.fetchall():
                credit_card.append(row)

            address = []
            cur = self.conn.cursor()
            cur.execute(
                "select address from member_address where address_id = '" + str(self.user_address[0])[14:-1] + "'")
            for row in cur.fetchall():
                address.append(row)

            # str(self.user_payment[0])[14:-1]
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, 'Credit Card:' + str(credit_card[0])[36:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Address:' + str(address[0])[13:-2] + '\n')

            self.editAreaTable.config(state="disabled")

            x = 0
            bag_counter = 0
            while x < len(self.add_link_list):
                if self.add_link_list[x] == "/":
                    bag_counter += 1
                x += 1

            self.btnbag.config(text="Bag: " + str(bag_counter))

            pass

    def __init__(self, root, id):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title("UberEat")

        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='ubereat',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()

        self.frameRt = tk.Frame(self.root, background="black")
        self.frameRt.pack(fill="both")

        self.id = str(id)
        print(self.id)
        self.user_name = []
        '''
        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.cursor = self.db.cursor()

        self.connection = pymysql.connect(user='root',
                                          password='',
                                          db='ubereat',
                                          cursorclass=pymysql.cursors.DictCursor)

        '''
        cur = self.conn.cursor()
        cur.execute("select CUSTOMER_SURNAME from member_data where MEMBER_ID = '" + str(self.id) + "'")
        for row in cur.fetchall():
            self.user_name.append(row)

        # print(str(self.user_name[0])[22:-2])
        self.date = datetime.datetime.now()
        self.date_label = tk.Label(self.frameRt, text='Welcome ' + str(self.user_name[0])[22:-2] + "      " + str(
            self.date.strftime('%Y/%m/%d') + '      '), font=("courier new", 20, "bold"), bg='black', fg="white")
        self.date_label.pack(side=tk.LEFT)

        self.clock1 = clock.Clock(self.frameRt)
        self.clock1.pack(side=tk.LEFT)
        self.clock1.configure(font=("courier new", 20, "bold"), bg='black', fg="white")

        self.btnbag = tk.Button(self.frameRt, text='Bag: 0', font=("Helvetica", 10, "bold "), width=20,
                                height=1, bg="black", fg="white", command=lambda: self.bag("1"))
        self.btnbag.pack(side=tk.LEFT)

        self.btnrefresh = tk.Button(self.frameRt, text='REFRESH', font=("Helvetica", 10, "bold "), width=20,
                                    height=1, bg="black", fg="white", command=lambda: self.bag("1"))
        self.btnrefresh.pack(side=tk.LEFT)

        self.bottom_nvaigation = Frame(self.root, background="black", borderwidth=5,
                                       relief="ridge", height=35)
        self.bottom_nvaigation.pack(side="bottom", fill="both",
                                    )

        self.right_frame = Frame(self.root, background="black",
                                 borderwidth=5, relief="ridge")
        self.right_frame.pack(side="right", fill="both",
                              )

        self.frame_bottom_nvaigation = tk.Frame(self.bottom_nvaigation)
        self.frame_bottom_nvaigation.pack()

        self.btnBack = tk.Button(self.frame_bottom_nvaigation, text='< BACK', font=("Helvetica", 10, "bold "), width=88,
                                 height=1, bg="black", fg="white")
        self.btnBack.pack(side=tk.LEFT)

        self.btnHome = tk.Button(self.frame_bottom_nvaigation, text='O HOME', font=("Helvetica", 10, "bold "), width=88,
                                 height=1, bg="black", fg="white", command=lambda: self.home_page())
        self.btnHome.pack(side=tk.LEFT)

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

        self.btnTR1 = tk.Button(self.frameR1, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR1.pack(side=tk.LEFT)
        self.btnTR2 = tk.Button(self.frameR2, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR2.pack(side=tk.LEFT)
        self.btnTR3 = tk.Button(self.frameR3, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR3.pack(side=tk.LEFT)
        self.btnTR4 = tk.Button(self.frameR4, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR4.pack(side=tk.LEFT)
        self.btnTR5 = tk.Button(self.frameR5, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR5.pack(side=tk.LEFT)
        self.btnTR6 = tk.Button(self.frameR6, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR6.pack(side=tk.LEFT)
        self.btnTR7 = tk.Button(self.frameR7, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR7.pack(side=tk.LEFT)
        self.btnTR8 = tk.Button(self.frameR8, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR8.pack(side=tk.LEFT)

        self.table_id_nm = ""
        self.add_list = ""
        self.del_list = ''
        self.address_list = ""
        self.delivery_list = []

        self.add_no_list = []
        self.add_id_list = []
        self.add_pd_list = []
        self.add_qty_list = []
        self.add_price_list = []
        self.add_link_list = []

        self.add_link_price_list = []
        self.set_option_count = 0
        self.creator_option_count = 0
        self.add_pd_location = ''
        self.table_people_no = ''
        self.member_id = ''
        self.update_order_id = []

        self.shop_id_choose=[]

        self.user_payment = []
        cur = self.conn.cursor()
        try:
            cur.execute("select payment_id from member_payment where MEMBER_ID = '" + str(self.id) + "'")
            # cur.execute("select payment_id from member_payment where MEMBER_ID = 'V0002'" )
            for row in cur.fetchall():
                self.user_payment.append(row)
                # print(self.user_payment[0])
        except:
            self.user_payment = []
            pass

        # print(str(self.user_payment[0])[14:-1])

        self.user_address = []
        cur = self.conn.cursor()
        try:
            cur.execute("select address_id from member_address where MEMBER_ID = '" + str(self.id) + "'")
            # cur.execute("select payment_id from member_payment where MEMBER_ID = 'V0002'" )
            for row in cur.fetchall():
                self.user_address.append(row)
                # print(self.user_payment[0])
        except:
            self.user_address = []
            pass

        # print(self.user_address)


        self.main_page(1, [], '')


def main(id, window):
    root = tk.Tk()
    Gui(root, id)
    window.destroy()
    root.mainloop()


if __name__ == '__main__':
    sys.exit(main())

