# get the sqlite3 lib
import sqlite3

# create the database connection
conn = sqlite3.connect('cars.db')

# create the cursor to interact w/ DB
cursor = conn.cursor()

# execute SQL
cursor.execute('''CREATE TABLE IF NOT EXISTS cars 
                (make TEXT, model TEXT, quantity INT)''')
     
# close the connection to DB     
conn.close()