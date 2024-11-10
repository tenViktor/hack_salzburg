import sqlite3
from sqlite3 import Error

"""File for navigating sqlite3"""

class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.db_file = db_file
        self.conn = self.create_connection()


    def create_connection(self) -> sqlite3.connect:
        """Create a connection to the database."""
        try:
            conn = sqlite3.connect(self.db_file)
            print(f"Connected to database: {self.db_file}")
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None


    def create_table(self, table_name, columns):
        """
        Create a table with the given name and columns.
        
        :param table_name: Name of the table to create
        :param columns: Dictionary of column names and types
        """
        try:
            column_definitions = ", ".join([f"{col} {col_type}" for col, col_type in columns.items()])
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
            self.conn.execute(query)
            self.conn.commit()
            print(f"Table '{table_name}' created successfully.")
        except Error as e:
            print(f"Error creating table '{table_name}': {e}")


    def insert_data(self, table_name, data):
        """
        Insert data into the table.
        
        :param table_name: Name of the table to insert data into
        :param data: Dictionary of column names and values
        """
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join("?" for _ in data)
            values = tuple(data.values())
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.conn.execute(query, values)
            self.conn.commit()
            print(f"Data inserted into '{table_name}' successfully.")
        except Error as e:
            print(f"Error inserting data into '{table_name}': {e}")


    def fetch_data(self, table_name, condition= None, condition_param= None):
        """
        Fetch all data from the specified table.
        
        :param table_name: Name of the table to fetch data from
        :param data: selective fetching where data falls under specific condition
        :return: List of rows fetched from the table
        """
        try:
            query = f"SELECT * FROM {table_name}"
            if condition != None:    
                query += f" WHERE {condition}"
            cursor = self.conn.cursor()
            cursor.execute(query, condition_param)
            rows = cursor.fetchall()
            print(f"Data fetched from '{table_name}': {rows}")
            return rows
            
        except Error as e:
            print(f"Error fetching data from '{table_name}': {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

