# imports
import sqlite3

# connect to DB
with sqlite3.connect('cars.db') as conn:
    
    # create the cursor
    c = conn.cursor()
    
    # create a cars table to insert into DB
    cars = [('Ford','Fusion',15),
            ('Ford','Expedition',20),
            ('Ford','Raptor',10),
            ('Honda','Civic',20),
            ('Honda','Accord',25)]
    '''        
    # execute SQL
    c.executemany('INSERT INTO inventory VALUES(?,?,?)', (cars))
   
    # do some updates
    c.execute("UPDATE inventory SET quantity = 25 WHERE model = 'Raptor'")
    c.execute("UPDATE inventory SET quantity = 30 WHERE model = 'Accord'")
    '''
    c.execute('SELECT * FROM inventory WHERE make = "Ford"')
    
    car_fetch = c.fetchall()
    
    for row in car_fetch:
        print(f'{row[0]} | {row[1]} | {row[2]}')
        

    