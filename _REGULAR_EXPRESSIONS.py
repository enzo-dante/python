""" 

    ! regular expressions (REGEX)
    
        describing patterns within search strings

            https://www.rexegg.com/regex-quickstart.html

            https://pythex.org/

    * REGEX potential use cases
    
        1. email validation

        2. credit card number validation

        3. phone number validation

        4. advanced find/replace in text

        5. formatting text/output

        6. syntax highlighting
"""

"""

    ! REGEX character class 
    character classes allow us to specify characters to filter in a pattern

        \ = escape special meaning of a character

        . = matches everything

        \. = string value of a period

        \d = digit 0-9

        \w = letter, digit, or underscore

        \s = whitespace character

        \D = not a digit

        \W = not a word character

        \S = not a whitespace character

    ! REGEX boundary matchers
    character classes allow us to specify characters in a GROUP/RANGE to filter in a pattern

        [] = character classes allow us to specify groups/ranges of characters

        [^] = anything that is NOT the specified characters in the brackets with the carrot symbol

            [^k] = anything but the lowercase letter k

        ^ = carrot anchor species the search string has to start with defined regular expression

            ^\d{3}

        '$' = dollar sign boundary denotes the end of string or line

        \b = word boundary

            ex: \b\w+\b = select only and every word

                'hello world I am typing'

        | = the pipe character in regex denotes logical or

            "Mr|Mrs|Ms"

        () = parenthesis represent whole group

            (\(\d{3}\)|\d{3}) \d{3} \d{4}

    ! REGEX quantifiers
    specify how many times a specific character should occur in a pattern

        + = one or more

        {x} = exactly x times.

            {3} = 3 times

        {3,5} = 3 to 5 times

        {4,} = four or more times

        * = zero or more times

        ? = once or none (optional)
"""

""" 
    ! REGEX email validation

    general email pattern sequence:

        starts with 1 or more letter, number, plus sign, dash, underscore, or period

        a single @ sign

        1 or more letter, number, or dash

        a single dot

        ends with 1 or more letter, number, dash or period

    ! (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

    * pattern explanation:

        ^ = search string has to start with any of the defined characters in the bracket

        [a-zA-Z0-9_.+-] = allow lower case a-z, upper case a-z, 0-9, underscore, period, plus sign, or dash

        + = allow one or more of the specified characters in the defined bracket

        @ = a single 'commercial at' sign

        [a-zA-Z0-9-] = allow lower case a-z, upper case a-z, 0-9 or dash

        + = allow one or more of the specified characters in the defined bracket

        \. = a single dot that (must use escape backslash to specify)

        [a-zA-Z0-9-.] = allow lower case a-z, upper case a-z, 0-9, underscore, dash or period

        + = allow one or more of the specified characters in the defined bracket

        $ = search string has to end with any of the defined characters in the bracket

"""

# import regex module
import re

# import regex module
search_str = r"Are test123@gmail.com or marvel616@yahoo.com valid emails?"

# define raw (r) regex string
regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# compile regex string
pattern = re.compile(regex)

# search for a single match in a string with our regex
result = pattern.search(search_str)

# result.group() will return 1st match due pattern.search()
print(result.group())

# find multiple matches in a string with our regex
result = pattern.findall(search_str)
print(result)

# return full match of a string with our regex
result = pattern.fullmatch(search_str)

# ! parsing URLs with python

import re

url_one = "http://www.youtube.com/videos"
url_two = "http://www.youtube.com/videos/asd/das/asd"
url_three = "http://www.youtube.com/videos/"

query_string = "bio?data=blah&dog=yes"

# define raw (r) regex string & compile
regex = r"(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

# use parenthesis to group items in a regex string to access individually
url_regex = re.compile(regex)

# search for a single match in a string with our regex
match = url_regex.search(url_search3+query_string)
print(match.group())

# you can pass int for the respective parenthesis group in a regex
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))

# .groups(), plural of group, returns a tuple of the different components separated by parenthesis
print(match.groups())

"""
! regex labels 

    regex with defined label and accessed by label (instead of index) using group():

        parenthesis and ?P<{label}>
"""

import re

regex_name = r"^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) ([A-Za-z]+)$"

def parse_name(test):

    pattern = re.compile(regex_name)
    matches = pattern.search(test)

    if matches:
        matches.group("first")

    return None

result = parse_name("Mrs. Tilda Swinton")
print(result)

# ! compilation flags

""" 
    ! compilation flags

        IGNORECASE = do case-insensitive matches (ignore capital or lowercase designation)
        
        VERBOSE = organizes regex patterns into a more readable format
"""

import re

test_email = "tom123@yahoo.com"
case_test_email = "TOM123@yahoo.com"
bad_test_email = "my email is tom123@yahoo.com"

"""
    ^([a-z0-9_\.-]+) # starts with first part of email
    @                # single @ sign
    ([\da-z\.-]+)    # email provider
    \.               # single period
    ([a-z\.]{2,6})$  # ends with com, org, net etc.
"""

regex_verbose = "^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"

# re.X = verbose
# re.I = ignore case too
pattern = re.compile(regex_verbose, re. X | re.I)

match = pattern.search(case_test_email)

if match:
    print(f"match: {match.group()}")
    print(f"match: {match.groups()}")
else:
    print(None)

# ! REGEX Substitution

import re

text = "Las night Mrs. Daisy and Mr. White murdered Mr. Chow"

"""
    * regex logic

        \. = escape special functionality of .
        [a-z] = all letter a - z are valid
        ([a-z])[a-z]+ = capture group first letter followed any number of letters
        + = 1 or more instances
"""

regex_replace = r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+"

# re.I = case insensitive
pattern = re.compile(regex_replace, re.I)

REDACTED = "redacted".upper()

result = pattern.sub(REDACTED, text)
print(result)

"""
    ! Capture Groups

        substitute the last name with only the first letter captured

        \g<1> = first matched regex pattern returned
"""

import re

REDACTED = "redacted".upper()
text = "Las night Mrs. Daisy and Mr. White murdered Mr. Chow"

regex_substitute = r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+"

pattern = re.compile(regex_substitute, text)

result = pattern.sub(f"\g<1> {REDACTED}", text)
print(result)

