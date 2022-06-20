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