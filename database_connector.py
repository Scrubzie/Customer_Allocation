import pyodbc

class DatabaseConnector:
    def __init__(self, connection_string):
        self.connection = pyodbc.connect(connection_string)
        self.cursors = []

    def __del__(self):
        for cursor in self.cursors:
            cursor.close()
        self.connection.close()

    def create_cursor(self):
        cursor = self.connection.cursor()
        self.cursors.append(cursor)
        return cursor