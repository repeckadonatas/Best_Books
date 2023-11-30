import psycopg2
import db_config as dbc

"""
Context manager for working with database using this program.
Functions are accessed by using main.py file.
"""

class MyDatabase:

    def __init__(self):
        self.params = dbc.get_config()

    def __enter__(self):
        """
        Creates a connection to the database when main.py is run.
        :return: connection to a database and creation uf cursor object
        """
        self.conn = psycopg2.connect(**self.params)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the connection to the database once the program is terminated.
        :param exc_type: exception type
        :param exc_val: exception value
        :param exc_tb: exception traceback
        """
        print('\n')
        print('Connection closed')
        self.conn.close()
        if exc_val:
            raise

    def test_connection(self):
        """
        Testing connection with the database.
        :return: If successful, returns database version
                and connection parameters.
                Upon failure to connect, returns an error.
        """
        self.cursor.execute("""SELECT version()""")
        self.db_version = self.cursor.fetchone()
        print('PostgreSQL version:', self.db_version, '\n')
        print('PostgreSQL connection properties:', '\n', self.conn.get_dsn_parameters(), '\n')

    def create_table(self):
        """
        Creates a table in a database.
        Enter table name and column name(s) with datatype.
        """
        self.table_name = input('Enter a table name: ')
        self.col_type = input('Enter column names and data types: ')
        self.new_table = f"""CREATE TABLE IF NOT EXISTS 
            {self.table_name} ({self.col_type});"""

        self.cursor.execute(self.new_table)
        self.conn.commit()
        print('\n')
        print(f'Table {self.table_name} was created successfully.')

    def check_if_created(self):
        """
        Returns a list of tables in the connected database.
        """
        self.cursor.execute("""SELECT relname FROM pg_class 
                               WHERE relkind='r' 
                               AND relname !~ '^(pg_|sql_)';""")
        print('\n')
        print('Tables in the database:')
        print(self.cursor.fetchall())

    def trunc_table(self):
        """
        Truncates data in a table with provided table name.
        """
        self.table_name = input('Enter table name to truncate: ')
        self.cursor.execute(f"""TRUNCATE TABLE {self.table_name};""")
        self.conn.commit()
        print('\n')
        print(f'Table {self.table_name} was truncated!')

    def populate_table(self):
        """
        Populates a table with data.

        Opens a provided CSV file in memory and uses
        copy_expert() function in combination with
        COPY SQL statement to load data to the table.
        """
        self.table_name = input('Enter table to copy to: ')
        self.col_name = input('Enter column names: ')
        self.file_name = input('Enter CSV file to copy from: ')
        self.open_csv = open(f'output/2NF/{self.file_name}.csv', encoding='utf8')
        self.load_csv = f"""COPY {self.table_name} ({self.col_name})
                            FROM STDIN
                            WITH
                                DELIMITER ','
                                CSV HEADER;
                        """

        self.cursor.copy_expert(sql=self.load_csv, file=self.open_csv)
        self.conn.commit()
        print('\n')
        print('Copying CSV data!')

    def check_if_populated(self):
        """
        Checks the table to see if it was populated with data correctly.
        """
        self.table_name = input('Enter table name to check: ')
        self.cursor.execute(f'''SELECT * FROM {self.table_name} LIMIT 10;''')
        self.records = self.cursor.fetchmany(size=self.cursor.arraysize)
        print('\t')
        print(self.records)
