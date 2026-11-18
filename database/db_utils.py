from database.connection import get_connection


def run_query(query, values=None):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(query, values or ())

    connection.commit()

    cursor.close()

    connection.close()


def run_select(query, values=None):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(query, values or ())

    rows = cursor.fetchall()

    cursor.close()

    connection.close()

    return rows