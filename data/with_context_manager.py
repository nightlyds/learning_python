import sqlite3

file = open('with.txt', 'w')
file.write('')
file.close()

with open('with.text', 'w') as file:
    file.write('')

# Modify __enter__ and __exit__ magic methods
class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise Exception(exc_type)

db = 'test.db'

with DataConn(db) as db:
    cursor = db.cursor()