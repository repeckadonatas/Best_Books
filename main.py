from db_functions.db_functions import MyDatabase

"""
Run this file to perform actions on a database.
"""

if __name__ == '__main__':
    with MyDatabase() as db:
        print('Working with a database. For a list of commands, type "help". \n')

        help = ("To test a connection with a database: test \n"
                "To create a table: create \n"
                "To get the list of created tables: check \n"
                "To truncate a table: trunc \n"
                "To populate a table with data from a file: pop \n"
                "To check on populated table data: if pop \n"
                "To quit: exit")

        while True:
            user_input = input('Enter a command: ')
            user_input = user_input.strip()
            user_input = user_input.lower()

            if user_input.startswith('test'):
                db.test_connection()

            elif user_input.startswith('create'):
                db.create_table()
                continue

            elif user_input.startswith('check'):
                db.check_if_created()
                continue

            elif user_input.startswith('trunc'):
                db.trunc_table()
                continue

            elif user_input.startswith('pop'):
                db.populate_table()
                continue

            elif user_input.startswith('if pop'):
                db.check_if_populated()
                continue

            elif user_input.startswith('help'):
                print(help, '\n')
                continue

            elif user_input.startswith('exit'):
                break

            else:
                print('Unknown command. For the list of commands type "help" \n')
                continue
