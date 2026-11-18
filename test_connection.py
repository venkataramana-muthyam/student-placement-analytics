from database.connection import get_connection

try:

    connection = get_connection()

    if connection.is_connected():

        print("Database Connected Successfully")

    connection.close()

except Exception as error:

    print(error)