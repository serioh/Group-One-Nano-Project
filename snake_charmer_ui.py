from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
# presumably the above could just be written from tkinter import *
from snake_brain import SnakeBrain

THEME_COLOR = "#90EE90"  # A "PaleGreen" to go with our snake theme


class QuizInterface:

    def __init__(self, snake_brain: SnakeBrain) -> None:
        self.quiz = snake_brain
        self.window = Tk()
        self.window.title("Snake Charmer Practice Quiz")
        self.window.geometry("850x550")

        # Display Title
        self.display_title()

        # Creating a canvas for question text and display question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(
            400, 125, text="Question here", width=680, fill=THEME_COLOR,
            font=('Arial', 15, 'italic'))  # Feel free to change the font and italics
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Use a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options w/ radio buttons
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.window, pady=10, font=("arial", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Next and Quit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()

    def display_title(self):
        # Does what it says on the tin

        # Title
        # Please note bg = background, fg = foreground (text colour)
        title = Label(self.window,
                      text="BETA Snake Charmer Quiz Game",
                      width=50,
                      bg="DarkGreen",  # Sea Green
                      fg="white",  # DarkGoldenrod
                      font=("arial", 20, "bold")
                      )

        # title placement
        title.place(x=0, y=2)

    def display_question(self):
        # To display the question

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        # To make four options in radio buttons

        # We initialise the list w/ an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(choice_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(
                self.window,
                text="",
                variable=self.user_answer,
                value='',
                font=("arial", 14)
            )

            # adding the button to the list
            choice_list.append(radio_btn)

            # button placement
            radio_btn.place(x=200, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

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

    def next_btn(self):
        # Shows feedback for each answer and checks for more questions

        # Check to see if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "white"
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
            self.window,
            text="Next",
            command=self.next_btn,
            width=10,
            bg="green",
            fg="black",
            font=("arial", 16, "bold")
        )

        # placing the Next button on the screen
        next_button.place(x=350, y=460)

        quit_button = Button(
            self.window,
            text="Quit",
            command=self.window.destroy,
            width=5,
            bg="gray",  # Dark grey
            fg="black",
            font=("arial", 16, "bold")
        )

        # Quit button placement on screen
        quit_button.place(x=700, y=50)

    def display_result(self):
        # To display the result using messagebox
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # caculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # shows a messagebox to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
