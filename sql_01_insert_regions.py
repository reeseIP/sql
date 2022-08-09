# imports 
import sqlite3

# connect to DB
with sqlite3.connect('new.db') as conn:

    # create the cursor
    c = conn.cursor()
    
    # create table in DB
    c.execute('CREATE TABLE IF NOT EXISTS regions(city TEXT, region TEXT)')
    
    # create a list of cities by region
    cities = [
              ('New York City', 'Northeast'),
              ('San Francisco', 'West'),
              ('Chicago', 'Midwest'),
              ('Houston', 'South'),
              ('Phoenix', 'West'),
              ('Boston', 'Northeast'),
              ('Los Angeles', 'West'),
              ('Houston', 'South'),
              ('Philadelphia', 'Northeast'),
              ('San Antonio', 'South'),
              ('San Diego', 'West'),
              ('Dallas', 'South'),
              ('San Jose', 'West'),
              ('Jacksonville', 'South'),
              ('Indianapolis', 'Midwest'),
              ('Austin', 'South'),
              ('Detroit', 'Midwest')
             ]
             
    # insert entries into table
    c.executemany('INSERT INTO regions VALUES(?,?)', (cities))
   
    c.execute('SELECT * FROM regions ORDER BY region ASC')
    
    data = c.fetchall()
    
    for row in data:
        print(f'{row[0]} | {row[1]}')