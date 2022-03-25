"""
    ? write a function called {} that takes a {} as parameter(s)
    ?   returns a {}

    * example & output:
        vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
"""

""" 
    ? write at least 4 different expression (using different operators) that equals 100 
"""

import numbers
from typing import List

def print_four_expressions():
    print(99 + 1)
    print(101 - 1)
    print(25 * 4)
    print(f"{10000/100:.0f}")

# print_four_expressions();

"""
    ? write a string index that returns the letter "r" from "Hello World"
"""

def get_letter_r(word="Hello World"):
    return word[-3]

# print(f"r = {get_letter_r()} in 'Hello World'")

"""
    ? use string slicing in python to grab the word "ink" in from inside the overall word "tinker" 

    * HINT: when slicing, you only go up to but not include the end index
"""

def get_ink(word="tinker"):
    return word[1:4:1]

# print(f"{get_ink()} = 'ink' slice in 'tinker'")

"""
    ? write reverse_string function that takes string parameter and returns string with all characters reversed 
"""

def reverse_string(input):
    return input[::-1]

# print(reverse_string("tHis is a tEst"))

"""
    ? write list_check function that takes a list parameter 
    ?   returns True if each value in the list is a list, else returns false
"""

def list_check(list_2d):
    # list comprehension with conditional logic:
    my_list = [isinstance(l, list) for l in list_2d]
    return all(my_list)

list_test_1 = [[], 1, [2,3], (1,2)]
# list_test_2 = [1, True, [], [1] [2,3]]
list_test_3 = [[], [1], [2,3]]

# print(list_check(list_test_1))
# ! print(list_check(list_test_2))
# print(list_check(list_test_3))

"""
    ? write remove_every_other function that takes a list parameter 
    ?   returns a new list with every second value removed 
"""

list_test_1 = [1,2,3,4,5]
list_test_2 = [5,1,2,4,1]

def remove_every_other(p_list):
    # list comprehension
    # If you use enumerate, you do have access to the index
    return [x for index, x in enumerate(p_list) if index % 2 == 0]

# print(remove_every_other(list_test_2))

"""
    ? write sum_pairs function that takes a list and a number as parameters
    ?   returns first pair of numbers that sum to the number pass as a parameter 

    # sum_pairs([4,2,10,5,1], 6) # [4,2]
"""

numbers_1 = [4,2,10,5,1]
numbers_2 = [11,20,4,2,1,5]

def sum_pairs(num_list, number):

    for i in num_list:
        for j in num_list:
            if j + i == number:
                return [i, j]
        
    return []

# print(sum_pairs(numbers_1, 6))
# print(sum_pairs(numbers_2, 100))

"""
    ? write vowel_count function that takes a str as parameters
    ?   returns a dictionary with the key as vowels & values as the count of times that vowel appears in the str 

    vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
"""

def vowel_count(word):
    v_count = {}
    vowels = ["a", "e", "i", "o", "u"]

    for letter in word.lower():
        if(letter in vowels):
            if(letter not in v_count):
                v_count[letter] = 1
            else:
                v_count[letter] += 1
    
    return v_count

# d = vowel_count("awesome")
d = vowel_count("Elie")
# d = vowel_count("Colt")

# print(d)

"""
    ? write a function called titleize that takes a string of words as parameters
    ?   returns a new string with the first letter of every word in the new str capitalized

    * example & output:
        titleize('this is awesome') # "This Is Awesome"
"""

def titleize(sentence):

    capitalized = ""

    for word in sentence.split(" "):
        word = word[0].upper() + word[1:] + " "
        capitalized += word
    
    return capitalized.strip()

# print(titleize("this is awesome"))
# print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

"""
    ? write a function called find_factors that takes a number as parameter(s)
    ?   returns a list of all the factors of that number
    ?   divisible numbers for that number from 1 up to that number

    * example & output:
        find_factors(111) # [1,3,37,111 ]
"""

def find_factors(number):

    """
        * list comprehension solution
    """
    return [factor for factor in range(1, number + 1) if number % factor == 0]

    """
        * for loop solution
    """
    # factors = []

    # for f in range(1, number + 1):
    #     if number % f == 0:
    #         factors.append(f) 
    
    # return factors

# print(find_factors(111)) # [1,3,37,111 ]
# print(find_factors(321421)) # [1,293,1097,321421 ]

"""
    ? write a function called includes that takes a collection, a value, and an optional starting index as parameter(s)
    ?   returns True if the value exists in the collection when we are starting from the starting_index, otherwise False

    ? the collection can be a string, a list, or a dictionary
    ?   if a string or array, the 3rd parameter is a starting_index from where to search from
    ?   if a dictionary, the function searches for the value among the values in a dictionary, since dictionary's have no sorted order, the 3rd parameter would be ignored

    * example & output:
        includes([1, 2, 3], 1) # True 
        includes([1, 2, 3], 1, 2) # False 
"""

def includes(collection, value=0, start_index=0):

    if type(collection) == str or type(collection) == list:

        if value in collection[start_index:]:
            return True
        
    elif type(collection) == dict:
        
        for k, v in collection.items():

            if v == value:
                return True
            
    return False

# print(includes([1,2,3], 1))
# print(includes([1,2,3], 1, 2))

"""
    ? write a function called repeat that takes a string and a number as parameter(s)
    ?   returns a new string with the string passed to the function
    ?       repeated the number amount of times

    * example & output:
        repeat('abc', 2) # 'abcabc' 
"""

def repeat(my_str, my_num):

    new_str = ""

    for n in range(0, my_num):
        new_str += my_str
    
    return new_str

# print(repeat('abc', 2)) # 'abcabc' 

"""
    ? write a function called truncate takes a string and a number n, truncate the string to a shorter string containing at most n characters 
    ?   truncation must be at least 3 characters long
    ?   returns a string

    * example & output:
        truncate("Problem solving is the best!", 10) # "Problem..."
        truncate("Super cool", 2) # "Truncation must be at least 3 characters."
"""

def truncate(string, n):

    target_length = n - 3

    if n >= 3:
        # python ternary operator
        return string[:target_length] + "..." if len(string) > len(string[:target_length]) else string[:n]
    
    return "Truncation must be at least 3 characters."
    
# print(truncate("Problem solving is the best!", 10)) # "Problem..."
# print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."

"""
    ? write a function called two_list_dictionary that takes 2 lists of varying length as parameter(s)
    ?   the first list contains keywords and the second list contains values 
    ?   returns a dictionary of the keywords and respective values
    ?       if there are not enough values per key, the remaining keys should have a value of null
    ?       if there are not enough keys per value, than just ignore the remaining values

    * example & output:
        two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
        two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
        two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}

    HINT: use built-in function zip() & then convert into dict: 
        pairs up two values from two different lists in sequential order respective of index position in each list
            lists have different length, zip will stop once there are no more pairs to zip
"""

def two_list_dictionary(keywords, values):

    """
    use built-in function zip() & then convert into dict: 
        pairs up two values from two different lists in sequential order respective of index position in each list
            lists have different length, zip will stop once there are no more pairs to zip
    """
    zipped_dict = dict(zip(keywords, values))

    for keyword in keywords:

        if zipped_dict.get(keyword) == None:
            zipped_dict[keyword] = None

    return zipped_dict

# print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}

"""
    ? write a function called range_in_list that takes a list, start_index, and end_index as parameter(s)
    ?   returns the sum of the values between the start_index and end_index in the list (inclusive)
    ?       if start_index not passed as arg, default to 0 
    ?       if end_index not passed as arg, default to last value index
    ?       if end_index is too large, sum should still go through end of list 

    * example & output:
        range_in_list([1,2,3,4],0,2) #  6
        range_in_list([1,2,3,4],0,3) # 10
        range_in_list([1,2,3,4],1) #  9
        range_in_list([1,2,3,4]) # 10
        range_in_list([1,2,3,4],0,100) # 10
        range_in_list([],0,1) # 0
"""

def range_in_list(nums, start=0, end=None):

    sum = 0

    if type(nums) == list:
        
        if end is None or end > len(nums):

            end = len(nums) - 1
        
        for n in nums[start:(end + 1)]:

            sum += n

    return sum

# print(range_in_list([1,2,3,4],0,2)) #  6
# print(range_in_list([1,2,3,4],0,100)) # 10
# print(range_in_list([1,2,3,4],1)) #  9

"""
    ? write a function called same_frequency that takes two numbers as parameter(s)
    ?   returns True if they contain the same frequency of digits, else return False

    * example & output:
        same_frequency(551122,221515) # True
        same_frequency(321142,3212215) # False
        same_frequency(1212, 2211) # True
"""

# inferior solution

# def same_frequency(nums1, nums2):
#     d_one = {}
#     d_two = {}

#     is_same = False

#     for n in str(nums1):
        
#         if d_one.get(n) == None:
#             d_one[n] = 1
#         else:
#             d_one[n] += 1
    
#     for n in str(nums2):
        
#         if d_two.get(n) == None:
#             d_two[n] = 1
#         else:
#             d_two[n] += 1
    
#     for k, v in d_one.items():

#         if d_two[k] == v:
#             is_same = True 
#         else:
#             is_same = False
#             break
        
#     return is_same
        
# superior solution

def same_frequency(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
  
    for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True

# print(same_frequency(551122,221515)) # True
# print(same_frequency(321142,3212215)) # False
# print(same_frequency(1212, 2211)) # True

"""
    ? write a function called nth() that takes a list and a number as parameter(s)
    ?   returns the element at whatever index is the number in the list
    ?       if the number is negative, the nth element from the end is returned
    ?       you cannot always assume that number will always be between the negative value of the list length and the list length minus 1  

    * example & output:
        nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
        nth(['a', 'b', 'c', 'd'], -2) #  'c'
        nth(['a', 'b', 'c', 'd'], 0)  # 'a'
        nth(['a', 'b', 'c', 'd'], -4) #  'a'
        nth(['a', 'b', 'c', 'd'], -1) #  'd'
        nth(['a', 'b', 'c', 'd'], 3)  # 'd'
"""

def nth(my_list, num):
    return my_list[num]
    
    # traditional else/if
    # if num < 0:
    #     return my_list[-1]

    # return my_list[num]

# print(nth(['a', 'b', 'c', 'd'], 1))  # 'b' 
# print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'

"""
    ? write a function called find_the_duplicate that takes an array of numbers (that contains a single duplicate) as parameter(s)
    ?   returns the duplicate number or None

    * example & output:
        find_the_duplicate([1,2,1,4,3,12]) # 1
        find_the_duplicate([6,1,9,5,3,4,9]) # 9
        find_the_duplicate([2,1,3,4]) # None
"""

def find_the_duplicate(nums):
    
    # dictionary comprehension that uses list count to get duplicate

    d = {n : nums.count(n) for n in nums}

    # traditional dictionary creation

    # d = {}

    # for n in nums:

    #     if d.get(n) == None:
    #         d[n] = 1
    #     else:
    #         d[n] += 1

    for k, v in d.items():

        if v > 1:
            return k
        
    return None

# print(find_the_duplicate([1,2,1,4,3,12])) # 1
# print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
# print(find_the_duplicate([2,1,3,4])) # None
