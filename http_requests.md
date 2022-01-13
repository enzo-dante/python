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

