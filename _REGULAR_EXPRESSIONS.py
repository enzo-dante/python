""" 

    ! regular expressions (REGEX)
    
        describing patterns withing search strings

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

    ! REGEX boundaries
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


