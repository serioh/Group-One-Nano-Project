import mysql.connector
from database.config import USER, PASSWORD, HOST

"""
This is a script you run at the beginning to create the SQL Database at the beginning
"""


def create_database():
    my_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
    )

    cur = my_db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS nano_degree_game_1")

    cur.close()


def create_questions_table():
    my_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database="nano_degree_game_1",

    )

    cur = my_db.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS`Questions` (
                `Q_Number` INTEGER NOT NULL,
                `Question` VARCHAR(300) NOT NULL,
                `Topic` VARCHAR(300) NOT NULL,
                `Difficulty_Level` INTEGER NOT NULL,
                `Answer` VARCHAR(300) NOT NULL,
                `Multiple_Choice` INTEGER NOT NULL,
                CONSTRAINT `PK_Q_Number` PRIMARY KEY (`Q_Number`));""")

    cur.close()


def create_multiple_choice_table():
    my_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database="nano_degree_game_1",

    )

    cur = my_db.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS`Multiple_choice` (
                `Q_Number` INTEGER NOT NULL,
                `Incorrect_answer_1` VARCHAR(300) NOT NULL,
                `Incorrect_answer_2` VARCHAR(300) NOT NULL,
                `Incorrect_answer_3` VARCHAR(300) NOT NULL,
                CONSTRAINT `FK_Q_Number` FOREIGN KEY (`Q_Number`)
                REFERENCES `Questions`(`Q_Number`));""")

    cur.close()

def create_registration_table():
    my_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database="nano_degree_game_1",

     )

    cur = my_db.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS Register (
                F_name VARCHAR(50) NOT NULL,
                L_name VARCHAR(50) NOT NULL,
                Email VARCHAR(100) NOT NULL UNIQUE,
                Password VARCHAR(20) NOT NULL,
                Confirm_password VARCHAR(20) NOT NULL);""")

    cur.close()


def insert_questions():
    my_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database="nano_degree_game_1",

    )

    cur = my_db.cursor()
    query = """INSERT IGNORE INTO questions (`Q_Number`, `Question`, `Topic`, `Difficulty_Level`, `Answer`, `Multiple_Choice`)
                VALUES (%s, %s, %s, %s, %s, %s)"""
    val = [
        (1, 'What are the three numeric types in Python?', 'Numbers', 1, "Integers (int), Floats (float) and Complex Numbers (complex)", 1),
        (2, 'Which of the following is an example of a list?', 'Lists', 1, 'ice_cream = ["vanilla", "strawberry", "pistachio", "chocolate"]', 1),
        (3, 'What method do you use to add an item to the end of a list?', 'Lists', 1, '.append()', 1),
        (4, 'Dictionaries in Python store data values in key:value pairs. Which one of these is a correct example of a dictionary?', 'Dictionaries', 1, "cake = {'flavor': 'coconut', 'color': 'white', 'type': 'layer cake'}", 1),
        (5, 'A tuple is one of the four built-in data types in Python. Which of these best describes a tuple?', 'Tuples', 1, 'A tuple is a collection which is unchangeable and ordered.', 1),
        (6, "word = 'Python' Which one of these will not print the output 'This is Python'?", 'Strings', 1, 'print("This is".append(word))', 1),
        (7, 'What is 5//2 ?', 'Operator', 1, '2', 1),
        (8, 'Which operation should be done first?', 'Operators', 1, 'Parentheses', 1),
        (9, 'What is print(True or False)?', 'Boolean', 1, 'True', 1),
        (10, 'ListZ = [a for a in range(5)]. What is ListZ?', 'Lists', 1, '[0,1,2,3,4]', 1),
        (11, 'Which of the following is a good naming convention in python for variables?', 'Syntax', 1, 'my_variable', 1),
        (12, 'Which of the following is a string method?', 'String Methods', 1, 'join()', 1),
        (13, 'Which of the following are methods for a Tuple?', 'Tuple Methods', 1, 'count(), index()', 1),
        (14, 'Which among the following does not allow duplicate items?', 'Sets', 1, 'set', 1),
        (15, 'Which operator can be used to compare two values?', 'Operators', 1, '!=', 1),
        (16, 'What is the term used to describe serialising of python objects when transferring over a network?', 'Theory', 1, 'Pickling', 1),
        (17, "str = 'hello' how do we get the following output: 'olleh'", 'String Methods', 1, 'print(str[::-1])', 1),
        (18, '"What output will the following give: print(2 % 2)"', 'Operators', 1, '0', 1),
        (19, '"What does the following return: "Hi".isupper()"', 'String Methods', 1, 'False', 1),
        (20, '"my_list = [1, 56, 8, 2]; fill in the blank index to print "8" from my_list. print(my_list[_])"', 'Lists', 1, '2', 1),
        (21, 'In Python, what is the term typically used to describe the type of iteration a while loop is used for?', 'Loops', 1, 'Indefinite', 1),
        (22, '"Which of the following is a method for both a list and a tuple?"', 'Lists/Tuples', 1, 'index()', 1),
        (23, '"In file handling, the open() function takes two parameters. What are they?"', 'File Handling', 1, 'filename and mode', 1),
        (24, 'How do we add a new item to index 1 to this list? our_pets = ["Foxx", "Broccoli"]', 'Lists', 1, "our_pets.insert(1, 'Biscoff')", 1),
        (25, '"What is the output of the following code: print((lambda x: (x + 9) * 2 / 4)(3))"', 'Functions', 1, '6.0', 1),
        (26, '"What is the output of the following code:\nfrom functools import reduce\nnumbers = [4, 5, 3]\nprint(reduce(lambda x, y: x + y, numbers))"', 'Functions', 1, '12', 1)
    ]

    cur.executemany(query, val)
    my_db.commit()

    cur.close()


def insert_choices():
    my_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database="nano_degree_game_1",

    )

    cur = my_db.cursor()
    query = """INSERT IGNORE INTO Multiple_Choice (Q_Number, Incorrect_answer_1, Incorrect_answer_2, Incorrect_answer_3)
                VALUES (%s, %s, %s, %s)"""

    val = [
        (1, 'Integers (int), Floats (float) and Fractions (frac)', 'Integers (int), Fractions (frac) and Negatives (neg)', 'Floats (float), Decimals (dec) and Whole Numbers (whole)'),
        (2, 'ice_cream = ["ice_cream = "vanilla", "strawberry", "pistachio", "chocolate"]', 'ice_cream = {"vanilla", "strawberry", "pistachio", "chocolate"}', 'ice_cream = ("vanilla", "strawberry", "pistachio", "chocolate")'),
        (3, '.addition()', '.plus()', '.addon()'),
        (4, 'cake = ["flavor": "coconut", "color": "white", "type": "layer cake"]', 'cake = {"flavor", "coconut", "color", "white", "type", "layer cake"}', 'cake = ("flavor": "coconut", "color": "white", "type": "layer cake")'),
        (5, 'A tuple is a collection which is unchangeable and unordered.', 'A tuple is a collection which is changeable and ordered.', 'A tuple is a collection which is changeable and can be ordered or unordered, depending on how it is used.'),
        (6, 'print(f"This is {word}")', 'print("This is {}".format(word))', 'print("This is " + word)'),
        (7, '2.5', '3', '1'),
        (8, 'Exponents', 'Multiplication', 'Division'),
        (9, 'None', 'Error', 'False'),
        (10, '[0,1,2,3,4,5]', '[1,2,3,4,5]', '[1,2,3,4]'),
        (11, '12_variable', ' ##variable', '__variable'),
        (12, 'append()', 'get()', 'read()'),
        (13, 'clear(),count()', 'append(),extend()', 'pop(),insert()'),
        (14, 'List', 'Tuple', 'Strings'),
        (15, '<>', '>>', '**'),
        (16, 'Decoding', 'Hashing', 'Unpickling'),
        (17, 'print(str[::])', 'print(reversed(str))', 'print(str[::1])'),
        (18, '2', '0.5', '1'),
        (19, 'None', 'Error', 'True'),
        (20, '3', '-1', '0'),
        (21, 'Discriminant', 'Indeterminate', 'Definite'),
        (22, 'sort()', 'clear()', 'pop()'),
        (23, 'read and write', 'text and binary', "create and modify"),
        (24, "our_pets.pop('Biscoff', 1)", "our_pets.append(1, 'Biscoff')", "our_pets.add('Biscoff', 1)"),
        (25, '12.0', 'Syntax Error', '0'),
        (26, '6', '60', 'Syntax Error')
    ]

    cur.executemany(query, val)
    my_db.commit()
    cur.close()



def run_database():
    create_database()
    create_questions_table()
    create_multiple_choice_table()
    insert_questions()
    insert_choices()
    create_registration_table()
