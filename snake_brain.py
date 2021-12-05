"""
Code inspo:
How to Build a GUI Quiz Application using Tkinter and Open Trivia DB
https://python.plainenglish.io/how-to-build-a-gui-quiz-application-using-tkinter-and-open-trivia-db-79b45391bba2


API URL: https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple

"""
# import fetch_questions

class SnakeBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        # To check if quiz has more questions

        return self.question_no < len(self.questions)

    def next_question(self):
        # Get the next question by incrementing the question number

        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question
        return f"Q. {self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        # Check the user answer against the correct answer and maintain score

        correct_answer = self.current_question.correct
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        # Get the number of correct answers, wrong answers and score percentage

        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)

        # If we don't want to do percentage, as we discussed
        # delete the score_percent variable and remove it from the return

