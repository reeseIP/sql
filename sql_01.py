# import sqlite lib
import sqlite3

# establish connection with the database
conn = sqlite3.connect('new.db')

# create the cursor to interact with the database
cursor = conn.cursor()

# execute SQL and create table
cursor.execute("""CREATE TABLE IF NOT EXISTS population
                (city TEXT, state TEXT, population INT)""")
         
# close connection with the database         
conn.close()