import random

from main import create_question_bank
from unittest.mock import MagicMock, patch
from backend.question import Question




class TestMain:

    @patch('database.sql_python_connection.get_question_count')
    def test_create_question_bank(self, mock_get_question_count):
        mock_get_question_count.returnvalue = MagicMock(26)
        # random.seed(1), numbers == [5, 19, 3, 9, 4, 16, 15, 21, 13, 7]
        random.seed(1)
        question_bank  = create_question_bank()
        random.seed()

        assert len(question_bank) == 10
        for q in range(10):
            assert type(question_bank[q]) is Question
        assert question_bank[0].question == 'A tuple is one of the four built-in data types in Python. Which of these best describes a tuple?'
        assert question_bank[9].correct == '2'

