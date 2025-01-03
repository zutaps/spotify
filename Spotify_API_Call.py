import sqlite3 as s3

connection = s3.connect('test.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    )
''')

# Insert data into the table
cursor.execute('''
    INSERT INTO users (name, age, email)
    VALUES ('Alice', 30, 'alice@example.com')
''')
cursor.execute('''
    INSERT INTO users (name, age, email)
    VALUES ('Bob', 25, 'bob@example.com')
''')

# Commit the changes
connection.commit()

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()  # Fetch all rows from the result

# Print the results
for row in rows:
    print(row)
