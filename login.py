from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageFont
from config import USER, PASSWORD, HOST
from sql_python_connection import _connect_to_db


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
        Frame_login = Frame(self.window, bg='black')
        # place frame in the window, main frame
        Frame_login.place(x=0, y=0, height=700, width=1366)
        # set background image
        canvas = Canvas(Frame_login, height=700, width=1366)
        canvas.pack()
        image = Image.open("bkgroundimage.jpeg")
        canvas.image = ImageTk.PhotoImage(image.resize((1366, 700), Image.ANTIALIAS))
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')
        # another frame to add buttons for user,email basically subframe
        frame_input = Frame(self.window, bg='white')
        frame_input.place(x=500, y=130, height=450, width=350)
        # styling of the login header, fg text color, bg
        login_header_label = Label(frame_input, text="Login Here", font=('Bebas Neue Regular', 32, 'bold'), fg="black",
                                   bg='white')
        login_header_label.place(x=105, y=20)

        email_label = Label(frame_input, text="Email", font=("Bebas Neue Regular", 20, "bold"),
                            fg='black', bg='white')
        email_label.place(x=30, y=95)
        # the input box
        self.email_txt = Entry(frame_input, font=("Bebas Neue Regular", 15, "bold"), bg='lightgray', fg='#7843E6')
        # place to show in window
        self.email_txt.place(x=30, y=145, width=290, height=35)

        pwd_label = Label(frame_input, text="Password", font=("Bebas Neue Regular", 20, "bold"), fg='black', bg='white')
        pwd_label.place(x=30, y=195)

        self.password = Entry(frame_input, font=("Bebas Neue Regular", 15, "bold"), bg='lightgray', fg='#7843E6')
        self.password.place(x=30, y=245, width=290, height=35)

        login_button = Button(frame_input, text="         LOGIN        ", command=self.login, cursor="hand2",
                              font=("Bebas Neue Regular", 15), bg="white", fg="#7843E6", bd=0)
        login_button.place(x=130, y=330)

        register_button = Button(frame_input, command=self.redirect_window, text="Not Registered? click here   "
                                 , cursor="hand2", font=("calibri", 10), bg='white', fg="black", bd=0)
        register_button.place(x=95, y=390)

    def login(self):

        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.window)

        else:

            try:

                db_name = "Nano_Degree_Game_1"
                db_connection = _connect_to_db(db_name)
                cur = db_connection.cursor()
                print("Connected to database")
                query = """SELECT * FROM register WHERE email= '{}' AND password = '{}'""".format(
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


            except Exception:
                pass

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
        from main import run

        obj = run()  # QuizInterface(window)
        obj.mainloop()

    def loginclear(self):

        self.email_txt.delete(0, END)

        self.password.delete(0, END)





