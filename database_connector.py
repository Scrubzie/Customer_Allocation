import pyodbc
import os

class DatabaseConnector:
    def __init__(self):
        self.connection_string = os.getenv('QuantumTestString')
        self.connection = pyodbc.connect(self.connection_string)
        self.cursors = []

    def __del__(self):
        for cursor in self.cursors:
            cursor.close()
        self.connection.close()
    
    def create_cursor(self):
        cursor = self.connection.cursor()
        self.cursors.append(cursor)
        return cursor
    
    def close_cursor(self, cursor):
        position = self.cursors.index(cursor)
        self.cursors.pop(position)
        cursor.close()

    def close_all_cursors(self):
        for cursor in self.cursors:
            cursor.close()