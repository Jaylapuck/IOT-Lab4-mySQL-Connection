import DBConfig as config
import regex as re

album_table = 'album'
review_table = 'review'
my_db_connection = config.connect()

# Create a cursor object
my_cursor = my_db_connection.cursor()


# select all from table, then print
def select_all_from_table(table_name):
    my_cursor.execute("SELECT * FROM " + table_name)
    my_result = my_cursor.fetchall()
    for row in my_result:
        print(row)


# select all by id , then print
def select_all_by_id(table_name, id):
    my_cursor.execute("SELECT * FROM " + table_name + " WHERE id = " + id)
    my_result = my_cursor.fetchall()
    for row in my_result:
        print(row)


# insert into table, then print
def insert_into_table(table_name, values):
    # get table fields
    my_cursor.execute("DESC " + table_name)
    my_result = my_cursor.fetchall()

    # print the first value in the array
    table_header_fields = []
    for row in my_result:
        if re.finditer('id', row[0]):
            table_header_fields.append(row[0])
        print(row[0])
    # insert into table
    add_employee = ("INSERT INTO " + album_table +
                    "(" + str(table_header_fields) + ") " +
                    ")VALUES (%s, %s, %s, %s)")

    my_cursor.execute(add_employee, values)
    my_db_connection.commit()


data_employee = ('The Beatles', 'Abbey Road', 'Rock', '10.99')
insert_into_table(album_table, data_employee)
select_all_from_table(album_table)
