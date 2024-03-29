"""
    ? write a function called {} that takes a {} as parameter(s)
    ?   returns a {}

    * example & output:

"""

# print("------------------------------------------------------------------------------------------")


"""
    ? write print_four_expressions function that takes no parameters 
    ? returns an array with at least 4 different expression (using different operators) that equals 100
"""

def print_four_expressions():

    return [
        99 + 1,
        101 - 1,
        50 * 2,
        200 / 2
    ]

"""
    ? write get_letter_r function that takes a default parameter: "Hello World" 
    ? returns the letter "r" from "Hello World"
"""

def get_letter_r(w= "Hello World"):

    return w.lower()[-3]

"""
    ? write get_ink function that takes the default string "tinker"
    ? returns the string "ink" substring from the default "tinker" string

    * HINT: when slicing, you only go up to but not include the end index
"""

def get_ink(w="tinker"):
    return w[1:4]

"""
    ? write reverse_string function that takes string parameter and returns string with all characters reversed

    reverse_string("tHis is a tEst") # "tsEt a si siHt"
"""

def reverse_string(s):
    return s[::-1]

"""
    ? write list_check function that takes a list parameter
    ?   returns True if each value in the list is a list, else returns false
"""

def list_check(values):
    # list comprehension w/ conditional logic
    my_list = [isinstance(v, list) for v in values]
    return all(my_list)

"""
    ? write remove_every_other function that takes a list parameter
    ?   returns a new list with every second value removed
    
    * HINT:
        list comprehension
        enumerate gives you access to the index
"""

def remove_every_other(values):
    return [v for index, v in enumerate(values) if index % 2 == 0]

"""
    ? write sum_pairs function that takes a list and a number as parameters
    ?   returns list of first pair of numbers that sum to the number pass as a parameter

    # sum_pairs([4,2,10,5,1], 6) # [4,2]
"""

def sum_pairs(nums, sum):

    for i in nums:

        for j in nums:

            if j + i == sum:
                return [i,j]
    
    return []

"""
    ? write vowel_count function that takes a str as parameters
    ?   returns a dictionary with the key as vowels & values as the count of times that vowel appears in the str

    vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
"""

def vowel_count(s):
    vowels = ["a", "e", "i", "o", "u"]
    v_count = {}

    for letter in s.strip().lower():

        if letter in vowels:

            if letter not in v_count:
                v_count[letter] = 1
            else:
                v_count[letter] += 1

    return v_count

"""
    ? write a function called titleize that takes a string of words as parameters
    ?   returns a new string with the first letter of every word in the new str capitalized

    * example & output:
        titleize('this is awesome') # "This Is Awesome"
"""

def titleize(s):

    cap_s = ""

    for word in s.split(" "):
        cap_s += word.capitalize() + " "
    
    return cap_s.strip()

"""
    ? write a function called find_factors that takes a number as parameter(s)
    ?   returns a list of all the factors of that number
    ?   divisible numbers for that number from 1 up to that number

    * example & output:
        find_factors(111) # [1,3,37,111]
"""

def find_factors(n):

    return [f for f in range(1, (n + 1)) if n % f == 0]

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

def includes(c, v, start=None):

    if type(c) is not dict:

        for e in c[start:]:
            if e == v:
                return True

        return False
    
    for e in c.items():
        if e == v:
            return True
    
    return False

"""
    ? write a function called repeat that takes a string and a number as parameter(s)
    ?   returns a new string with the string passed to the function
    ?       repeated the number amount of times

    * example & output:
        repeat('abc', 2) # 'abcabc'
"""

def repeat(s, n):
    return s.strip() * n

"""
    ? write a function called truncate takes a string and a number n, 
    ?   truncate the string to a shorter string containing at most n characters
    ?   truncation must be at least 3 characters long
    ?   returns a string with "..." if n is less than length of string

    * example & output:
        truncate("Problem solving is the best!", 10) # "Problem..."
        truncate("Super cool", 2) # "Truncation must be at least 3 characters."
"""

def truncate(s, n):
    
    min_length = len(s) - 3

    if n < 3:
        return "Truncation must be at least 3 characters."
    elif n < min_length:
        # use slice to create a substring
        return s[:n-3] + "..."

    # implied else-statement
    return s[:n]

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

    ! HINT: use built-in function zip() & then convert into dict:
        pairs up two values from two different lists in sequential order respective of index position in each list
            lists have different length, zip will stop once there are no more pairs to zip
"""

def two_list_dictionary(keywords, values):

    z_dict = dict(zip(keywords, values))

    for k in keywords:

        if z_dict.get(k) == None:
            z_dict[k] = None

    return z_dict

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
    
"""
    ? write a function called same_frequency that takes two numbers as parameter(s)
    ?   returns True if they contain the same frequency of digits, else return False

    * example & output:
        same_frequency(551122,221515) # True
        same_frequency(321142,3212215) # False
        same_frequency(1212, 2211) # True
"""
def same_frequency(n1, n2):

    d1 = {n:str(n1).count(n) for n in str(n1)}
    d2 = {n:str(n2).count(n) for n in str(n2)}

    for k, v in d1.items():
        
        if not k in d2.keys():
            return False
        elif d2[k] != d1[k]:
            return False

    return True
    
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

def nth(my_list, n):
    return my_list[n]
    
"""
    ? write a function called find_the_duplicate that takes an array of numbers (that contains a single duplicate) as parameter(s)
    ?   returns the duplicate number or None

    * example & output:
        find_the_duplicate([1,2,1,4,3,12]) # 1
        find_the_duplicate([6,1,9,5,3,4,9]) # 9
        find_the_duplicate([2,1,3,4]) # None
"""

def find_the_duplicate(a):

    # OPTION 1
    sorted_a = sorted(a) 
    i = 0

    while i < len(sorted_a):
        
        if (i + 1) < len(sorted_a) and (sorted_a[i] == sorted_a[i + 1]):
            return sorted_a[i]

        i += 1
    
    return None

    # OPTION 2
    d = {n : nums.count(n) for n in nums} # dictionary comprehension that uses list count to get duplicate

    for k, v in d.items():

        if v > 1:
            return k

    return None

"""
    ? write a function called sum_up_diagonals that takes a NxN list of lists (2D array) as parameter(s)
    ?   returns a sum of the two main diagonals in the array
    ?       the 1 from the upper left to the lower right
    ?       the 1 from the upper right to the lower left

    * example & output:

        list1 = [
          [ 1, 2 ],
          [ 3, 4 ]
        ]

        sum_up_diagonals(list1) # 10

        list2 = [
          [ 1, 2, 3 ],
          [ 4, 5, 6 ],
          [ 7, 8, 9 ]
        ]

        sum_up_diagonals(list2) # 30

        list3 = [
          [ 4, 1, 0 ],
          [ -1, -1, 0],
          [ 0, 0, 9]
        ]

        sum_up_diagonals(list3) # 11

        list4 = [
          [ 1, 2, 3, 4 ],
          [ 5, 6, 7, 8 ],
          [ 9, 10, 11, 12 ],
          [ 13, 14, 15, 16 ]
        ]

        sum_up_diagonals(list4) # 68
"""

def sum_up_diagonals(array_2d):

    sum = 0

    for i, v in enumerate(array_2d):

        sum += array_2d[i][i]
        sum += array_2d[i][-1-i]

    return sum

"""
    ? write a function called min_max_key_in_dictionary that takes a dict as parameter(s)
    ?   returns a list with lowest and highest key in the arg

    * example & output:
        min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
        min_max_key_in_dictionary({1: "Ellie", 4:"Matt", 2: "Tim"}) # [1,4]
"""

def min_max_key_in_dictionary(d):

    return [min(d.keys()), max(d.keys())]

"""
    ? write a function called find_greater_numbers that takes a list as parameter(s)
    ?   returns the number of times a number is followed by a larger number across the entire list

    * example & output:
        find_greater_numbers([1,2,3]) # 3
        find_greater_numbers([6,1,2,7]) # 4
        find_greater_numbers([5,4,3,2,1]) # 0
        find_greater_numbers([]) # 0
"""

def find_greater_numbers(nums):

    i = 0
    j = 1 
    count = 0
    
    while i <= len(nums):

        while j < len(nums):

            if nums[j] > nums[i]:
                count += 1
            
            j += 1
        
        i += 1
        j = i + 1
    
    return count

"""
    ? write a function called two_oldest_ages that takes a list of numbers as parameter(s)
    ?   returns the two highest numbers within the list in the format [second_oldest_age, oldest_age]

    * example & output:
        two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
        two_oldest_ages( [6,1,9,10,4] ) # [9,10]
        two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
"""

def two_oldest_ages(nums):
    """
    returns a list with the two highest numbers within the list in the format [second_oldest_age, oldest_age]
    """
    return [sorted(nums)[-2], sorted(nums)[-1]]
    
"""
    ? write a function called is_odd_string that takes a str as parameter(s)
    ?   returns True if sum of each character's position in the alphabet is odd
    ?           False if the sum is even

    !   NOTE: index start starts at 1

    * example & output:
        is_odd_string('a') # True
        is_odd_string('aaaa') # False
        is_odd_string('amazing') # True
        is_odd_string('veryfun') # True
        is_odd_string('veryfunny') # False
"""

import string

def is_odd_string(s):
    '''return True if letter index in english radix sums odd'''

    s = s.lower()
    alphabet = list(string.ascii_lowercase)
    sum = 0

    for i, v in enumerate(alphabet):
        
        for character in s:
            
            if character == v:
                sum += (i + 1)
    
    return sum % 2 != 0

"""
    ? write a function called valid_parentheses that takes a string as parameter(s)
    ?   returns a boolean if the string is valid

    * example & output:
        valid_parentheses("()") # True
        valid_parentheses(")(()))") # False
        valid_parentheses("(") # False
        valid_parentheses("(())((()())())") # True
        valid_parentheses("))((") # False
        valid_parentheses("())(") # False
        valid_parentheses("()()()()())()(") # False
        valid_parentheses("") # False
"""

def valid_parentheses(p):
    '''only valid pairs if count is 0'''
    count = 0
    i = 0

    if len(p) <= 0:
        return False

    while i < len(p.strip()):

        if p[i] == "(":
            count += 1

        elif p[i] == ")":
            count -= 1

        if count < 0:
            return False

        i += 1

    return count == 0

"""
    ? write a function called reverse_vowels that takes a str as parameter(s)
    ?   returns a string where the vowels re reversed

    ! do not consider 'y' to be a vowel

    * example & output:
        reverse_vowels("Hello!") # "Holle!"
        reverse_vowels("Tomatoes") # "Temotaos"
        reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
        reverse_vowels("aeiou") # "uoiea"
        reverse_vowels("why try, shy fly?") # "why try, shy fly?"
"""

def reverse_swap_vowels(string, i, j):

    if i == j:
        return

    temp = string[i]
    string[i] = string[j]
    string[j] = temp

    # evaluate next char if not vowel or swapped vowel
    i += 1
    j -= 1

    return (string, i, j)

def reverse_vowels(string):

    # in-place algorithm
    # O(n^2) = quadratic time complexity

    vowels = "aeiou"
    i = 0
    j = len(string) - 1
    str_list = list(string)

    # iterate over list of chars from both directions
    while i < j:

        # continue traversal forward if char at index i not a vowel
        if str_list[i].lower() not in vowels:
            i += 1
        # continue traversal backwards if char at index j not a vowel
        elif str_list[j].lower() not in vowels:
            j -= 1
        # after finding vowels for both indices, swap
        else:
            str_list, i, j = reverse_swap_vowels(str_list, i, j)

    return "".join(str_list)

"""
    ? write a function called three_odd_numbers that takes a list of numbers as parameter(s)
    ?   returns True if any three consecutive numbers sum to an odd number

    * example & output:
        three_odd_numbers([1,2,3,4,5]) # True
        three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
        three_odd_numbers([5,2,1]) # False
        three_odd_numbers([1,2,3,3,2]) # False
"""

def three_odd_numbers(numbers):

    i = 0

    while (i + 2) < len(numbers):

        # check if consecutive numbers sum in list equals odd value
        if((numbers[i] + numbers[i + 1] + numbers[i + 2]) % 2 != 0):
            return True

        i += 1

    return False


"""
    ? write a function called mode that takes a list of numbers as parameter(s)
    ?   returns the mode (most frequent number), can assume mode is unique in challenge

    * example & output:
        mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
"""

def mode(nums):
    # build dict: {value: numFrequency}
    d = {n : nums.count(n) for n in nums}
    # get max key with highest numFrequency
    return max(d, key=d.get)

"""
    ? write a function called running_average that takes a function as parameter(s)
    ?       when returned parameter function is passed a value,
    ?           the parameter function returns the current average of all precious function calls

    ! HINT: use closure, round all answers to the 2nd decimal place

    * example & output:
        rAvg = running_average()
        rAvg(10) # 10.0
        rAvg(11) # 10.5
        rAvg(12) # 11

        rAvg2 = running_average()
        rAvg2(1) # 1
        rAvg2(3) # 2
"""

def running_average():

    running_average.sum = 0
    running_average.num_divisors = 0

    def rAvg(n):
        running_average.sum += n
        running_average.num_divisors += 1

        return (running_average.sum / running_average.num_divisors)

    return rAvg

"""
    ? write a function called letter_counter that takes a str as parameter(s)
    ?   letter_counter returns a function
    ?       write an inner case-insensitive function that takes a letter as parameter(s)
    ?           inner function returns frequency of letter in str from letter_counter function

    ! HINT: use closure

    * example & output:
        counter = letter_counter('Amazing')
        counter('a') # 2
        counter('m') # 1

        counter2 = letter_counter('This Is Really Fun!')
        counter2('i') # 2
        counter2('t') # 1 
"""

def letter_counter(s):

    letter_counter.s = s.lower()
    
    def counter(l):
        return letter_counter.s.count(l)
    
    return counter

"""
    ? write a function called once that takes a function as parameter(s)
    ?   returns a new function that can be invoked only once, else return None if invoked more than once

    * example & output:
        def add(a,b):
            return a+b

        oneAddition = once(add)
        
        oneAddition(2,2) # 4
        oneAddition(2,2) # None
        oneAddition(12,200) # None
"""

def once(func):

    once.count = 0

    def inner(a, b):
        once.count += 1

        if once.count > 1:
            return None
        else:
            return func(a,b)

    return inner

"""
    ? write a function called next_prime that takes no parameter(s)
    ?   returns a generator that will yield unlimited number of primes starting from 2

    * HINT: recall that a prime number is any whole number that has exactly two divisors: one & the number itself

    * example & output:

    primes = next_prime()
    [next(primes) for i in range(25)]
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""

def next_prime():
    pass