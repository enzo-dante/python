"""
    ? write a function called {} that takes a {} as parameter(s)
    ?   returns a {}

    * example & output:

"""

# print("function_name() was called")


# print("------------------------------------------------------------------------------------------")


"""
    ? write at least 4 different expression (using different operators) that equals 100
"""

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

list1 = [
    [1,2],
    [3,4]
]

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

# INFERIOR solution
# def sum_up_diagonals(array_2d):

#     d1 = 0
#     d2 = len(array_2d) - 1
#     sum = 0

#     for l in array_2d:

#         sum += l[d1]
#         sum += l[d2]

#         if d1 != (len(l) - 1):
#             d1 += 1
#             d2 -= 1

#     return sum

# SUPERIOR solution
def sum_up_diagonals(arr):
    total = 0

    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total

# print(sum_up_diagonals(list1))
# print(sum_up_diagonals(list2))

"""
    ? write a function called min_max_key_in_dictionary that takes a dict as parameter(s)
    ?   returns a list with lowest and highest key in the arg

    * example & output:
        min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
        min_max_key_in_dictionary({1: "Ellie", 4:"Matt", 2: "Tim"}) # [1,4]
"""

d1 = {2:'a', 7:'b', 1:'c',10:'d',4:'e'}
d2 = {1: "Ellie", 4:"Matt", 2: "Tim"}

# INFERIOR solution
# def min_max_key_in_dictionary(d):

#     min_k = 0
#     max_k = 0

#     for k in d.keys():
#         if min_k == 0 or max_k == 0:
#             min_k = k
#             max_k = k
#         elif min_k > k:
#             min_k = k
#         elif max_k < k:
#             max_k = k

#     return [min_k, max_k]

# SUPERIOR solution
def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]

# print(min_max_key_in_dictionary(d1))

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

    count = 0
    i = 0
    j = 1

    while i < len(nums):

        while j < len(nums):

            if nums[j] > nums[i]:
                count += 1

            j += 1

        j = i + 1
        i += 1

    return count

# print(find_greater_numbers([1,2,3])) # 3

"""
    ? write a function called two_oldest_ages that takes a list of numbers as parameter(s)
    ?   returns the two highest numbers within the list in the format [second_oldest_age, oldest_age]

    * example & output:
        two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
        two_oldest_ages( [6,1,9,10,4] ) # [9,10]
        two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
"""

# INFERIOR solution
# def two_oldest_ages(nums):

#     sorted_nums = sorted(nums)
#     return [sorted_nums[-2], sorted_nums[-1]]

# SUPERIOR solution
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

# print(two_oldest_ages( [1, 2, 10, 8])) # [8, 10]

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

# SUPERIOR solution

from decimal import Decimal
import string # for alphabet

def is_odd_string(letters):

    sum = 0
    n_list = [n for n in range(1, 27)]
    a_list = list(string.ascii_lowercase)

    # create dictionary of with nums as keys and values as letters in the alphabet via zip
    d = dict(zip(n_list, a_list))

    for (k, v) in d.items():

        for l in letters:

            if l == v:
                sum += k

    if sum % 2 != 0:
        return True

    return False

# INFERIOR solution
def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1

# print(is_odd_string('a')) # True
# print(is_odd_string('aaaa')) # False
# print(is_odd_string('veryfun')) # True

"""
    ? write a function called valid_paranthesis that takes a string as parameter(s)
    ?   returns a boolean if the string is valid

    * example & output:
        valid_parentheses("()") # True
        valid_parentheses(")(()))") # False
        valid_parentheses("(") # False
        valid_parentheses("(())((()())())") # True
        valid_parentheses('))((') # False
        valid_parentheses('())(') # False
        valid_parentheses('()()()()())()(') # False
"""

# def valid_parentheses(parens):

#     count = 0
#     i = 0

#     while i < len(parens):

#         if (parens[i] == '('):
#             count += 1
#         elif (parens[i] == ')'):
#             count -= 1

#         if (count < 0):
#             return False

#         i += 1

#     return count == 0

def valid_parentheses(p):

    '''only valid pairs if count is 0'''
    p = p.strip()
    count = 0
    i = 0

    while i < len(p):

        if p[i] == "(":

            count += 1

        elif p[i] == ")":

            count -= 1

        if count < 0:
            return False

        i += 1

    return count == 0

# print(valid_parentheses("()")) # True
# print(valid_parentheses(")(()))")) # False
# print(valid_parentheses("(")) # False

# print(valid_parentheses("(())((()())())")) # True
# print(valid_parentheses('))((')) # False
# print(valid_parentheses('())(')) # False

# print(valid_parentheses('()()()()())()(')) # False

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
