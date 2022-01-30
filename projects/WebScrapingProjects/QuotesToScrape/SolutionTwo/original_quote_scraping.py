# in chrome, access developer tools to 'inspect' html structure for webscraping
    # https://quotes.toscrape.com/

import requests # handle http requests
from bs4 import BeautifulSoup as bs # handle html
from time import sleep # space out webscraping requests to avoid getting caught
from random import choice

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

        if guess.lower() == quote[AUTHOR].lower():
            print("\nyou got it right!".upper())

        # hint 1: href for author bio = BASE_URL + href
        elif remaining_guesses == 3:
            href = quote[BIO_LINK]
            response = requests.get(f"{BASE_URL}{href}")

            bio_soup = bs(
                response.text,
                HTML_PARSER
            )

            birth_date = bio_soup.find(class_="author-born-date").get_text()
            birth_place = bio_soup.find(class_="author-born-location").get_text()
            # description = bio_soup.find(class_="author-description").get_text().split(".")[0]

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

    again = ""

    while again.lower() not in (YES_SHORT, YES_LONG, NO_SHORT, NO_LONG):
        again = input("Would you like to play again? (y/n)?\t")

    if again.lower() in (YES_LONG, YES_SHORT):
        # return ends function but restarts game since it calls start_game()
        return start_game(quotes)
    else:
        print("ok, goodbye".upper())

quotes = scrape_quotes()
start_game(quotes)