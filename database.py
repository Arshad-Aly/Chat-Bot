import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="au_bot"
)


def syb_sub(sem:int, sub):
    cursor = cnx.cursor(buffered=True)

    query = f"SELECT subject_name FROM semestersubjects WHERE LEFT(subject_id, 1) IN (%s) AND RIGHT(subject_id, 1) IN ({sub});"
    cursor.execute(query, (sem,))

    result = cursor.fetchone()[0]

    cursor.close()

    return result

def get_stu_mid1result(roll_number: str , sub, exam):
    cursor = cnx.cursor(buffered=True)

    query = f"SELECT {sub} FROM {exam} WHERE roll_number = %s;"
    cursor.execute(query, (roll_number,))

    result = cursor.fetchone()[0]

    cursor.close()

    return result


def check_stuID(roll_number:str):
    cursor = cnx.cursor(buffered=True)

    query = f"SELECT student_name FROM students WHERE roll_number = %s;"
    cursor.execute(query, (roll_number,))

    result = cursor.fetchone()

    cursor.close()

    if result is not None:
        return result[0]
    else:
        return None
def get_stu_subName(sub_id):
    cursor = cnx.cursor(buffered=True)

    query = f"SELECT subject_name FROM semestersubjects WHERE subject_id = {sub_id};"
    cursor.execute(query)

    result = cursor.fetchone()[0]

    cursor.close()

    return result
