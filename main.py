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
from sql_python_connection_rz import get_question_count

def create_question_bank():
    question_count = get_question_count()
    question_numbers = random.sample(range(1, question_count+1), 10)
    question_bank = []
    for q in question_numbers:
        question = Question()
        question.populate_question(q)
        question.print_question()
        question_bank.append(question)
    return question_bank

if __name__ == "__main__":
    question_bank = create_question_bank()
    print(question_bank[0].choices)
    quiz = SnakeBrain(question_bank)

    quiz_ui = QuizInterface(quiz)

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_no}")
