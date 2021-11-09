import sys

from Models.Album import Album
from Models.Review import Review
import DBHandler as dbHandler


# select all from table
# dbHandler.select_all_from_table('album')
# dbHandler.select_all_from_table('review')

# select by id
# dbHandler.select_by_id('album', 1)
# dbHandler.select_by_id('review', 1)

# insert into table
# dbHandler.insert_into_table(Album('The Beatles', 'Abbey Road', 'Rock', '10.99'))
# dbHandler.insert_into_table(Review('Worst Album Ever', 'Title says it all', 5, 3))

# menu for db Handler
def menu():
    while True:
        table_response = input("Pick a table: ")
        option_response = input("Pick an option: ")
        if option_response == '1':
            dbHandler.select_all_from_table(table_response)
        elif option_response == '2':
            dbHandler.select_by_id(table_response, input("Enter id"))
        elif option_response == '3':
            if table_response == 'album':
                dbHandler.insert_into_table(
                    Album(input("Enter artist"), input("Enter title"), input("Enter genre")))
            elif table_response == 'review':
                dbHandler.insert_into_table(
                    Review(input("Enter title"), input("Enter review"), input("Enter rating"), input("Enter album_id")))
        elif option_response == '4':
            dbHandler.delete_by_id(table_response, input("Enter id"))
        elif option_response == '5':
            dbHandler.close_connection()
            sys.exit()


menu()
