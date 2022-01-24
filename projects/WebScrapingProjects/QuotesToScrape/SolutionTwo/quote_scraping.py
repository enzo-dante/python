# in chrome, access developer tools to 'inspect' html structure for webscraping
    # https://quotes.toscrape.com/

import requests # handle http requests
from bs4 import BeautifulSoup as bs # handle html
from time import sleep # space out webscraping requests to avoid getting caught
from random import choice

# BeautifulSoup documentation
# print(help(soup))

all_quotes = []
BASE_URL = "https://quotes.toscrape.com/"
url_endpoint = "/page/1"

# handle pagination by accessing html body again and finding html element with 'next' class
while url_endpoint:
    response = requests.get(f"{BASE_URL}{url_endpoint}")
    # print(f"please stand by as we web scrape:".upper())
    # print(f"{BASE_URL}{url_endpoint}\n")

    soup = bs(
        response.text, 
        "html.parser"
    )

    # use module method .find with parameter that must be 'class_' to avoid python keyword error
    quotes = soup.find_all(class_="quote")

    # inspect quote html structure to access specific fields
    # print(quotes[0])

    # loop through every quote and build a list of quotes with the text, author, and bio-link
    for quote in quotes:
        # .get_text() method will return only quote and not entire span html element

        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find_next("a")["href"]
        })

    # inspect quote html structure to find next button with URL endpoint for next page 
    next_btn = soup.find(class_="next")

    # re-assign URL endpoint for next iteration request call
        # if next button does not exist (reached end), break out of loop
    url_endpoint = next_btn.find("a")["href"] if next_btn else None

    # avoid overloading server and general detection
    # sleep(1)

# GAME LOGIC

remaining_guesses = 4
guess = ""

# choose random quote
quote = choice(all_quotes)

quote_text = quote["text"]
print(f"Here's the quote: \n\n{quote_text}")

author = quote["author"] # TESTING
print(f"\t-{author}")

while guess.lower() != quote["author"].lower():
    guess = input(f"\nWho said this quote?\nGuesses remaining: {remaining_guesses}\n\n")
    

print("after while loop".upper())