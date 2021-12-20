"""This is the main file"""

"""
Possible class ideas:
class Question (create an instance of this class each time you want to show a question)
- Will contain correct answer, wrong answer as an attribute
- Attributes taken from connecting to the SQL server
- Can use permutations itertool in a method to select how it will be displayed?

class Player (create an instance of this class for each user)
- Attributes (private ones probably) will include username, password, score history
- Can login, delete player, show previous scores etc...

class Test (create an instance every time you start a new test)
- Brings up options to select difficulty of questions you want
- Calculates total score from no. of questions you get right?
- in main, create instance of test, then instances of questions


"""
import random
from backend.question import Question
from backend.snake_brain import SnakeBrain
from user_interface.snake_charmer_ui import QuizInterface
from user_interface.login import Login
from database.sql_python_connection import get_question_count, open_connection_pool
from tkinter import *
from database.create_database import *


def create_question_bank():
    open_connection_pool()
    question_count = get_question_count()
    question_numbers = random.sample(range(1, question_count + 1), 10)
    question_bank = []
    for q in question_numbers:
        question = Question()
        question.populate_question(q)
        question_bank.append(question)
    return question_bank


def run():
    """ A function to add all the functions in the game, and its being called in the login page"""
    question_bank = create_question_bank()
    quiz = SnakeBrain(question_bank)
    quiz_ui = QuizInterface(quiz)
    print("You've completed the quiz")
    if quiz.question_no == 10:
        number = 10
    else:
        number = quiz.question_no - 1
    print(f"Your final score was: {quiz.score}/{number}")

    return quiz_ui


if __name__ == "__main__":
    # for creation of db, tables, and inserting questions
    run_database()
    # run the login
    Login(Tk())
