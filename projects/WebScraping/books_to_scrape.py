# make sure to pip install these dependencies 
import sqlite3 # database 
import requests # request url module
from bs4 import BeautifulSoup # html extraction

url = 'https://books.toscrape.com/catalogue/category/books/horror_31/index.html'

def get_price(book):
    # <div class=product price><p class=price color>
    # .select = css selector
    price = book.select('.price_color')[0].get_text()
    # remove strange symbols and convert to a float with 2 decimal points
    standard_price = round(float(price.replace("£","").replace("Â","")), 2)
    return standard_price

def get_rating(book):
    # <p class=star-rating One>
    # select returns and an array of 1 item
    stars = book.select('.star-rating')[0]
    # access attribute list and return number of stars string
    word_rating = stars.get_attribute_list('class')[-1]

    # define dictionary that will help convert num_stars string into an int
    ratings = {
        'Zero': 0,
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    # rating key will be used to return corresponding int value in ratings dictionary
    int_rating = ratings[word_rating]
    return int_rating

def save_books(book_collection):
    # establish connection to SQLite3 db or create new one
    connection = sqlite3.connect('books.db')
    # cursor handles SQL queries
    cursor = connection.cursor()
    # ''' allows for multi-line string
    # SQLite3 syntax: TEXT = VARCHAR, REAL = FLOAT, INTEGER = INT
    create_table_query = '''
    CREATE TABLE books(
        title TEXT,
        price REAL,
        rating INTEGER
    );
    '''

    # will throw an error if table aready exists, should define new method for handling this issue
    # cursor.execute(create_table_query)

    # bulk INSERT INTO books.db
    books_table = 'books'
    bulk_insert_query = f'''
    INSERT INTO {books_table}
    VALUES (?, ?, ?)
    '''
    cursor.executemany(bulk_insert_query, book_collection)

    # commit changes to books.db
    connection.commit()
    # close db connection
    connection.close()

def scrape_books(url):
    # 1. request URL: Beautiful Soup does not download HTML, we need a requests module
    res = requests.get(url)

    # 2. initialize BeautifulSoup: parse HTML webpage response from url request
    parser = BeautifulSoup(res.text, 'html.parser')

    # 3. extract desired data: select titles from parsed books response
    # inspect webpage (option+cmd+j on mac)
    # search (cmd+shift+c on mac) and select container element for book

    # return: <article class='product pod'>
    books = parser.find_all('article')
    book_collection = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        book_collection.append(book_data)
        print(book_collection)

    # 4. save data to SQLite3 database
    save_books(book_collection)

def get_title(book):
    # <h3><a title='x'>
    title = book.find('h3').find('a')['title']
    return title

scrape_books(url)

# 5. test SQL queries

# in terminal, execute: sql3 books.db

# in sql3 shell, execute: SELECT * FROM books;

# in sql3 shell, execute: SELECT title FROM books WHERE rating > 4;

# exit sql3 shell, execute: ctl+d
