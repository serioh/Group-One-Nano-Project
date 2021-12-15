from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from tkinter import *
# presumably the above could just be written from tkinter import *
from snake_brain import SnakeBrain
from PIL import ImageTk, Image, ImageFont

THEME_COLOR = "#7843E6"  # A "Purple" to go with our theme


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
        self.image = Image.open("bkgroundimage_game.jpeg")
        self.canvas.image = ImageTk.PhotoImage(self.image.resize((1366, 800), Image.ANTIALIAS))
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        # another frame to add buttons for user,email basically subframe
        self.frame_input = Frame(self.window, bg='white')
        self.frame_input.place(x=238, y=120, height=600, width=890)
        self.canvas1 = Canvas(self.frame_input, height=600, width=890)
        self.canvas1.pack()
        self.question_text = self.canvas1.create_text(
            400, 100, text="Question here", width=800, fill=THEME_COLOR,
            font=('Bebas Neue Regular', 20, 'bold'))  # Feel free to change the font and italics
        #Display Question
        self.display_question()

        # Use a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options w/ radio buttons
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.frame_input, pady=10, font=("Bebas Neue Regular", 15, "bold"))
        self.feedback.place(x=700, y=550)

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
                font=("Bebas Neue Regularl", 14)
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
        self.user_answer.set(None)

        # looping over the options to be displayed for the text of the radio buttons
        for option in self.quiz.current_question.choices:
            self.opts[val]["text"] = option
            self.opts[val]["value"] = option
            val += 1

    def wrong_questions_message(self):
        self.feedback["text"] = "Try this question again"

    def next_btn(self):
        # Shows feedback for each answer and checks for more questions

        # Check to see if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "#000000" #Black
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
            # if self.quiz.question_no > 10:
            #     self.wrong_questions_message()
        else:
            # If no more questions, then shows score
            self.display_result()
            if len(self.quiz.wrong_questions) > 0:
                self.try_again()
            else:
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
            font=("Bebas Neue Regular", 16, "bold")
        )

        # placing the Next button on the screen
        next_button.place(x=405, y=560)

        quit_button = Button(
            self.frame_input,
            text="Quit",
            command=self.window.destroy,
            width=5,
            bg="gray",  # Dark grey
            fg="black",
            font=("Bebas Neue Regular", 16, "bold")
        )

        # Quit button placement on screen
        quit_button.place(x=840, y=15)

    def display_result(self):
        # To display the result using messagebox
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # caculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # shows a messagebox to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def display_wrong_questions(self):
        for key, value in self.quiz.wrong_questions.items():
            q_text = key
            # q_text = q
            self.canvas1.itemconfig(self.question_text, text=q_text)

    def display_wrong_question_options(self):
        val = 0

        # deselecting the options
        self.user_answer.set(None)
        i = 0
        # looping over the options to be displayed for the text of the radio buttons
        for key, value in self.quiz.wrong_questions.items():
            while i < len(self.quiz.wrong_questions):
                self.opts[val]["text"] = value[i]
                self.opts[val]["value"] = value[i]
                val += 1
                i += 1

    def try_again(self):
        again = messagebox.askquestion("Continue?", "Do you want to try the wrong questions again?")
        if again == "yes":
            self.display_wrong_questions()
            self.display_wrong_question_options()
        else:
            self.window.destroy()



