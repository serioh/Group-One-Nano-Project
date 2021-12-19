from database.sql_python_connection import get_correct_answer, get_incorrect_answers, get_question, get_question_count, open_connection_pool

class TestSQLPythonConnection:
    open_connection_pool()

    def test_get_question(self):
        question = get_question(1)
        assert question == 'What are the three numeric types in Python?'

    def test_get_correct_answer(self):
        answer = get_correct_answer(1)
        assert answer == "Integers (int), Floats (float) and Complex Numbers (complex)"

    def test_get_incorrect_answers(self):
        incorrect = get_incorrect_answers(1)
        assert incorrect == ['Integers (int), Floats (float) and Fractions (frac)', 'Integers (int), Fractions (frac) and Negatives (neg)', 'Floats (float), Decimals (dec) and Whole Numbers (whole)']

    def test_get_question_count(self):
        count = get_question_count()
        assert count == 26