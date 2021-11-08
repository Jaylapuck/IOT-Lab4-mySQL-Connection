import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


# connect to database
def connect():
    print("Connecting to database...")

    # connect to database
    mysqldb = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PASSWORD'),
        database=os.environ.get('MYSQL_DATABASE')
    )
    return mysqldb


# close the database

def close(my_db):
    print("Closing database...")
    if my_db.is_connected():
        my_db.close()
        print("Database connection closed.")


# add a cursor
def select_all():
    my_db = connect()
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM album")
    my_result = my_cursor.fetchall()

    # print the result
    for x in my_result:
        print(x)

    close(my_db)
