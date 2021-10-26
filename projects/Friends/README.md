# SQLite commands

to run SQLite, execute:
sql3 

to view tables, execute:
.tables

to access database, execute:
.open {db_name}

to read a file with SQL code, execute:
.read {sql_file}

to read schema of table, execute:
.schema {table_name}

to break up long SQL queries, use triple quotes:

insert_query = '''INSERT INTO
                    friends(first_name,
                            last_name,
                            friendship)
                            VALUES ('Dante', 'Vernon', 3);'''

# SQLite datatypes

https://www.sqlite.org/datatype3.html

SQLite datatypes are different from other SQL data structures
- doesn't use date variables, have to store as string
- REAL is a floating point value
- TEXT is VARCHAR equivelent

