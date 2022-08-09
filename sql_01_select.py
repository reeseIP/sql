#imports
import sqlite3

with sqlite3.connect('new.db') as conn:
    
    # create the cursor
    c = conn.cursor()
    
    # select records from the DB
    c.execute('SELECT firstname, lastname FROM employees')
    
    # make a list of the DB records
    employees = c.fetchall()
    
    # output the records
    for row in employees:
        print(f'{row[0]}, {row[1]}')
    
    