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
from question import Question
from snake_brain import SnakeBrain
from snake_charmer_ui import QuizInterface
from login import Login
from sql_python_connection import get_question_count, open_connection_pool
from tkinter import *
from create_database import *

def create_question_bank():
    open_connection_pool()
    question_count = get_question_count()
    question_numbers = random.sample(range(1, question_count+1), 10)
    question_bank = []
    for q in question_numbers:
        question = Question()
        question.populate_question(q)
        question_bank.append(question)
    return question_bank

""" run adds all the functions in the game, and its being called in thSe login page"""
def run():
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
    # question_bank = create_question_bank()
    # print(question_bank)
    # quiz = SnakeBrain(question_bank)
    #
    # quiz_ui = QuizInterface(quiz)
    #
    # print("You've completed the quiz")
    # print(f"Your final score was: {quiz.score}/{quiz.question_no}")
    # main.loop going more than once, hence the error after the quiz is finished, would look into this or if you have
    # any hint to solve this
    run_database()
    Login()
