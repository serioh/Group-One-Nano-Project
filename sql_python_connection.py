import mysql.connector
from config import USER, PASSWORD, HOST
from pprint import pp


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=db_name,
    )
    return cnx


def get_all_questions():
    try:
        db_name = "Nano_Degree_Game_1"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to database")

        query = """SELECT question FROM Questions"""
        cur.execute(query)

        result = (
            cur.fetchall()
        ) # this is a list with db records where each record is a tuple


        ## or use fetchmany() to specify how many rows we want back
        # while True:
        #     results = cur.fetchmany(10)
        #     if not results:
        #         break
        #     print(results)
        for i in result:
            question = "i"
            print(question)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def get_correct_answer():
    try:
        db_name = "Nano_Degree_Game_1"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to database")

        query = """SELECT Answer FROM Questions"""
        cur.execute(query)

        result = (
            cur.fetchall()
        ) # this is a list with db records where each record is a tuple


        ## or use fetchmany() to specify how many rows we want back
        # while True:
        #     results = cur.fetchmany(10)
        #     if not results:
        #         break
        #     print(results)

        for i in result:
            correct_answer = i
            print(correct_answer)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def get_incorrect_answers():
    try:
        db_name = "Nano_Degree_Game_1"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to database")

        query = """SELECT incorrect_answer_1, incorrect_answer_2, incorrect_answer_3 FROM multiple_choice"""
        cur.execute(query)

        result = (
            cur.fetchall()
        ) # this is a list with db records where each record is a tuple


        ## or use fetchmany() to specify how many rows we want back
        # while True:
        #     results = cur.fetchmany(10)
        #     if not results:
        #         break
        #     print(results)

        for i in result:
            incorrect_answer_1 = i[0]
            incorrect_answer_2 = i[1]
            incorrect_answer_3 = i[2]
            print(incorrect_answer_1, incorrect_answer_2, incorrect_answer_3)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


_connect_to_db("Nano_Degree_Game_1")
get_all_questions()
get_correct_answer()
get_incorrect_answers()


