'''
REQUIREMENTS

    dev inspect web page to identify html structure for web scraping

    GET data & save as a list:
        text of all quotes
        name of the author of the quote
        href of the link to person's bio

    handle pagination: use loop that extracts html element with url modifier and request new URL

GAME LOGIC

    pick & display 1 quote to player and ask the player who said the quote

    the player can guess 3 times until losing and being shown the correct answer

    after each incorrect guess, the player is shown a hint
        first hint has to make a request to author's bio page
        second hint is the first letter of the author's first name
        third hint displays first line of the author bio but has author's name redacted

    after win or loss, ask player if they want to play again loop

TDD (Test Driven Development)

    STEP 1: setup testing infrastructure

    STEP 2: write tests that you expect to FAIL
        run verbose tests: python3 tests.py -v
    
    STEP 3: write method implementation in activities.py and individually run tests
'''

# make sure to pip install these dependencies
from bs4 import BeautifulSoup # html extraction
from random import choice
import requests # requests url module

BASE_URL = "https://quotes.toscrape.com/"
NUM_GUESSES = 3
HINT_TWO = "The first letter of the author's first name is "
PLAY_AGAIN = "Would you like to play again?"
WIN_GAME = "Congratulations, you guessed correctly!"
LOSE_GAME = "You are out of guesses, the author of the quote was "


def get_all_quotes():
    pass

def get_random_quote():
    pass

def get_author_bio():
    pass

def get_author_name():
    pass

def handle_pagination():
    pass

def get_hint_one():
    pass

def get_hint_two():
    pass

def get_hint_three():
    pass

def get_win_msg():
    pass

def get_loss_msg():
    pass

