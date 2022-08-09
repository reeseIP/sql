# imports
import sqlite3

# connect to DB
with sqlite3.connect('new.db') as conn:
    
    # create the cursor
    c = conn.cursor()
    
    c.execute('SELECT population.city, population.population, regions.region FROM population, regions    WHERE population.city = regions.city ORDER BY population.population ASC')   
    
    data = c.fetchall()
    
    for row in data:
        print(f'\nCity: {row[0]}\nPopulation: {str(row[1])}\nRegion: {row[2]}')