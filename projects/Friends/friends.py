import sqlite3

# connect to existing/create new sqlite3 db
conn = sqlite3.connect('my_friends.db')

# define cursor that will handle SQL commands
c = conn.cursor()

# create friends table
# c.execute('CREATE TABLE friends(first_name TEXT, last_name TEXT, closeness INTEGER);')

# INSERT INTO db (superior scalability)
# using a ? for sql args in a tuple allows for clean readability 
# the number of ? have to align with the number of columns of the inserted data
# data = ('Steve', 'Kiwi', 2)
# insert_query = f'INSERT INTO friends(first_name, last_name, closeness) VALUES(?,?,?)'

# INSERT INTO db (high maintenance traditional)
# insert_query = '''INSERT INTO friends 
                                # VALUES('Bilbo', 'Baggins', 9);'''

# c.execute(insert_query, data)

# BULK INSERT INTO db

data = [
    ('Gary', 'Vernon', 79),
    ('Cathryn', 'Vernon', 23),
    ('Stone', 'Vernon', 47),
    ('Mojo', 'Vernon', 19),
    ('Prizzi', 'Vernon', 31),
]

insert_query = f'INSERT INTO friends (first_name, last_name, closeness) VALUES (?, ?, ?)'
# strictly insert method
# c.executemany(insert_query, data)

# alternative insert method that allows for dynamic manipulation
for p in data:
    c.execute(insert_query, p)

select_query = f'''SELECT * FROM friends 
                        WHERE closeness > 5 
                        ORDER BY closeness DESC'''

c.execute(select_query)

# select data as a list
print(c.fetchall())

# select first row from query
# print(c.fetchone())

# commit changes to db
conn.commit()

# terminate db connection
conn.close()