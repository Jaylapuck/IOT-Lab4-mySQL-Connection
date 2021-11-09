import DBConfig as config


# select all from table, then print
def select_all_from_table(table_name):
    my_db_connection = config.connect()
    my_cursor = my_db_connection.cursor()

    query = "SELECT * FROM " + table_name
    my_cursor.execute(query)
    my_result = my_cursor.fetchall()
    for row in my_result:
        print(row)
    config.close(my_db_connection)


# select all by id , then print
def select_by_id(table_name, table_id):
    my_db_connection = config.connect()
    my_cursor = my_db_connection.cursor()

    my_fields = get_table_fields(table_name)
    my_id = my_fields[0]
    query = "SELECT * FROM " + table_name + " WHERE " + my_id + " = " + str(table_id)
    my_cursor.execute(query)
    my_result = my_cursor.fetchall()
    for row in my_result:
        print(row)
    config.close(my_db_connection)


# insert into table, then print
def insert_into_table(table_object: object):
    my_db_connection = config.connect()
    my_cursor = my_db_connection.cursor()

    # get table fields
    table = table_object.__class__.__name__.upper()
    my_fields = get_table_fields(table)
    print(my_fields)

    # insert into table
    query = "INSERT INTO " + table + " ("
    for field in my_fields:
        query += field + ", "
    query = query[:-2] + ") VALUES ("
    for field in my_fields:
        query += "'" + str(getattr(table_object, field)) + "', "
    query = query[:-2] + ")"
    print(query)
    my_cursor.execute(query)
    my_db_connection.commit()
    config.close(my_db_connection)


# insert into table with parameters, then print
def insert_into_table_with_parameters(table_object: object):
    data = ""
    my_db_connection = config.connect()
    my_cursor = my_db_connection.cursor()

    add_row = "INSERT INTO " + table_object.__class__.__name__.upper() + " ("
    for field in table_object.__dict__:
        add_row += field + ", "
    add_row = add_row[:-2] + ") VALUES ("

    for field in table_object.__dict__:
        add_row += "%(" + field + ")s, "
    add_row = add_row[:-2] + ")"

    data = table_object.__dict__

    my_cursor.execute(add_row, data)
    my_db_connection.commit()
    config.close(my_db_connection)


def delete_by_id(table_name, table_id):
    my_db_connection = config.connect()
    my_cursor = my_db_connection.cursor()

    my_fields = get_table_fields(table_name)
    my_id = my_fields[0]
    query = "DELETE FROM " + table_name + " WHERE " + my_id + " = " + str(table_id)
    my_cursor.execute(query)
    my_db_connection.commit()
    config.close(my_db_connection)


def get_table_fields(table_name):
    my_db_connection = config.connect()
    my_cursor = my_db_connection.cursor()

    my_cursor.execute("DESC " + table_name)
    my_result = my_cursor.fetchall()
    table_header_fields = []
    for row in my_result:
        table_header_fields.append(row[0])

    config.close(my_db_connection)
    return table_header_fields
