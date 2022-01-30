# in chrome, access developer tools to 'inspect' html structure for webscraping
    # https://quotes.toscrape.com/

import requests # handle http requests
from bs4 import BeautifulSoup as bs # handle html
from time import sleep # space out webscraping requests to avoid getting caught
from csv import DictWriter

# BeautifulSoup documentation
# print(help(soup))

AUTHOR = "author"
ANCHOR = "a"
BASE_URL = "https://quotes.toscrape.com/"
BIO_LINK = "bio-link"
HTML_PARSER = "html.parser"
HREF = "href"
NEXT = "next"
NO_LONG = "no"
NO_SHORT = "n"
YES_LONG= "yes"
YES_SHORT = "y"
QUOTE = "quote"
TEXT = "text"
QUOTES_CSV_FILE = "quotes.csv"
WRITE_MODE = "w"

description = ""
playing = True

def scrape_quotes():
    all_quotes = []
    url_endpoint = "/page/1"

    # handle pagination by accessing html body again and finding html element with 'next' class
    while url_endpoint:
        response = requests.get(f"{BASE_URL}{url_endpoint}")
        # print(f"please stand by as we web scrape:".upper())
        # print(f"{BASE_URL}{url_endpoint}\n")

        soup = bs(
            response.text,
            HTML_PARSER
        )

        # use module method .find with parameter that must be 'class_' to avoid python keyword error
        quotes = soup.find_all(class_=QUOTE)

        # inspect quote html structure to access specific fields
        # print(quotes[0])

        # loop through every quote and build a list of quotes with the text, author, and bio-link
        for quote in quotes:
            # .get_text() method will return only quote and not entire span html element

            all_quotes.append({
                TEXT: quote.find(class_=TEXT).get_text(),
                AUTHOR: quote.find(class_=AUTHOR).get_text(),
                BIO_LINK: quote.find_next(ANCHOR)[HREF]
            })

        # inspect quote html structure to find next button with URL endpoint for next page
        next_btn = soup.find(class_=NEXT)

        # re-assign URL endpoint for next iteration request call
            # if next button does not exist (reached end), break out of loop
        url_endpoint = next_btn.find(ANCHOR)[HREF] if next_btn else None

        # avoid overloading server and general detection
        sleep(1)

    return all_quotes

# WRITE quotes to csv file
def csv_write_quotes(quotes):
    with open(QUOTES_CSV_FILE, WRITE_MODE) as file:

        headers = [TEXT, AUTHOR, BIO_LINK]
        csv_writer = DictWriter(file, fieldnames=headers)

        csv_writer.writeheader() 
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
csv_write_quotes(quotes)