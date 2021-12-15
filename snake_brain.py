"""
Code inspo:
How to Build a GUI Quiz Application using Tkinter and Open Trivia DB
https://python.plainenglish.io/how-to-build-a-gui-quiz-application-using-tkinter-and-open-trivia-db-79b45391bba2


API URL: https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple

"""
# import fetch_questions
from question import Question

class SnakeBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None
        for idx, question in enumerate(self.questions):
            question.index = idx
        self.wrong = None
        self.wrong_questions = []

    def has_more_questions(self):
        # To check if quiz has more questions

        return self.question_no < len(self.questions)

    def next_question(self):
        # Get the next question by incrementing the question number
        if self.current_question == None:
            self.current_question = self.questions[0]
            self.current_question.index = 0
        else:
            self.current_question = self.questions[self.current_question.index]
        self.current_question.index += 1
        self.question_no += 1
        q_text = self.current_question.question
        return f"Q. {self.current_question.index}: {q_text}"

    def check_answer(self, user_answer):
        # Check the user answer against the correct answer and maintain score
        correct_answer = self.current_question.correct
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        elif user_answer.lower() != correct_answer.lower():
            wrong = Question(self.current_question)
            # self.current_question.populate_question()
            self.wrong_questions.append(wrong)
            return False

    def get_score(self):
        # Get the number of correct answers, wrong answers and score percentage

        self.wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return self.score, self.wrong, score_percent

        # If we don't want to do percentage, as we discussed
        # delete the score_percent variable and remove it from the return
