from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
#from login import Login
from PIL import ImageTk, Image, ImageFont
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
        self.window.title("Snake Charmer Sign Up")
        self.window.geometry("1366x700+0+0")
        self.window.config(bg="green")
        self.window.resizable(False, False)
        # add a frame or block in the window
        frame = Frame(self.window, bg="black")
        # place frame in the window, main frame
        frame.place(x=0, y=0, height=700, width=1366)
        # set background image
        canvas = Canvas(frame, height=700, width=1366)
        canvas.pack()
        image = Image.open("bkgroundimage_signup.jpeg")
        canvas.image = ImageTk.PhotoImage(image.resize((1366, 700), Image.ANTIALIAS))
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')
        # another frame to add buttons for user,email basically subframe
        frame_input = Frame(self.window, bg='white')
        frame_input.place(x=500, y=130, height=450, width=350)
        # styling of the signup header, fg text color, bg
        signup_header_label = Label(frame_input, text="Create an account ", font=("Arial", 24, "bold"), fg="black", bg="white")
        signup_header_label.place(x=35, y=10)
        f_name = Label(frame_input, text="First name", font=("Arial", 20, "bold"),fg='black', bg="white")
        f_name.place(x=20, y=60)
        # the input box
        self.fname_txt = Entry(frame_input, font=("Arial", 15, "bold"), bg='lightgray', fg='#7843E6')
        # place to show in window
        self.fname_txt.place(x=20, y=90, width=290, height=35)
        # styling of the input header, fg text color, bg
        l_name = Label(frame_input, text="Last name", font=("Arial", 20, "bold"), fg='black', bg='white')
        l_name.place(x=20, y=130)
        # the input box
        self.lname_txt = Entry(frame_input, font=("Arial", 15, "bold"), bg='lightgray', fg='#7843E6')
        # place to show in window
        self.lname_txt.place(x=20, y=160, width=290, height=35)
        # styling of the input header, fg text color, bg
        email = Label(frame_input, text="Email", font=("Arial", 20, "bold"), fg='black', bg='white')
        email.place(x=20, y=200)
        # the input box
        self.email_txt = Entry(frame_input, font=("Arial", 15, "bold"), bg='lightgray', fg='#7843E6')
        # place to show in window
        self.email_txt.place(x=20, y=230, width=290, height=35)
        # styling of the input header, fg text color, bg
        password = Label(frame_input, text="New password", font=("Arial", 20, "bold"), fg='black', bg='white')
        password.place(x=20, y=270)
        # the input box
        self.password_txt = Entry(frame_input, font=("Arial", 15, "bold"), bg='lightgray', fg='#7843E6', show='*')
        # place to show in window
        self.password_txt.place(x=20, y=300, width=290, height=35)
        # styling of the input header, fg text color, bg
        confirm_password = Label(frame_input, text="Confirm password", font=("Arial", 20, "bold"), fg='black', bg='white')
        confirm_password.place(x=20, y=340)
        # the input box
        self.confirm_password_txt = Entry(frame_input, font=("Arial", 15, "bold"), bg='lightgray', fg='#7843E6', show='*')
        # place to show in window
        self.confirm_password_txt.place(x=20, y=370, width=290, height=35)
        self.signup = Button(frame_input, text="Sign Up", command=self.signup, cursor="hand2",
                             font=("Arial", 18, "bold"), bg="white", fg="#7843E6", bd=0,)
        self.signup.place(x=20, y=410, width=290)

        self.window.mainloop()

    def redirect_window(self):
        self.window.destroy()
        from login import Login
        window = Tk()
        Login(window)

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
                    self.redirect_window()



            except Exception as es:

                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.window)


