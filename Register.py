from tkinter import *

from tkinter import ttk, messagebox
import mysql.connector
#from login import Login
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=db_name,
    )
    return cnx


class Register:

    def __init__(self, window):
        self.window = window
        self.window.title("Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="green")
        # big frame
        frame = Frame(self.window, bg="lightgreen")
        frame.place(x=350, y=100, width=500, height=550)

        title1 = Label(frame, text="Create an account ", font=("times new roman", 25, "bold"), bg="white").place(x=20,
                                                                                                                 y=10)
        f_name = Label(frame, text="First name", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=100)
        self.fname_txt = Entry(frame, font=("arial"), bg='lightgrey')
        self.fname_txt.place(x=20, y=130, width=200)

        l_name = Label(frame, text="Last name", font=("helvetica", 15, "bold"), bg="white").place(x=240, y=100)
        self.lname_txt = Entry(frame, font=("arial"), bg='lightgrey')
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame, font=("arial"), bg='lightgrey')
        self.email_txt.place(x=20, y=210, width=420)
        password = Label(frame, text="New password", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=260)

        self.password_txt = Entry(frame, font=("arial"), bg='lightgrey')
        self.password_txt.place(x=20, y=290, width=200)

        confirm_password = Label(frame, text="Confirm password", font=("helvetica", 15, "bold"), bg="white").place(
            x=240, y=260)
        self.confirm_password_txt = Entry(frame, font=("arial"), bg='lightgrey')
        self.confirm_password_txt.place(x=240, y=290, width=200)
        self.signup = Button(frame, text="Sign Up", command=self.signup, font=("times new roman", 18, "bold"),
                             bd=0, cursor="hand2", bg="green2", fg="white")
        self.signup.place(x=120, y=470, width=250)

    def regclear(self):

        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.password_txt.delete(0, END)
        self.confirm_password_txt.delete(0, END)

    def signup(self):

        if self.fname_txt.get() == "" or self.lname_txt == "" or self.email_txt.get() == "" or self.password_txt == "" \
                or self.confirm_password_txt == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.window)
        elif self.password_txt.get() != self.confirm_password_txt.get():
            messagebox.showerror("Error!", "Password and Confirm Password does not match", parent=self.window)
            # if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "":

            messagebox.showerror("Error", "All Fields Are Required", parent=self.window)

        else:
            try:
                db_name = "nano_degree_game_1"
                db_connection = _connect_to_db(db_name)
                cur = db_connection.cursor()
                query = """SELECT * FROM register WHERE email=%s"""
                data = (self.email_txt.get())
                cur.execute(query, (data,))
                row = cur.fetchone()
                # # if a row is found
                if row != None:
                    messagebox.showerror("Error", "User already Exist,Please try with another Email",
                                         parent=self.window)

                else:
                    query = """
                    INSERT INTO register(f_name,l_name,email,password,confirm_password) VALUES(%s,%s,%s,%s,%s)"""

                    data = (
                        self.fname_txt.get(), self.lname_txt.get(), str(self.email_txt.get()), self.password_txt.get(),
                        self.confirm_password_txt.get())

                    cur.execute(query, data)
                    db_connection.commit()
                    db_connection.close()

                    messagebox.showinfo("Success", "Register Successful", parent=self.window)
                    self.regclear()



            except Exception as es:

                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.window)



