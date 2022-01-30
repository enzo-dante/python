# in chrome, access developer tools to 'inspect' html structure for webscraping
    # https://quotes.toscrape.com/

import requests # handle http requests
from bs4 import BeautifulSoup as bs # handle html
from random import choice
from csv import DictReader

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
READ_MODE = "r"
QUOTES_CSV_FILE = "quotes.csv"

description = ""
playing = True

def read_quotes(filename):
    with open(filename, READ_MODE) as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

read_quotes(QUOTES_CSV_FILE)
    
def start_game(quotes):
    remaining_guesses = 4
    guess = ""

    # choose random quote
    quote = choice(quotes)

    quote_text = quote[TEXT]
    print(f"Here's the quote: \n\n{quote_text}")

    author = quote[AUTHOR]
    print(f"\t-{author}")

    while guess.lower() != quote[AUTHOR].lower() and remaining_guesses > 0:
        guess = input(f"\nWho said this quote?\nGuesses remaining: {remaining_guesses}\n\n")
        remaining_guesses -= 1

        display_hint(guess, quote, remaining_guesses)

    again = ""

    while again.lower() not in (YES_SHORT, YES_LONG, NO_SHORT, NO_LONG):
        again = input("Would you like to play again? (y/n)?\t")

    if again.lower() in (YES_LONG, YES_SHORT):
        # return ends function but restarts game since it calls start_game()
        return start_game(quotes)
    else:
        print("ok, goodbye".upper())

def display_hint(guess, quote, remaining_guesses):
    href = quote[BIO_LINK]
    response = requests.get(f"{BASE_URL}{href}")

    bio_soup = bs(
        response.text,
        HTML_PARSER
    )

    author = quote[AUTHOR]
    birth_date = bio_soup.find(class_="author-born-date").get_text()
    birth_place = bio_soup.find(class_="author-born-location").get_text()
    # description = bio_soup.find(class_="author-description").get_text().split(".")[0]

    if guess.lower() == quote[AUTHOR].lower():
        print("\nyou got it right!".upper())

    # hint 1: href for author bio = BASE_URL + href
    elif remaining_guesses == 3:
        print("\nhint 1: ".upper() + f"\n\tThe author was born {birth_date}")

    # hint 2: first initial
    elif remaining_guesses == 2:
        author = quote[AUTHOR].split()
        first_initial = author[0][0]
        last_initial = author[-1][0]
        print("hint 2: ".upper() + f"\n\tThe author's initials are {first_initial}.{last_initial}.")

    # hint 3: first sentence of href bio
    elif remaining_guesses == 1:
        print()
        print("\nhint 3: ".upper() + f"\n\tThe author was born {birth_place}")

    else:
        print(f"\nSorry you ran out of guesses. The answer was {author[0]} {author[1]}")

quotes = read_quotes(QUOTES_CSV_FILE)
start_game(quotes)