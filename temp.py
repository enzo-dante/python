import re

search_string1 = "my number is 818 412-6890"
search_string2 = "818 412-6890"
search_string3 = "818 412-6890 abdfdfsdf"
search_string4 = "my number is 818 412-6890 or call me at 345 666-1234"
invalid_search_string1 = "my number is 818 4120-68909"
invalid_search_string2 = "my number is 818 412-689077 or call me at 345 66643-1234"

regex = r"\b\d{3} \d{3}-\d{4}\b"
regex_validator = r"^\d{3} \d{3}-\d{4}$"
regex_fullmatch = r"\b\d{3} \d{3}-\d{4}\b"

def extract_phone(input, regex):
    phone_regex = re.compile(regex)
    match = phone_regex.search(input)
    if match:
        return match.group() 
    
    # implied else block
    return None

def extract_all_phones(input, regex):
    phone_regex = re.compile(regex)
    return phone_regex.findall(input)

# print(extract_phone(search_string1, regex))
# print(extract_phone(search_string2, regex))
# print(extract_phone(search_string3, regex))
# print(extract_phone(invalid_search_string1, regex))

# print(extract_all_phones(search_string4, regex))
# print(extract_all_phones(invalid_search_string2, regex))

def is_valid_phone(input):
    phone_regex = re.compile(regex_validator)
    match = phone_regex.search(input)
    if match:
        return True
    return False

def is_full_valid_match(input):
    phone_regex = re.compile(regex_validator)
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


print(is_valid_phone(search_string2))
print(is_valid_phone(invalid_search_string1))
print(is_valid_phone(invalid_search_string1))
    
print(is_full_valid_match(search_string2))



