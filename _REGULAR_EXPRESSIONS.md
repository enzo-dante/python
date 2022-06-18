# regular expressions (regex) = describing patterns withing search strings

__cheat sheet__

https://www.rexegg.com/regex-quickstart.html

# writing basic regular expression

regex is case sensitive

/h/ = 'h' and not 'H'

> regular expression tester that catches python nuances

https://pythex.org/

# parsing URLs with python

    # regex module
import re

url_search1 = "http://www.youtube.com/videos"
url_search2 = "http://www.youtube.com/videos/asd/das/asd"

url_search3 = "http://www.youtube.com/videos/"
query_string = "bio?data=blah&dog=yes"

    # define raw (r) regex string & compile
    # use parenthesis to group items in a regex string to access individually
regex = r"(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
url_regex = re.compile(regex)

    # search for a single match in a string with our regex

    # match = url_regex.search(url_search2)
match = url_regex.search(url_search3+query_string)
    # print(match.group())

    # you can pass int for the respective parenthesis group in a regex
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))

__.groups(), plural of group, returns a tuple of the different components separated by parenthesis__
print(match.groups())

# regex access using labels instead of index

> regex with defined with label and accessed by label (instead of index) using group():
    > parenthesis and ?P<{label}>

import re

    # original regex
    # regex_name = r"^(Mr\.|Mrs\.|Ms\.|Mdme\.) ([A-Za-z]+) ([A-Za-z]+)$"

    # regex with defined with label and accessed by label (instead of index) using group():
        # parenthesis and ?P<{label}>
regex_name = r"^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) ([A-Za-z]+)$"

def parse_name(test):
    pattern = re.compile(regex_name)
    matches = pattern.search(test)
    if matches:
        # return matches.groups()

        # accessed by label using group():
        return matches.group("first")
    return None

result = parse_name("Mrs. Tilda Swinton")
print(result)

# compilation flags

> IGNORECASE = do case-insensitive matches (ignore capital or lowercase designation)
>
> VERBOSE = organizes regex patterns into a more readable format

import re

test_email = "tom123@yahoo.com"
case_test_email = "TOM123@yahoo.com"
bad_test_email = "my email is tom123@yahoo.com"

verbose_regex = r"""
    ^([a-z0-9_\.-]+) # starts with first part of email
    @                # single @ sign
    ([\da-z\.-]+)    # email provider
    \.               # single period
    ([a-z\.]{2,6})$  # ends with com, org, net etc.
"""

pattern = re.compile(verbose_regex, re.X | re.I) # X = verbose and I = ignore case too

match = pattern.search(case_test_email)

if match:
    print(f"match: {match.group()}")
    print(f"match: {match.groups()}")
else: print(None)

# regex substitution

import re

text = "Last night Mrs. Daisy and Mr. White murdered Mr. Chow"

'''
    \. = escape special functionality of .
    [a-z] = all letters a through z are valid
    ([a-z])[a-z]+ = capture group first letter followed any number of letters
    + = 1 or more instances
'''
replace_regex = r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+"

__compile and define raw regex pattern that ignores letter-casing__
pattern = re.compile(replace_regex, re.I)

'''result = pattern.findall(text)'''
'''result = pattern.search(text).group()'''

__substitute matching regex patterns in text string with REDACTED__

'''result = pattern.sub("redacted".upper(), text)'''
'''print(result)'''

'''
using CAPTURE GROUPS,
    substitute matching regex patterns in text string with REDACTED

    \g<1> = first matched regex pattern returned

    *doesn't seem to work when you call .upper()
'''

'''result = pattern.sub('\g<1> REDACTED', text)'''
'''print(result)'''

'''
using CAPTURE GROUPS
    substitute the last name with only the first letter captured
'''
result = pattern.sub('\g<1> \g<2>', text)
print(result)