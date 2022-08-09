# imports
import csv
import sqlite3

# establish connection w/ DB
with sqlite3.connect('new.db') as conn:
    
    # create the cursor object
    c = conn.cursor()
    
    # open the csv file and assign it to a variable
    employees = csv.reader(open('employees.csv','rU'))
    
    # create the employees table
    c.execute('CREATE TABLE IF NOT EXISTS employees(firstname TEXT, lastname TEXT)')
    
    # insert entries into table from csv
    c.executemany('INSERT INTO employees VALUES(?,?)', (employees))