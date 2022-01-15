import requests

# search endpoint to programatically get jokes
url = "https://icanhazdadjoke.com/search"

response = requests.get(
        url,
        # get json version
        headers={"Accept": "application/json"},
        # review websites api documentation for specific domain params
            # equivalent: https://icanhazdadjoke.com/search?term=cat&limit=1
        params={
            "term": "cat",
            "limit": 1
        }
    )

# when header accepts json response
    # takes json and converts into python dictionary

json_data = response.json()

# print(json_data) # review data structure
print(json_data["results"])
