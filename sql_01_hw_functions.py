import sqlite3

with sqlite3.connect('cars.db') as conn:
    
    c = conn.cursor()
    
    c.execute('SELECT make, model, quantity FROM inventory')
    
    #c.execute('SELECT count(order_date) FROM orders')
    
    data = c.fetchall()
    
    for row in data:
        c.execute('SELECT count(order_date) FROM orders WHERE make =? AND model =?',  (row[0], row[1]))
        count = c.fetchone()
        
        print(f'Make: {row[0]}, Model: {row[1]} \nQuantity: {row[2]} \nOrder(s): {count[0]}')