# import sqlite lib
import sqlite3

# NOTE: create a database in memory with 
# keep in mind that when the DB connection is closed it will disappear
# conn = sqlite3.connect(":memory:")

# establish connection with the database
conn = sqlite3.connect('new.db')

# create the cursor to interact with the database
cursor = conn.cursor()

# execute SQL and create table
cursor.execute("""CREATE TABLE IF NOT EXISTS population
                (city TEXT, state TEXT, population INT)""")
         
# close connection with the database         
conn.close()