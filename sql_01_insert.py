# import the sqlite3 lib
import sqlite3

# create connection with DB
with sqlite3.connect('new.db') as conn:

    # create the cursor to interact w/ DB
    cursor = conn.cursor()

    # list of populations by city
    populations = [
                   ('Boston', 'MA', 600000),
                   ('Chicago', 'IL', 2700000),
                   ('Houston', 'TX', 2100000),
                   ('Phoenix', 'AZ', 1500000),
                   ('Los Angeles', 'CA', 38000000),
                   ('Philadelphia', 'PA', 1500000),
                   ('San Antonio', 'TX', 1400000),
                   ('San Diego', 'CA', 130000),
                   ('Dallas', 'TX', 1200000),
                   ('San Jose', 'CA', 900000),
                   ('Jacksonville', 'FL', 800000),
                   ('Indianapolis', 'IN', 800000),
                   ('Austin', 'TX', 800000),
                   ('Detroit', 'MI', 700000)
                   ]
                   
    # execute SQL, insert entries
    cursor.executemany('INSERT INTO population VALUES(?,?,?)',
                        (populations))
                        