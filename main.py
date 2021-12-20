"""This is the main file"""
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
