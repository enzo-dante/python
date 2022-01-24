'''
REQUIREMENTS

    dev inspect web page to identify html structure for web scraping

    GET data & save as a list:
        all quotes (html - class="quote")
            text of individual quote (html - class="text")
        name of the author of the quote (html - class="author")
        href of the link to person's bio (html - href="/author/Albert-Einstein")

        use BeautifulSoup's methods:
            {element}.get_text() to get inner text of html element
            {soup.element}.attrs[key]

    handle pagination: use loop that extracts html element with url modifier and request new URL

GAME LOGIC

    pick & display 1 quote to player and ask the player who said the quote

    the player can guess 3 times until losing and being shown the correct answer

    after each incorrect guess, the player is shown a hint
        first hint has to make a request to author's bio page
            class="author-details"
        second hint is the first letter of the author's first name
        third hint displays first line of the author bio but has author's name redacted
            class="author-details"

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

BASE_URL = "https://quotes.toscrape.com"
HINT_TWO = "The first letter of the author's first name is "
PLAY_AGAIN = "\nWould you like to play again? Y or N\n"
WIN_GAME = "\nCongratulations, you guessed correctly!"
LOSE_GAME = "\nYou are out of guesses, the author of the quote was "
QUOTE_PROMPT = "\nCan you correctly guess who said this?\n"
GUESS_AGAIN = "\nGuess again!\n"
HINT_PREFIX = "\nHINT ?:\n"
HTML_PARSER = "html.parser"
JSON_HEADERS={"Accept": "application/json"}

all_quotes = []
random_quote = {}

def get_all_quotes():

    # reset list of quotes
    all_quotes = []
    url = BASE_URL

    while True:
        response = requests.get(
                url,
                # get json version of HTML for list of quotes(element that has a class quote)
                JSON_HEADERS
            )

        # extract html from response with specified html.parser
        soup = BeautifulSoup(
                response.text,
                HTML_PARSER
            )

        quotes = soup.find_all(class_="quote")

        # loop over list of html quote elements
        for quote in quotes:

            '''
            use BeautifulSoup's methods:
                {element}.get_text() to get inner text of html element
                {soup.element}.attrs[key]
            '''

            all_quotes.append({
                    "text": quote.find(class_="text").get_text(),
                    "author": quote.find(class_="author").get_text(),
                    "href": quote.find_next("a").attrs["href"]
                })


        url = handle_pagination(soup)

        if url is None: break

    return all_quotes

def handle_pagination(soup):

    next_btn = soup.find(class_="next")

    if next_btn is None:
        return None

    next_page_url= BASE_URL + next_btn.find_next("a").attrs["href"]
    return next_page_url

def get_random_quote():
    return choice(get_all_quotes())

def get_author_details(random_quote):

    bio_url = BASE_URL + random_quote["href"]

    bio_response = requests.get(
        bio_url,
        JSON_HEADERS
    )

    bio_soup = BeautifulSoup(
        bio_response.text,
        HTML_PARSER
    )

    author_details = bio_soup.find(class_="author-details")

    strong = author_details.find("strong").get_text()
    birth_date = author_details.find(class_="author-born-date").get_text()
    birth_location = author_details.find(class_="author-born-location").get_text()

    description = author_details.find(class_="author-description").get_text()

    return {
        "bio": f"{strong} {birth_date} {birth_location}",
        "description": description,
    }

def get_hint_one(author_details):

    hint_one = HINT_PREFIX.replace("?", "1") + author_details["bio"]
    print(hint_one)

def get_hint_two(author):

    first_letter = author[0]
    hint_two = HINT_PREFIX.replace("?", "2") + HINT_TWO + first_letter
    print(hint_two)

def get_hint_three(author_details, author):

    descriptions = author_details["description"].strip().split(".")

    hint_three = HINT_PREFIX.replace("?", "3") + descriptions[1].strip().replace(author.split(" ")[0], "?").replace(author.split(" ")[-1], "?")
    print(hint_three)

def get_win_msg():

    print(WIN_GAME)

def get_loss_msg(random_quote):

    author = random_quote["author"]
    print(LOSE_GAME + author)

def reset_game():

    num_guesses = 0
    random_quote = get_random_quote()
    user_input = None
    author_details = None
    return num_guesses, random_quote, user_input, author_details

def start_game():

    is_testing = False
    num_guesses, random_quote, user_input, author_details = reset_game()

    while num_guesses < 4 and num_guesses >= 0:

        author = random_quote["author"]
        quote = "\n" + random_quote["text"] + "\n"

        if is_testing is True:
            print(quote + "\t-" + author)
        else:
            print(quote)

        if num_guesses == 0:

           user_input = input(QUOTE_PROMPT)
           num_guesses += 1

        if user_input.strip() != author and num_guesses == 3:

            get_hint_three(author_details, author)
            user_input = input(GUESS_AGAIN)
            num_guesses += 1

        elif user_input.strip() != author and num_guesses == 2:

            num_guesses += 1
            get_hint_two(author)
            user_input = input(GUESS_AGAIN)

        elif user_input.strip() != author and num_guesses == 1:

            num_guesses += 1
            author_details = get_author_details(random_quote)
            get_hint_one(author_details)
            user_input = input(GUESS_AGAIN)

        elif user_input.strip() == author:

            get_win_msg()

            user_input = input(PLAY_AGAIN).lower().strip()

            if user_input != "y":
                break

            print("\n---\n")

            num_guesses, random_quote, user_input, author_details = reset_game()

    else:

        get_loss_msg(random_quote)

        user_input = input(PLAY_AGAIN).lower().strip()

        if user_input == "y":
            print("\n---\n")
            start_game()

start_game()