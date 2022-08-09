import sqlite3

with sqlite3.connect('newnum.db') as conn:

    c = conn.cursor()
    
    prompt = '''
        Select the operation that you want to perform [1-5]:
        1. Average
        2. Max
        3. Min
        4. Sum
        5. Exit\n'''
        
    while True:
        
        # get selection from user input
        selection = input(prompt)
        
        if selection in set(['1','2','3','4']):
        
            # build a table of operations based on selection
            operations = {1:'avg',2:'max',3:'min',4:'sum'}[int(selection)]
            
            # execute sql with given operation
            c.execute('SELECT {}(number) FROM numbers'.format(operations))
            
            data = c.fetchone()
            
            print(operations + ': %f' % data[0])
            
        elif selection == '5':
        
            print('exit')
            break

        else:
        
            print('Please enter a valid selection')