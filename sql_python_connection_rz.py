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


def get_question(question_number):
    try:
        db_name = "Nano_Degree_Game_1"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to database")

        query = f"""SELECT question FROM Questions WHERE Q_Number={question_number}"""
        cur.execute(query)

        result = (
            cur.fetchone()
        ) 
        for i in result:
            question = i
            # print(question)

        cur.close()
        return question

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def get_correct_answer(question_number):
    try:
        db_name = "Nano_Degree_Game_1"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to database")

        query = f"""SELECT Answer FROM Questions WHERE Q_Number={question_number}"""
        cur.execute(query)

        result = (
            cur.fetchone()
        ) 
        correct_answer = result[0]

        cur.close()
        return correct_answer

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def get_incorrect_answers(question_number):
    try:
        db_name = "Nano_Degree_Game_1"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to database")

        query = f"""SELECT incorrect_answer_1, incorrect_answer_2, incorrect_answer_3 FROM multiple_choice WHERE Q_Number={question_number}"""
        cur.execute(query)

        result = (
            cur.fetchall()
        ) 

        for i in result:
            incorrect_answer_1 = i[0]
            incorrect_answer_2 = i[1]
            incorrect_answer_3 = i[2]
            incorrect_answers = [incorrect_answer_1, incorrect_answer_2, incorrect_answer_3]

        cur.close()
        return incorrect_answers

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def get_question_count():
    try:
        db_name = "Nano_Degree_Game_1"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to database")

        cur.execute("SELECT count(*) FROM Questions")    
        question_count = cur.fetchone()[0]

        cur.close()
        return question_count

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

if __name__ == "__main__":

    _connect_to_db("Nano_Degree_Game_1")
    print(get_question(1))
    print("*********")
    print(get_correct_answer(1))
    print("*********")
    print(get_incorrect_answers(1))
    # get_question_count()


