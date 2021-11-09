import mysql.connector
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()


# connect to database
def connect():
    print("Connecting to database...")

    # connect to database
    mysqldb = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PASSWORD'),
        database=os.environ.get('MYSQL_DB')
    )
    return mysqldb


# close the database
def close(my_db):
    print("Closing database...")
    if my_db.is_connected():
        my_db.close()
        print("Database connection closed.")


# check if the database is connected
def is_connected(my_db):
    if my_db.is_connected():
        print("Database connection established.")
    else:
        print("Database connection failed.")
