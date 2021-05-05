import sqlite3

connection = sqlite3.connect('data_bases.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS persons (
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
""")

cursor.execute("""
    INSERT INTO persons VALUES
    ('Person', '1', 1),
    ('Person', '2', 2),
    ('Person', '3', 3)
""")

cursor.execute("""
    SELECT * FROM persons
    WHERE first_name = 'Person'
""")

rows = cursor.fetchall()

print(rows)

connection.commit()
connection.close()