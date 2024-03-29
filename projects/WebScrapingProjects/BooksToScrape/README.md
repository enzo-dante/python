# run file

to run the file, from the terminal, execute:

        python3 file_name.py

# web scraping

web scraping involves programmatically grabbing data from a web page

__3 steps:__

1. write python code to download html web page

2. python code parses data and extracts desired data

3. aggregate, store, manipulate, and analyze data

# web scraping best practices

1. consult the robot.txt file to avoid legal issues

        Craigslist Inc. vs 3Taps Inc. case

2. if making requests, time them out

3. if you are too aggressive, your IP can be blocked because some websites don't want you to webscrape their data

# beautiful soup (bs4)

beautiful soup is a python package that allows for extracting data from HTML with python. bs4 does not download HTML, we need a requests module

download Beautiful Soup and Requests package using PIP

in the terminal, execute:

        python3 -m pip install bs4

        python3 -m pip install requests


# bs4 documentation

beautiful soup documentation in python, execute:

soup = BeautifulSoup(html, 'html.parser')
help(soup)

__beautiful soup process__

1. parse (must be html.parser, and not xml.parser)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

2. navigate parsed data

Navigation options return an array via tag

        ex:

        data = soup.body.contents
        print(data) # a list of items with new lines

returns one matching tag
        .find()

returns a list of matching tags
        .find_all()

to access a class attribute in HTML
        .find(class_="placeholder")

Navigating with CSS, execute syntax:

- Select by id:
        #foo
- Select by class:
        .bar
- Select by attribute:
        [foo]
- Select children:
        div > p
- select descendents:
        div p

__find an element with an id of foo__
soup.find(id='foo')
soup.select('#foo')[0]

__find an element with a class of bar__
soup.find_all(class='bar')
soup.select('.bar')

__find all elements with a data attribute of baz__
soup.find_all(attrs={'data-baz: True})
soup.select('[data-baz]')

3. handle return data

accessing data in elements:

- get_text(): access the inner text in an element

        el = soup.select('.special')[0]
        print(el.get_text())

- .name

        for el in data:
                print(el.name)

- attrs 
        - dictionary of attributes
        - you can also access attribute values using brackets

        attrs = soup.find('div').attrs
        attrs = soup.find('div')['id']

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