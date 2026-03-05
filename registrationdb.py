import mysql.connector as db_connector
from mysql.connector import Error


def createDB(db_name, host="localhost", user="root", password="root"):
    """This function creates a new database and take the following parameters:
    @param: db_name
    @param: host
    @param: user
    @param: password
    """
    # vars
    db_connection = None
    cursor = None
    try:
        # Sets up the connection
        db_connection = db_connector.connect(host=host, user=user, password=password)

        if db_connection.is_connected():
            print("Successfully Connected to MySQL database")

            # Query
            query = """CREATE DATABASE IF NOT EXISTS `%s`"""

            # Create cursor and execute query
            cursor = db_connection.cursor()
            cursor.execute(query, (db_name,))

            print(f"Table {db_name} created!")
    except Error as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if db_connection is not None and db_connection.is_connected():
            db_connection.close()


createDB("test_db_1")
createDB(db_name="test_db_1", password="my-password")