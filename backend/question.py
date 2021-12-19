import random

from database.sql_python_connection import get_question, get_correct_answer, get_incorrect_answers


class Question:

    def __init__(self, question = None, choices = None, correct = None):
        self.question = question
        self.choices = choices
        self.correct = correct
    
    def populate_question(self, question_number):
        self.question = get_question(question_number)
        self.correct = get_correct_answer(question_number)
        incorrect_answers = get_incorrect_answers(question_number)
        choices = incorrect_answers + [self.correct]
        random.shuffle(choices)
        self.choices = choices
    
    # def print_question(self):
    #     print(self.question)
    #     print(self.choices)
    #     print(self.correct)



        