import pyodbc

class DatabaseConnector:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.cursor = pyodbc.connect(self.connection_string).cursor()

    def get_cursor(self):
        return self.cursor
    