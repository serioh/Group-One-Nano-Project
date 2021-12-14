import random

from main import create_question_bank
from snake_brain import SnakeBrain


class TestSnakeBrain:
    # random.seed(1), numbers == [5, 19, 3, 9, 4, 16, 15, 21, 13, 7]
    random.seed(1)
    question_bank  = create_question_bank()
    random.seed()

    def test_snakebrain_instance(self):
        brain = SnakeBrain(TestSnakeBrain.question_bank)

        assert brain.questions == TestSnakeBrain.question_bank
        assert brain.question_no == 0

    def test_next_question(self):
        brain = SnakeBrain(TestSnakeBrain.question_bank)
        text = brain.next_question() 

        assert brain.question_no == 1    
        assert text == 'Q. 1: A tuple is one of the four built-in data types in Python. Which of these best describes a tuple?'

    def test_has_more_questions(self):
        brain = SnakeBrain(TestSnakeBrain.question_bank)
        brain.question_no = 10

        assert brain.has_more_questions() == False

    def test_check_answer(self):
        brain = SnakeBrain(TestSnakeBrain.question_bank)   
        brain.next_question() 

        assert brain.check_answer('A tuple is a collection which is unchangeable and ordered.') == True
        assert brain.check_answer('A tuple is a collection which is unchangeable and unordered.') == False
        assert brain.score == 1

    def test_check_score(self):
        brain = SnakeBrain(TestSnakeBrain.question_bank)
        brain.next_question() 

        assert brain.check_answer('A tuple is a collection which is unchangeable and ordered.') == True
        brain.question_no = 10
        assert brain.get_score() == (1, 9, 10)
                     

