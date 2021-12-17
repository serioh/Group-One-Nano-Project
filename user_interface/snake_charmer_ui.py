from tkinter import messagebox
from tkinter import *
from backend.snake_brain import SnakeBrain
from PIL import ImageTk, Image
from pathlib import Path

THEME_COLOR = "#7843E6"  # A "Purple" to go with our theme

bkgroundimage_game = Path.cwd() / "user_interface" / "bkgroundimage_game.jpeg"


class QuizInterface:

    def __init__(self, snake_brain: SnakeBrain) -> None:
        self.quiz = snake_brain
        # initialise a variable window which would be used to create a tinker object
        self.window = Tk()
        # set the title of the window
        self.window.title("Snake Charmer Quiz")
        # set the size
        self.window.geometry("1366x800+0+0")
        self.window.resizable(False, False)

        # Creating a frame for question text and display question
        self.frame_general = Frame(self.window, bg='black')
        # place frame in the window, main frame
        self.frame_general.place(x=0, y=0, height=800, width=1366)
        # set background image
        self.canvas = Canvas(self.frame_general, height=800, width=1366)
        self.canvas.pack()
        self.image = Image.open(bkgroundimage_game)
        self.canvas.image = ImageTk.PhotoImage(self.image.resize((1366, 800), Image.ANTIALIAS))
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        # another frame to add buttons for user,email basically subframe
        self.frame_input = Frame(self.window, bg='white')
        self.frame_input.place(x=238, y=120, height=600, width=890)
        self.canvas1 = Canvas(self.frame_input, height=600, width=890)
        self.canvas1.pack()
        self.question_text = self.canvas1.create_text(
            400, 100, text="Question here", width=800, fill=THEME_COLOR,
            font=('Arial', 20, 'bold'))  # Feel free to change the font and italics
        #Display Question
        self.display_question()

        # Use a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options w/ radio buttons
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.frame_input, pady=10, font=("Arial", 15, "bold"))
        self.feedback.place(anchor=SE, relx=0.95, rely=0.99)

        # Next and Quit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()


    def display_question(self):
        # To display the question

        q_text = self.quiz.next_question()
        self.canvas1.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        # To make four answer multiple choice options in radio buttons format

        # We initialise the list w/ an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 230

        # adding the options to the list
        while len(choice_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(
                self.frame_input,
                text="",
                variable=self.user_answer,
                value='',
                font=("Arial", 14)
            )

            # adding the button to the list
            choice_list.append(radio_btn)

            # button placement
            radio_btn.place(x=20, y=y_pos)

            # incrementing the y-axis position by 80
            y_pos += 90

        # return the radio buttons
        return choice_list

    def display_options(self):
        # To display the four options

        val = 0

        # deselecting the options
        if 'None' in self.quiz.current_question.choices:
            no_selection = "Default"
        else:
            no_selection = None
        self.user_answer.set(no_selection)

        # looping over the options to be displayed for the text of the radio buttons
        for option in self.quiz.current_question.choices:
            self.opts[val]["text"] = option
            self.opts[val]["value"] = option
            val += 1

    def next_btn(self):
        # Shows feedback for each answer and checks for more questions

        # Check to see if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
<<<<<<< HEAD:user_interface/snake_charmer_ui.py
            self.feedback["fg"] = "#000000"
=======
            self.feedback["fg"] = "#C000000"
>>>>>>> cf9d1d2 (changed that's correct to black):snake_charmer_ui.py
            self.feedback["text"] = "That's correct!"

        else:
            self.feedback["fg"] = "#C70039"  # Red
            self.feedback["text"] = "Sorry, that's incorrect."
            # alternatively
            # self.feedback["text"] = ("Sorry, that's incorrect.\n"
            # f"The correct answer is: {self.quiz.current_question.correct_answer}")

        if self.quiz.has_more_questions():
            # Moves to the next display
            self.display_question()
            self.display_options()
        else:
            # If no more questions, then shows score
            self.display_result()

            # destroys the self.window
            self.window.destroy()

    def buttons(self):
        # To show next button and quit button

        next_button = Button(
            self.frame_input,
            text="Next",
            command=self.next_btn,
            width=10,
            bg="white",
            fg="#7843E6",
            font=("Arial", 16, "bold")
        )

        # placing the Next button on the screen
        next_button.place(anchor=S, relx = 0.5, rely = 0.98)

        quit_button = Button(
            self.frame_input,
            text="Quit",
            command=self.window.destroy,
            width=5,
            bg="gray",  # Dark grey
            fg="black",
            font=("Arial", 16, "bold")
        )

        # Quit button placement on screen
        quit_button.place(anchor =NE, relx=0.98, rely=0.02)

    def display_result(self):
        # To display the result using messagebox
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # shows a messagebox to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")

