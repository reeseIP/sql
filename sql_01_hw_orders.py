# imports
import sqlite3

with sqlite3.connect('cars.db') as conn:

    c = conn.cursor()
    
    c.execute('CREATE TABLE IF NOT EXISTS orders(make TEXT, model TEXT, order_date DATE)')
    
    # create a cars table to insert into DB
    cars = [('Ford','Fusion','2020-11-11'),
            ('Ford','Expedition','2020-04-12'),
            ('Ford','Raptor','2020-03-13'),
            ('Honda','Civic','2020-03-23'),
            ('Honda','Accord','2020-02-01'),
            ('Ford','Fusion','2019-08-11'),
            ('Ford','Expedition','2019-04-23'),
            ('Ford','Raptor','2019-09-19'),
            ('Honda','Civic','2019-03-05'),
            ('Honda','Accord','2019-11-01'),
            ('Ford','Fusion','2018-05-17'),
            ('Ford','Expedition','2018-06-27'),
            ('Ford','Raptor','2018-09-19'),
            ('Honda','Civic','2017-06-05'),
            ('Honda','Accord','2017-02-01')]
    
    #c.executemany('INSERT INTO orders VALUES(?,?,?)', cars)
    
    c.execute('SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date FROM inventory INNER JOIN orders ON inventory.model = orders.model')

    data = c.fetchall()
    
    c.execute('SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date FROM inventory INNER JOIN orders ON inventory.model = orders.model')
        
    first_car = c.fetchone()
    
    car = (first_car[0]+first_car[1])
    
    print(f'Make: {first_car[0]}, Model: {first_car[1]}\nQuantity: {first_car[2]}')
    print(f'Order Date(s)')
    
    for row in data:
        if car == row[0]+row[1]:
            print(f'{row[3]}')
        else:
            car = row[0]+row[1]
            print(f'\nMake: {row[0]}, Model: {row[1]}\nQuantity: {row[2]}')
            print(f'Order Date(s)\n{row[3]}')