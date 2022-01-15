# pip install requests module than import
import requests
# choice will take a list and pick 1 random item and return it
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 3000")
colored_header = colored(header, color="magenta")
print(colored_header)

# get user input
user_input = input("What would you like to search for? ")

# request json version of URL response with accepted headers
url = "https://icanhazdadjoke.com/search"
response = requests.get(
        url,
        headers={"Accept": "application/json"},
        # use params to add user_input as term in query string
        params={"term": user_input}
    ).json()

num_jokes = response["total_jokes"]
results = response["results"]

if num_jokes > 1:

    rand_joke = choice(results)
    print(f"There are {num_jokes} jokes!")
    print(rand_joke["joke"])

elif num_jokes == 1:

    print("There is only 1 joke")
    # since there is only 1 joke, looping through a list is ill-advised
    print(results[0]["joke"]) 

else:
    print(f"\nThere are no jokes with your search term: \n{user_input}")