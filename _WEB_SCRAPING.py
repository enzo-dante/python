""" 
    ! WEB SCRAPING

        web scraping involves programmatically grabbing data from a web page

    * 3 steps:

        1. write python code to download html web page

        2. python code parses data and extracts desired data

        3. aggregate, store, manipulate, and analyze data


    ? BEST PRACTICES: web scraping 

        1. consult the robot.txt file to avoid legal issues

        2. when making requests, time them out

        3. if you are too aggressive, your IP can be blocked because some websites don't want you to web scrape their data


    ! Run python file

        to run the file, from the terminal, execute:

            python3 file_name.py

    ! SQLite database

        https://www.sqlite.org/datatype3.html

        SQLite datatypes are different from other SQL data structures

            doesn't use date variables, have to store as string

            REAL is a floating point value

            TEXT is VARCHAR equivalent

    ! SQLite commands

        ? to run SQLite

            sql3

        ? SQLite view tables

            .tables

        ? SQLite db access 

            .open {db_name}

        ? SQLite read a file with SQL code

            .read {sql_file}

        ? SQLite read schema of table

            .schema {table_name}
"""

# break up long SQL queries, use triple quotes:
insert_query = '''INSERT INTO
                    friends(first_name,
                            last_name,
                            friendship)
                            VALUES ('Dante', 'Vernon', 3);'''

""" 
    ! Beautiful Soup

        a python package that allows for extracting data from HTML with python

            beautiful soup does not download HTML, we need a requests module

    * Setup 

        in the terminal, execute:

            python3 -m pip install bs4

            python3 -m pip install requests
"""

from bs4 import BeautifulSoup

html_str = "<h1> Test </h1>"

"""
! parse html

    must be html.parser, and not xml.parser

"""
soup = BeautifulSoup(html_str, "html.parser")

# DOCUMENTATION
help(soup)

"""
! navigate parsed data

    Navigation options return an array
    - via tag

    ex:
    data = soup.body.contents
    print(data) # a list of items with new lines

    - using find - returns one matching tag
    - using find_all - returns a list of matching tags
            - to access a class attribute in HTML must use: class_=

    Navigating with CSS, execute syntax:

    - Select by id: #foo
    - Select by class: .bar
    - Select by attribute: [foo]
    - Select children: div > p
    - select descendents: div p
"""

# find an element with an id of foo
soup.find(id='foo')
soup.select('#foo')[0]

# find an element with a class of bar
soup.find_all(class_='bar')
soup.select('.bar')

# find all elements with a data attribute of baz
soup.find_all(attrs={'data-baz': True})
soup.select('[data-baz]')

# ! handle return data

# access the inner text in an element

el = soup.select('.special')[0]
print(el.get_text())

# name tag

for el in data:
        print(el.name)

# dictionary of attributes

attrs = soup.find('div').attrs
attrs = soup.find('div')['id']

# dictionary attributes values access using brackets

key_value = {soup.element}.attrs["key"]


