import re

'''
    () = capture group
    ?P<{label}> = capture group label
    ^ = pattern starts with
    [] = allowed group of characters
    \w = any word, digit, or underscore
    + = one or more times
    \( = escape special function & use string ( character
    \) = escape special function & use string ) character
    \d{4} = any digit of 4 character length
'''

# place paranthesis around desired capture groups

# sub_regex = r"(^[\w ]+) \((\d{4})\)" # uses paranthesis group index
# title_format = "\g<2> - \g<1>"

sub_regex = r"(?P<title>^[\w ]+) \((?P<date>\d{4})\)" # uses paranthesis group label
title_format = "\g<date> - \g<title>"

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

def update_titles(titles):
    formatted_titles = []
    for title in titles:
        # compile and define raw regex pattern that is case-insensitive
        pattern = re.compile(sub_regex, re.I)
        # sub matches in text with format that uses capture groups
        result = pattern.sub(title_format, title)
        formatted_titles.append(result)
    
    return formatted_titles

formatted_titles = update_titles(titles)
print(formatted_titles)
