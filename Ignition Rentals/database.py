import sqlite3
conn = sqlite3.connect('ignition.db')
curr = conn.cursor()

#creating tables for the database
curr.execute('''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        u_name TEXT,
        pass TEXT,
        tag TEXT
    )
''')

curr.execute('''
    CREATE TABLE IF NOT EXISTS employee(
        e_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        join_date DATE,
        salary INTEGER,
        n_clients INTEGER
    )
''')

curr.execute('''
    CREATE TABLE IF NOT EXISTS customer(
        c_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        bike TEXT,
        no_of_days INTEGER,
        payment INTEGER
    )
''')

curr.execute('''
    CREATE TABLE IF NOT EXISTS bikes(
        b_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        model_no INTEGER,
        price INTEGER,
        stock INTEGER
    )
''')

curr.execute(
    '''
    INSERT INTO bikes VALUES(NULL, 'DODGE TOMAHAWK', 51, 80000, 5)
    '''
)
curr.execute(
    '''
    INSERT INTO bikes VALUES(NULL, 'SUZUKI HAYABUSA', 69, 76000, 5)
    '''
)
curr.execute(
    '''
    INSERT INTO bikes VALUES(NULL, 'MTT TURBINE SUPERBIKE Y2K', 328, 76000, 7)
    '''
)
curr.execute(
    '''
    INSERT INTO bikes VALUES(NULL, 'KAWASAKI NINJA H2R', 67, 54000, 10)
    '''
)

# Commit changes and close the connection
conn.commit()
conn.close()