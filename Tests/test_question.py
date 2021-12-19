import random

from backend.question import Question
from unittest.mock import MagicMock, patch

class TestQuestion:

    def test_create_empty_question_instance(self):
        example_question = Question()

        assert example_question.question == None
        assert example_question.choices == None
        assert example_question.correct == None
    
    @patch('sql_python_connection.get_question')
    @patch('sql_python_connection.get_correct_answer')
    @patch('sql_python_connection.get_incorrect_answers')
    def test_populate_question(self, mock_get_question, mock_get_correct_answer, mock_get_incorrect_answers):
        mock_get_question.returnvalue = MagicMock("What are the three numeric types in Python?")
        mock_get_correct_answer.returnvalue = MagicMock("Integers (int), Floats (float) and Complex Numbers (complex)")
        mock_get_incorrect_answers.returnvalue = MagicMock(['Integers (int), Floats (float) and Fractions (frac)', 'Integers (int), Fractions (frac) and Negatives (neg)', 'Floats (float), Decimals (dec) and Whole Numbers (whole)'])
        example_question = Question()
        random.seed(1)
        example_question.populate_question(1)
        random.seed()
        assert example_question.question == "What are the three numeric types in Python?"
        assert example_question.correct == "Integers (int), Floats (float) and Complex Numbers (complex)"
        assert example_question.choices == ['Integers (int), Floats (float) and Complex Numbers (complex)', 'Integers (int), Floats (float) and Fractions (frac)', 'Floats (float), Decimals (dec) and Whole Numbers (whole)', 'Integers (int), Fractions (frac) and Negatives (neg)']


