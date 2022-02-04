import re

# original regex
# regex_name = r"^(Mr\.|Mrs\.|Ms\.|Mdme\.) ([A-Za-z]+) ([A-Za-z]+)$"

# regex with defined with label and accessed by label (instead of index) using group():
    # paranthesis and ?P<{label}>

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