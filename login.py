from tkinter import *

from tkinter import messagebox
from config import USER, PASSWORD, HOST
from sql_python_connection_rz import _connect_to_db


class Login:

    def __init__(self):
        # initialise a variable window which would be used to create a tinker object
        self.window = Tk()
        # set the title of the window
        self.window.title("Snake Charmer Login")
        # set the size
        self.window.geometry("1366x700+0+0")
        # self.window.geometry("850x550")
        self.window.resizable(False, False)
        self.loginform()
        # Mainloop
        self.window.mainloop()

    def loginform(self):
        # add a frame or block in the window
        Frame_login = Frame(self.window, bg="#90EE90")
        # place frame in the window, main frame
        Frame_login.place(x=0, y=0, height=700, width=1366)
        # another frame to add buttons for user,email basically subframe
        frame_input = Frame(self.window, bg='white')
        frame_input.place(x=320, y=130, height=450, width=350)
        # styling of the login header, fg text color, bg
        login_header_label = Label(frame_input, text="Login Here", font=('arial', 32, 'bold'), fg="black",
                                   bg='white')
        login_header_label.place(x=75, y=20)

        email_label = Label(frame_input, text="Email", font=("Goudy old style", 20, "bold"),
                            fg='blue', bg='white')
        email_label.place(x=30, y=95)
        # the input box
        self.email_txt = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        # place to show in window
        self.email_txt.place(x=30, y=145, width=270, height=35)

        pwd_label = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg='blue', bg='white')
        pwd_label.place(x=30, y=195)

        self.password = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)

        forgot_pwdbutton = Button(frame_input, text="forgot password?", cursor='hand2', font=('calibri', 10),
                                  bg='white', fg='black', bd=0)
        forgot_pwdbutton.place(x=125, y=305)

        login_button = Button(frame_input, text="Login", command=self.login, cursor="hand2",
                              font=("times new roman", 15)
                              , fg="white", bg="blue", bd=0, width=15, height=1)
        login_button.place(x=90, y=340)

        register_button = Button(frame_input, command=self.redirect_window, text="Not Registered? register"
                                 , cursor="hand2", font=("calibri", 10), bg='white', fg="black", bd=0)
        register_button.place(x=110, y=390)

    def login(self):

        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.window)

        else:

            try:

                db_name = "Nano_Degree_Game_1"
                db_connection = _connect_to_db(db_name)
                cur = db_connection.cursor()
                print("Connected to database")
                query = """SELECT * FROM register WHERE email= '{}' AND password = {}""".format(
                    self.email_txt.get(),
                    self.password.get())
                cur.execute(query)
                row = cur.fetchone()

                if row == None:

                    messagebox.showerror('Error', 'Invalid Username And Password', parent=self.window)
                    self.loginclear()
                    self.email_txt.focus()

                else:

                    self.appscreen()

                    cur.close()

            except Exception as es:

                messagebox.showerror('Error', f'Error Due to : {str(es)}'

                                     , parent=self.window)

    def redirect_window(self):
        self.window.destroy()
        from Register import Register
        window = Tk()
        obj = Register(window)
        window.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def appscreen(self):

        self.window.destroy()
        print('welcome')
        # from snake_charmer_ui import QuizInterface
        from main import run
        # window = Tk()
        obj = run()  # QuizInterface(window)
        obj.mainloop()

    def loginclear(self):

        self.email_txt.delete(0, END)

        self.password.delete(0, END)


# window = Tk()
# obj = Login(window)
# window.mainloop()
