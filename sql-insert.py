import sqlite3, random

with sqlite3.connect('newnum.db') as conn:
    
    #create cursor
    c = conn.cursor()
    
    c.execute('CREATE TABLE IF NOT EXISTS numbers(number INT)')
    
    for i in range(0,100):
        c.execute('INSERT INTO numbers VALUES(?)', (random.randint(0,100),))
        