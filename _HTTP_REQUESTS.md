# internet process

> DNS lookup: get an ip address for a domain name/website URL

> computer/client makes a REQUEST to a server

> server processes that request

> server's response is compiling website

# REQUEST/RESPONSE cycle

> the requests & responses contain HTTP Headers, additional metadata for both request and responses

accept: acceptable content-types for response

cache-control: specify caching behavior

user-agent: information about the software used to make the request

# response status codes

2xx - success
3xx - redirect
4xx - client error (user fault)
5xx - server error (not user fault)

# HTTP verbs: GET & POST

> GET

useful for retrieving data
data passed in query string
should have no "side-effects"
can be cached
can be bookmarked

> POST

useful for writing data
data passed in request body
can have "side-effects"
not cached
cannot be bookmarked

# api (application programming interface)

> a version of a website intended for computers to communicate with one another with code

apis allows users to get data from another application without needing to understand how that application functions

apis can often send data back in different formats: JSON or XML

# requests Module

> requests is a popular external module for handling https requests

__in terminal, execute:__

python3 -m pip install requests

> example 1: http request

import requests

url = "https://www.google.com"
response = requests.get(url)

print(response.ok) # True

print(f"your request to {url} came back w/ status code {response.status_code}")

print(response.text) # html source

# JSON requests w/ headers

> request header

import requests

response = requests.get(
    "http://www.example.com",
    headers={
        "header1": "value1",
        "header2": "value2"
    }
)

> request headers boilerplate

import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(
        url,
        # get plain text version
        # just joke for this URL, but not all URLs are have plain text headers setup
        # headers={"Accept": "text/plain"}

        # get html version
        # headers={"Accept": "text/html"}

        # get json version
        headers={"Accept": "application/json"}

    )

print(response.text)

json_data = response.json() # when header accepts json response

print(type(json_data)) # takes json and converts into python dictionary

print(json_data["joke"])

> sending requests with a query string params

__QUERY STRING: a way to pass data to the server as part of a GET request__

> option 1

import requests

response = requests.get(
    "http://www.example.com?key1=value1&key2=value2"
)

> option 2

import requests

response = requests.get(
    "http://www.example.com",
    params={
        "key1": "value1",
        "key2": "value2"
    }
)

> example 1

import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(
        url,
        # get plain text version
        # just joke for this URL, but not all URLs are have plain text headers setup
        # headers={"Accept": "text/plain"}

        # get html version
        # headers={"Accept": "text/html"}

        # get json version
        headers={"Accept": "application/json"}

    )

print(response.text)

json_data = response.json() # when header accepts json response

print(type(json_data)) # takes json and converts into python

print(json_data["joke"])