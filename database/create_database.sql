CREATE database Nano_Degree_Game_1;
USE Nano_Degree_GAME_1;

CREATE TABLE IF NOT EXISTS `Questions` (
    `Q_Number` INTEGER NOT NULL UNIQUE,
    `Question` VARCHAR(300) NOT NULL UNIQUE,
    `Topic` VARCHAR(300) NOT NULL,
    `Difficulty_Level` INTEGER NOT NULL,
    `Answer` VARCHAR(300) NOT NULL,
    `Multiple_Choice` INTEGER NOT NULL,
    CONSTRAINT `PK_Q_Number` PRIMARY KEY (`Q_Number`));

CREATE TABLE IF NOT EXISTS `Multiple_choice` (
    `Q_Number` INTEGER NOT NULL UNIQUE,
    `Incorrect_answer_1` VARCHAR(300) NOT NULL,
    `Incorrect_answer_2` VARCHAR(300) NOT NULL,
    `Incorrect_answer_3` VARCHAR(300) NOT NULL,
    CONSTRAINT `FK_Q_Number` FOREIGN KEY (`Q_Number`)
    REFERENCES `Questions`(`Q_Number`));

INSERT IGNORE INTO `Questions` (`Q_Number`, `Question`, `Topic`, `Difficulty_Level`, `Answer`, `Multiple_Choice`)
VALUES 
(2, 'What are the three numeric types in Python?', 'Numbers', 1, 'Integers (int), Floats (float) and Complex Numbers (complex)', 1),
(3, 'Which of the following is an example of a list?', 'Lists', 1, 'ice_cream = ["vanilla", "strawberry", "pistachio", "chocolate"]', 1),
(4, 'What method do you use to add an item to the end of a list?', 'Lists', 1, '.append()', 1),
(5, 'Dictionaries in Python store data values in key:value pairs. Which one of these is a correct example of a dictionary?', 'Dictionaries', 1, '"cake = {""flavor"": ""coconut"", ""color"": ""white"", ""type"": ""layer cake""}
"', 1),
(6, 'A tuple is one of the four built-in data types in Python. Which of these best describes a tuple?', 'Tuples', 1, 'A tuple is a collection which is unchangeable and ordered.', 1);

INSERT IGNORE INTO `Questions` (`Q_Number`, `Question`, `Topic`, `Difficulty_Level`, `Answer`, `Multiple_Choice`)
VALUES 
(7, '"word = ""Python""
Which one of these will not print the output ""This is Python""?"', 'Strings', 1, 'print("This is".append(word))', 1);

INSERT IGNORE INTO `Questions` (`Q_Number`, `Question`, `Topic`, `Difficulty_Level`, `Answer`, `Multiple_Choice`)
VALUES 
(8, 'What is 5//2 ?', 'Operator', 1, '2', 1),
(9, 'Which operation should be done first?', 'Operators', 1, 'Parentheses', 1),
(10, 'What is print(True or False)?', 'Boolean', 1, 'True', 1),
(11, 'ListZ = [a for a in range(5)]. What is ListZ?', 'Lists', 1, '[0,1,2,3,4]', 1),
(12, 'Which of the following is a good naming convention in python?', 'Syntax', 1, 'my_variable', 1),
(13, 'Which of the following is a string method?', 'String Methods', 1, 'join()', 1),
(14, 'Which of the following are methods for a Tuple?', 'Tuple Methods', 1, 'count(), index()', 1),
(15, 'Which among the following does not allow duplicate items?', 'Sets', 1, 'set', 1),
(16, 'Which operator can be used to compare two values?', 'Operators', 1, '!=', 1),
(17, 'What is the term used to describe serialising of python objects when transferring over a network?', 'Theory', 1, 'Pickling', 1),
(18, '"str = "hello"
how do we get the following output:
"olleh""', 'String Methods', 1, 'print(str[::-1])', 1),
(19, '"What output will the following give:
print(2 % 2)"', 'Operators', 1, '0', 1),
(20, '"What does the following return:
"Hi".isupper()"', 'String Methods', 1, 'False', 1),
(21, '"my_list = [1, 56, 8, 2]
fill in the blank index to print "8" from my_list.
print(my_list[_])"', 'Lists', 1, '2', 1),
(22, 'What type of iteration is "while" loop used for?', 'Loops', 1, 'Indefinite', 1),
(23, '"What is the output of the following code:
s = {"salt": 1, "pepper": 2, "chilli": 3}
while s:
    print(s.popitem())
print("Complete.")"', 'Loops', 1, '"("chilli", 3)
("pepper", 2)
("salt", 1)
Complete."', 1),
(24, '"What is the output of the following code:
s = {"salt": 1, "pepper": 2, "chilli": 3}
while len(s) > 3:
    print(s.popitem())
print("Complete.")"', 'Loops', 1, 'Complete.', 1),
(25, '"What is the output of the following code:
    s = ["salt", "pepper", "chilli", "garlic", "onion"]
while s:
    if len(s) < 3:
        break
    print(s.pop())
print("Complete.")"', 'Loops', 1, '"onion
garlic
chilli
Complete. "', 1),
(26, '"What is the output of the following code:
print((lambda x: (x + 9) * 2 / 4)(3))"', 'Functions', 1, '6.0', 1),
(27, '"What is the output of the following code:
from functools import reduce
numbers = [4, 5, 3]
print(reduce(lambda x, y: x + y, numbers))"', 'Functions', 1, '12', 1);

INSERT IGNORE INTO Multiple_Choice (Q_Number, Incorrect_answer_1, Incorrect_answer_2, Incorrect_answer_3)
VALUES (1, '2', '3', '4');
INSERT IGNORE INTO Multiple_Choice (Q_Number, Incorrect_answer_1, Incorrect_answer_2, Incorrect_answer_3)
VALUES (2, 'Integers (int), Floats (float) and Fractions (frac)', 'Integers (int), Fractions (frac) and Negatives (neg)', 'Floats (float), Decimals (dec) and Whole Numbers (whole)'),
(3, 'ice_cream = ["ice_cream = "vanilla", "strawberry", "pistachio", "chocolate"]', 'ice_cream = {"vanilla", "strawberry", "pistachio", "chocolate"}', 'ice_cream = ("vanilla", "strawberry", "pistachio", "chocolate")'),
(4, '.addition()', '.plus()', '.addon()'),
(5, 'cake = ["flavor": "coconut", "color": "white", "type": "layer cake"]', 'cake = {"flavor", "coconut", "color", "white", "type", "layer cake"}', 'cake = ("flavor": "coconut", "color": "white", "type": "layer cake")'),
(6, 'A tuple is a collection which is unchangeable and unordered.', 'A tuple is a collection which is changeable and ordered.', 'A tuple is a collection which is changeable and can be ordered or unordered, depending on how it is used.'),
(7, 'print(f"This is {word}")', 'print("This is {}".format(word))', 'print("This is " + word)'),
(8, '2.5', '3', '1'),
(9, 'Exponents', 'Multiplication', 'Division'),
(10, 'None', 'Eror', 'False'),
(11, '[0,1,2,3,4,5]', '[1,2,3,4,5]', '[1,2,3,4]'),
(12, '12_variable', ' ##variable', '__variable'),
(13, 'append()', 'get()', 'read()'),
(14, 'clear(),count()', 'append(),extend()', 'pop(),insert()'),
(15, 'List', 'Tuple', 'Strings'),
(16, '<>', '>>', '**'),
(17, 'Decoding', 'Serialising', 'Unpickling'),
(18, 'print(str[::])', 'print(reversed(str))', 'print(str[::1])'),
(19, '2', '0.5', '1'),
(20, 'None', 'Error', 'True'),
(21, '3', '-1', '0'),
(22, 'Discriminant', 'Indeterminate', 'Definite'),
(23, '"chilli
pepper
salt"', 'Complete', 'No output is generated'),
(24, 'No output is generated.', '"chilli
pepper
salt"', '"("chilli", 3)
("pepper", 2)
("salt", 1)
Complete."'),
(25, '"onion
garlic
chilli"', 'No output is generated.', '"salt
pepper
chilli
Complete."'),
(26, '12.0', 'Syntax Error', '0'),
(27, '6', '60', 'Syntax Error');

CREATE TABLE register(
f_name CHAR(50),
l_name CHAR(50),
email VARCHAR(100) UNIQUE,
password VARCHAR(20) ,
confirm_password VARCHAR(20));
