import sys


from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import Button, Frame, Tk

from tkinter import END
import cx_Oracle
import pymysql
import Get_JSON_302

class Gui:
    def login_page_editarea(self, choice):
        if choice == "del" and self.login_list != "":

            self.login_list = self.login_list[:-1]
            self.editAreaAddress2.delete("1.0", END)
            for i in range(len(self.login_list)):
                self.editAreaAddress2.insert(tk.INSERT, '*')

        else:
            self.login_list += choice
            self.editAreaAddress2.insert(tk.INSERT, '*')

    def wrong_(self):
        self.input_list = []
        self.editAreaAddress.delete("1.0", END)
        self.editAreaAddress2.delete("1.0", END)
        self.editAreaAddress.insert(tk.INSERT, 'Wrong username/ password')
        self.editAreaAddress.insert(tk.INSERT, '\nInput username:')
        self.login_list = ''
        self.btn_ap_enter.config(command=lambda: self.username_receive())

    def password_receive(self):
        self.input_list.append(self.login_list)
        self.login_list = ''
        self.editAreaAddress.delete("1.0", END)
        self.editAreaAddress2.delete("1.0", END)

        pw=[]
        cur = self.conn.cursor()
        cur.execute("select password from shop_login where username = '"+str(self.input_list[0])+"'")
        for row in cur.fetchall():
            pw.append(row)
            print(pw)
            print(str(pw[0])[14:-2])
        try:
            if str(pw[0])[14:-2] == str(self.input_list[1]):
                shop_id = []
                cur = self.conn.cursor()
                cur.execute("select Shop_id from shop_login where username = '" + str(self.input_list[0]) + "'")
                for row in cur.fetchall():
                    shop_id.append(row)
                    print(shop_id)
                    print("test"+str(shop_id[0])[13:-2])
                Get_JSON_302.main((str(shop_id[0])[13:-2]),self.root)
            else:
                self.wrong_()
        except IndexError as error:

            self.wrong_()

    def username_receive(self):
        self.input_list.append(self.login_list)
        self.login_list=''
        self.editAreaAddress.delete("1.0", END)
        self.editAreaAddress.insert(tk.INSERT, 'Input password:')
        self.editAreaAddress2.delete("1.0", END)
        self.btn_ap_enter.config(command=lambda :self.password_receive())

    def login_template(self):
        self.str_btn.destroy()
        #self.str_btn2.destroy()
        self.name_label1.destroy()
        self.name_label2.destroy()
        self.name_label3.destroy()
        self.name_label4.destroy()
        self.name_label5.destroy()
        self.name_label6.destroy()
        self.editAreaAddress = tkst.ScrolledText(self.frameL1, height=7, background="white", fg="black",
                                               font=("courier new", 15, "bold"))
        self.editAreaAddress.pack(fill="both", expand="yes", side="left")
        self.editAreaAddress.insert(tk.INSERT, 'Input your username:')

        self.editAreaAddress2 = tkst.ScrolledText(self.frameL2, height=5, background="white", fg="black",
                                                font=("courier new", 15, "bold"))
        self.editAreaAddress2.pack(fill="both", expand="yes", side="left")

        keyboardlist=['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L',"'",'Z','X','C','V','B','N','M',',','/']

        self.btn_ap = [[0 for x in range(121)] for y in range(1)]
        for i in range(0, 10):
            self.btn_ap[0][i] = tk.Button(self.frameL3, text=keyboardlist[i], font=("Helvetica", 20, "bold "),fg= "white",bg="grey20", width=4, height=2,
                                          command= lambda i=i: self.login_page_editarea(keyboardlist[i]))
            self.btn_ap[0][i].pack(side=tk.LEFT)
        self.btn_ap_bk = tk.Button(self.frameL3, text='<[X]', font=("Helvetica", 20, "bold "),fg="white", bg="dark red", width=6,
                                      height=2,
                                      command=lambda: self.login_page_editarea("del"))
        self.btn_ap_bk.pack(side=tk.LEFT)
        for i in range(10, 20):
            self.btn_ap[0][i] = tk.Button(self.frameL4, text=keyboardlist[i], font=("Helvetica", 20, "bold "),fg= "white",bg="grey20", width=4, height=2,
                                          command=lambda i=i: self.login_page_editarea(keyboardlist[i]))
            self.btn_ap[0][i].pack(side=tk.LEFT)

        for i in range(20, 30):
            self.btn_ap[0][i] = tk.Button(self.frameL5, text=keyboardlist[i], font=("Helvetica", 20, "bold "),fg= "white",bg="grey20", width=4, height=2,
                                          command=lambda i=i: self.login_page_editarea(keyboardlist[i]))
            self.btn_ap[0][i].pack(side=tk.LEFT)

        for i in range(30, 39):
            self.btn_ap[0][i] = tk.Button(self.frameL6, text=keyboardlist[i], font=("Helvetica", 20, "bold "),fg= "white",bg="grey20", width=4, height=2,
                                          command=lambda i=i: self.login_page_editarea(keyboardlist[i]))
            self.btn_ap[0][i].pack(side=tk.LEFT)

        self.btn_ap_space= tk.Button(self.frameL7, text='Spacebar', font=("Helvetica", 20, "bold "),fg= "white",bg="grey20", width=40, height=2,
                                          command=lambda: self.login_page_editarea(' '))
        self.btn_ap_space.pack(side=tk.LEFT)

        self.btn_ap_enter = tk.Button(self.frameL7, text='ENTER', font=("Helvetica", 20, "bold "), fg="white", bg="dark orange3", width=6,
                                      height=2,
                                      command=lambda: self.username_receive())
        self.btn_ap_enter.pack(side=tk.LEFT)

    def create_receive(self):

        self.create_label2.config(text='Email')
        self.create_label3.config(text='Phone number')
        self.create_label5.config(text='Confirm password')
        self.input_list.append(self.login_list)
        self.login_list=''
        self.check_list=[]
        email=[]
        PASS=0


        phone_number=[]
        cur = self.conn.cursor()
        cur.execute(
            "select phone_number from member_data  " )
        for row in cur.fetchall():
            phone_number.append(row)
        print(str(phone_number[0]))
        print(str(phone_number[0])[17:-1])
        print(str(self.create_input3.get()))
        i=0
        while i<len(phone_number):
            if str(self.create_input3.get()) == (str(phone_number[i])[17:-1]):
                self.create_label3.config(text='Repeated phone number')
                PASS = 1
            i+=1


        cur = self.conn.cursor()
        cur.execute(
            "select email from member_data  ")
        for row in cur.fetchall():
            email.append(row)
        print(str(email[0]))
        print(str(email[0])[11:-2])
        print(str(self.create_input2.get()))

        i=0
        while i<len(email):
            print("avb")
            if str(self.create_input2.get()) == (str(email[i])[11:-2]):
                print('hello')
                self.create_label2.config(text='Repeated email')
                PASS = 1
            i+=1

        if str(self.create_input4.get()) != str(self.create_input5.get()):
            self.create_label5.config(text='Wrong confirm password')
            PASS = 1

        if PASS==0:
            cur = self.conn.cursor()
            with self.conn.cursor() as cur:

                cur.execute("INSERT INTO member_data(PHONE_NUMBER, CUSTOMER_SURNAME, EMAIL, PASSWORD) VALUES ('"+ str(self.create_input3.get()) + "','" + str(self.create_input1.get()) + "','" + str(self.create_input2.get()) + "','" + str(self.create_input3.get()) + "')")
                self.conn.commit()

                self.create_submit(command=lambda: self.create_receive())
    '''
    def create_account(self):
        self.str_btn.destroy()
        self.str_btn2.destroy()
        self.name_label1.destroy()
        self.name_label2.destroy()
        self.name_label3.destroy()
        self.name_label4.destroy()
        self.name_label5.destroy()
        self.name_label6.destroy()
        self.input_list=[]
        cur = self.conn.cursor()
        self.create_title = tk.Label(self.frameL1, text="Please input the followings", font=("Helvetica", 30), fg="white",
                                      background="black")
        self.create_title.pack(side=tk.LEFT)
        self.create_label1 = tk.Label(self.frameL2, text="User name: ", font=("Helvetica", 20), fg="white",background="black")
        self.create_label1.pack(side=tk.LEFT)
        self.create_input1 = tk.Entry(self.frameL2, text="",background="white")
        self.create_input1.pack(side=tk.LEFT)
        self.input_list.append(self.create_input1)


        self.create_label2 = tk.Label(self.frameL3, text="Email: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)
        self.create_input2 = tk.Entry(self.frameL3, text="dsdsd", background="white", fg="black")
        self.create_input2.pack(side=tk.LEFT)
        print(self.create_input2.get())
        self.input_list.append(self.create_input2)

        self.create_label3 = tk.Label(self.frameL4, text="Phone: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)
        self.create_input3 = tk.Entry(self.frameL4, text="", background="white")
        self.create_input3.pack(side=tk.LEFT)
        self.input_list.append(self.create_input3)

        self.create_label4 = tk.Label(self.frameL5, text="Password: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)
        self.create_input4 = tk.Entry(self.frameL5, text="", background="white")
        self.create_input4.pack(side=tk.LEFT)
        self.input_list.append(self.create_input4)

        self.create_label5 = tk.Label(self.frameL6, text="Confirm Password: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label5.pack(side=tk.LEFT)
        self.create_input5 = tk.Entry(self.frameL6, text="", background="white")
        self.create_input5.pack(side=tk.LEFT)
        self.input_list.append(self.create_input5)
        self.create_submit = tk.Button(self.frameL7, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.create_receive())
        self.create_submit.pack(side=tk.LEFT)
        '''

    '''
        self.create_back = tk.Button(self.frameL7, text='back', font=("Helvetica", 20, "bold "), fg="white",
                                 bg="red",
                                 width=12, height=2, command=lambda: self.__init__(root))
        self.create_back.pack(side=tk.LEFT)
        '''
    '''
        pass


    '''
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title("PIZZAHUT")

        self.left_frame = Frame(self.root, background="white",
                                borderwidth=5, relief="ridge",
                                width=600)
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

        self.name_label1= tk.Label(self.frameL1, text=" ",background="white",font=("Helvetica", 100, "bold "))
        self.name_label1.pack()


        img = PhotoImage(file='')

        self.name_label2 =""
        self.name_label2=tk.Label(self.frameL2,image=img,height = 200, width =200,background="white")
        self.name_label2.image = img
        self.name_label2.pack(side=tk.LEFT)

        self.name_label3 = tk.Label(self.frameL3, text="",background="white")
        self.name_label3.pack()
        self.name_label4 = tk.Label(self.frameL4, text="PIZZA HUT", font=("Helvetica", 50, "bold italic"), fg="black",background="white")
        self.name_label4.pack()
        self.name_label5 = tk.Label(self.frameL5, text="",background="white")
        self.name_label5.pack()
        self.name_label6 = tk.Label(self.frameL6, text="", background="white")
        self.name_label6.pack()
        self.str_btn=tk.Button(self.frameL7, text='Login', font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                      width=12, height=2,command=lambda: self.login_template())
        self.str_btn.pack(side=tk.LEFT)
        #self.str_btn2 = tk.Button(self.frameL7, text='Create Account', font=("Helvetica", 20, "bold "), fg="white",bg="dark green",width=12, height=2, command=lambda: self.create_account())
        #self.str_btn2.pack(side=tk.LEFT)
        self.login_list=''
        self.input_list=[]

        self.db = pymysql.connect('localhost', 'root', '', 'PIZZAHUT')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='PIZZAHUT',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()

def main(window):
    root = tk.Tk()
    Gui(root)
    window.destroy()
    root.mainloop()


if __name__ == '__main__':
    sys.exit(main())