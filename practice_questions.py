# for loop exercise

# exercise 1: print out string based on input

# num_requests = input('How many times do I have to tell you\n')
# num_requests = int(num_requests)
#
# for num_requests in range(num_requests):
#     print(f'{num_requests + 1}: clean up your room!'.upper())

# exercise 2: loop through 1-20

# if 4 or 13, print 'x is unlucky'
# if even, print 'x is even'
# if odd, print 'x is odd'

# for x in range(1, 21):
#     remainder = x % 2
#     if x == 4 or x == 13:
#         print(f'{x} is unlucky')
#     elif remainder:
#         print(f'{x} is odd')
#     else:
#         print(f'{x} is even')

# alternative solution

# for num in range(1,21):
#     if num == 4 or num == 13:
#         state = 'unlucky'
#     elif num % 2:
#         state = 'odd'
#     else:
#         state = 'even'
#     print(f'{num} is {state}')

# while loop exercise

# exercise 1: capture input to stop while loop

# user_res = None
# while user_res != 'please':
#     user_res = input('what is the magic word to stop the while loop?\n')
#     user_res = user_res.lower()

# exercise 2: print X with BOTH while and for loops

# for num in range(1, 11):
#     print(f'num_prints: {num}\n'+'x'.upper()*num)
#
# # ugly nested loop solution without string multiplication
#
# num_prints = 0
#
# while num_prints < 10:
#     print(f'num_prints: {num_prints + 1}')
#     num_prints += 1
#     x = ''
#     for num in range(num_prints):
#         x += 'x'
#     print(x.upper())

# exercise 3: repeat everything until the user says 'stop copying me'

# sentence = input('How is it going?\n')
# solution = 'stop copying me'
#
# while sentence != solution:
#     print(sentence)
#     sentence = input()
#
#     if sentence == solution:
#         print('Ugh fine you win...')

# alternative solution

# is_copying = True
# sentence = input('How is it going?\n')
#
# print(sentence)
#
# while is_copying:
#     if sentence == 'stop copying me':
#         print('Ugh fine you win')
#         is_coping = False
#         break
#     else:
#         sentence = input()
#         print(sentence)

# exercise 4: create list called nums that contains 1-99 (including 99)

nums = []
for n in range(1, 100):
    nums.append(n)
    n += 1

# alternative solution
nums = []
for n in range(99):
    n += 1
    nums.append(n)

# exercise 5: access elements in the provided list to correct strings

# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
people[0] = 'Hannah'
#Change "Geoffrey" to "Jeffrey"
people[-2] = 'Jeffrey'
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = 'Aparna'

# exercise 6: add list items together into a single sentence that is capitalized
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ''
# Define your code below:
for n in sounds:
    result += n.upper()

# exercise 7: add list of items to a pre-existing list

# Create a list called instructor
instructor = []
# Add the following strings to the instructor list
    # "Colt"
    # "Blue"
    # "Lisa"
instructor.extend(['Colt', 'Blue', 'Lisa'])

# alternative solution
instructor.append("Colt")
instructor.append("Blue")
instructor.append("Lisa")

# exercise 8: get first letter of str vars in list and get only even numbers

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

# exercise 8 for loop alt solution

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)

# exercise 9: get intersercting numbers in 2 different lists and reverse and lowercase list of names

nums1 = [1,2,3,4]
nums2 = [3,4,5,6]

answer = [n for n in nums1 if n in nums1 and n in nums2]

names = ["Elie", "Tim", "Matt"]
answer2 = [name[::-1].lower() for name in names]


# exercise 9 for loop alt solution

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())

# exercise 10: get numbers divisible by 12 in range 1-100

answer = [val for val in range(1,101) if val % 12 == 0]

# exercise 10 for loop alt solution

numbers = []

for n in range(1, 101):
    numbers.append(n)

answer = [n for n in numbers if n % 12 == 0]

# exercise 11: get string excluding vowels from "amazing"

answer = [char for char in "amazing" if char not in "aeiou"]

# exercise 11 list alt solution

answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]

# exercise 12: write out nested_list that returns [[0,1,2], [0,1,2], [0,1,2]]

nested_list = [0,1,2]
answer = [[nested_list for nested_list in range(0,3)] for nested_list in range(0,3)]

# exercise 13: write out 10x10 nested list and each inner list holds numbers 0-10

answer = [[i for i in range(0,10)] for num in range(0,10)]

# exercise 14: print out artist full name using dictionary

# superior option 1: f-string in python 3.6+

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"

# inferior option 2: "{}".format()

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = "{} {}".format(artist["first"],artist["last"])

# exercise 15: use a loop to add together all the donations and store the resulting number in a variable called total_donations

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

total_donations = 0

for value in donations.values():
    total_donations += value

# exercise 16: use dictionary to print out either '3 left' if toffee cookie, '1 left' if morning bun, or 'We don't make that' if not in dict

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

# get() option:
quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")

# IN option:
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")

# exercise 17: use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state

#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

initial_game_state = {}.fromkeys(game_properties, 0)

# exercise 18: update inventory copy

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"

stock_list["cookie"] = 18

# remove 'cake' from stock_list USE A DICTIONARY METHOD

stock_list.pop("cake")

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# exercise 18: use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state

# make sure your solution is assigned to the answer variable so the tests can work!
# {key@index : value@index iterate for each index starting at 0 to length of list 1

answer = {list1[i]: list2[i] for i in range(0,len(list1))}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# exercise 19:

# use the person variable in your answer to get this output:
#   {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

# option 1
answer = {person[i][0] : person[i][1] for i in range(0, len(person))}

# option 2
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

# option 3
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)

# exercise 20:

# make sure your solution is assigned to the answer variable so the tests can work!
# get this output: {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}

# option 1
answer = {}.fromkeys("aeiou", 0)

# option 1.5
answer = dict.fromkeys("aeiou", 0)

# option 2
answer = {key : 0 for key in "aeiou"}

# exercise 21: use chr(num) to get ASCII uppercase letter value A-Z (65-90) and create dictionary with corresponding ASCII code - letter value

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {count: chr(count) for count in range(65,91)}

# exercise 22: tuples & sets exercises

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
# Hint: you can use slicing with tuples

# option 1
value = (1,)
# option 2
value = numbers[0:1]

# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 4 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

# exercise 23: Define your make_noise function below, then call make_noise once:
# make_noise() prints 'THE CROWD GOES WILD'

def make_noise():
    print("the crowd goes wild".upper())

make_noise()

# exercise 23: Define a function called generate_evens
# it should return a list of even numbers between 1 and 50(not including 50)

# option 1: for loop
def generate_evens():
    even_nums = []

    for n in range(1, 50):
        if n % 2 == 0:
            even_nums.append(n)

    return even_nums

generate_evens()

# option 2: list comprehension
def generate_evens():
    evens = [n for n in range(1,50) if n % 2 == 0]
    return evens

generate_evens()

# exercise 24: without adding any new lines of code, make count_dollar_signs work as intended

# original:
    # def count_dollar_signs(word):
    #     count = 0
    #     for char in word:
    #         if char == '$':
    #             count += 1
    #         return count

# solution:
    # The problem is that the function returns the very first time through the loop because of the way return is indented.
    # To fix it, all we have to do is outdent the return statement so that it now only returns after the loop finishes running

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

# exercise 25: redefine speak to get the same functionality but with less code

# original:

# def speak(animal="dog"):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#          return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     else:
#         return "?"

# solution:

def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')

# exercise 26: define a function contains_purple that accepts any number of arguments;
    # it should return True if any of the arguments are "purple" (all lower case), otherwise False

purple = "Purple".lower()

def contains_purple(*args):
    if purple in args:
        return True

    # short circuit implied else = cleaner simplified code
    return False

# exercise 27: define a function combine_words that accepts word and any number of arguments;
    # if prefix == True, "{prefix_value}{word}"
    # if suffix == True, "{word}{suffix_value}"
    # else word

prefix = "prefix"
suffix = "suffix"

# Define combine_words below:
def combine_words(word, **kwargs):
    if prefix in kwargs:
        # return f"{kwargs[prefix]}{word}"
        return "{}{}".format(kwargs[prefix], word)
    elif suffix in kwargs:
        # return f"{word}{kwargs[suffix]}"
        return "{}{}".format(word, kwargs[suffix])

    # short circuit implied else = cleaner simplified code
    return word


# exercise 28: use list/tuple unpacking to get individual values
    # Instead of passing in a single item (the list), pass in 121 separate arguments

# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)

result2 = count_sevens(*nums)

# exercise 29: function exercises

# Define a function product that returns the product of two numbers

def product(a,b):
    return a*b

# Define a function product that returns the product of two numbers

'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

# option 1: dictionary
def return_day(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    if num < 1 or num > 7:
        return None
    elif num in days.keys():
        return days[num]

# option 2: list
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num-1]
    return None

# option 3: error handling
def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

# First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(elements):
    if not elements:
        return None

    return elements[-1]


# count the number of times letter appears in string and the function should be case insensitive

def single_letter_count(word,letter):
    return word.lower().count(letter.lower())

# count the number of times letter appears in string as a dictionary and the function with 1 arg

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# solution explanation:
'''
For each letter in the input string,
make the key the letter itself ("a" for example),
the corresponding value is the result of running count() of that letter in the string.
'''

# option 1:
def multiple_letter_count(msg):
    return {msg[i] : msg.count(msg[i]) for i in range(0, len(msg))}

# option 2:
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

# produce the desired results below for the function list_manipulation()

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

add = "add"
remove = "remove"
end = "end"
beginning = "beginning"

def list_manipulation(the_list, command, location, value=None):
    if command == remove and location == end:
        return the_list.pop()
    elif command == remove and location == beginning:
        return the_list.pop(0)
    elif command == add and location == beginning:
        # must make copy of the list before adding to it, it will return None if you try to add to argument
        new_list = [value]
        new_list.extend(the_list)
        return new_list
    elif command == add and location == end:
        # must make copy of the list before adding to it, it will return None if you try to add to argument
        list_copy = the_list
        list_copy.append(value)
        return list_copy

print(list_manipulation([1,2,3], "add", "end", 30))

# write a function that checks if a single argument is a palindrome

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

# option 1:
def is_palindrome(sentence):
    # use slicing to check if sentence is the same backwards as it is forwards
        # [::-1] = start at beginning: go until end: go in reverse order
    return sentence == sentence[::-1]

# option 2: advanced
def is_palindrome(string):
    # replace all spaces(" ") with empty strings ("")
    stripped = string.replace(" ", "")
    # use slicing to check if sentence is the same backwards as it is forwards
    return stripped == stripped[::-1]

# write a function that takes two arguments to check how often arg_b is in the list arg_a

'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(a_list, search_term):
    search_count = a_list.count(search_term)
    return search_count

# write a function that multiplies all the even numbers in a list arg and returns the total

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(num_list):
    # use list comprehension to get even numbers
        # current n for each n in number_list
        # return if the remaineder of current n divided by 2 = 0
    even_nums = [n for n in num_list if n % 2 == 0]
    # start with 1 since you are multiplying
    total = 1
    for n in even_nums:
        total *= n

    return total

# write a function that multiplies all the even numbers in a list arg and returns the total

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

# option 1: python 3.5 and below
# def capitalize(s):
#     # Slicing the first character (up to index 1) and capitalizing it
#     # Adding that to the rest of the string (from index 1 onward)
#     return s[:1].upper() + s[1:]

# option 2
# def capitalize(s):
#     # Slicing the first character (up to index 1) and capitalizing it
#     # Adding that to the rest of the string (from index 1 onward)
#    return f"{s[:1].upper()}{s[1:]}"

# write a function that returns only Truthy values in a list arg

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

# option 1: list comprehension
def compact(values):
    # the current value for each value in values list
        # return if the value is Truthy
    return [v for v in values if v]

# option 2:
def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals

# write a function that returns a list of values where the values are present in both list arguments

# option 1: list comprehension
def intersection(list_a, list_b):
    # the current value for each value in list_a
        # return v if v is in list_b too
    return [v for v in list_a if v in list_b]

# option 2:
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

# option 3: sets
    # It converts the lists to sets, which removes duplicate values, and then finds the intersection of them using &.
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

# write a function that returns a list of values where the values are seperated by the callback function argument

'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

# option 1: list comprehension
def partition(a_list, callback):
    truthy_list = [v for v in a_list if callback(v)]
    falsy_list = [v for v in a_list if callback(v) == False]

    final_list = []
    final_list.append(truthy_list)
    final_list.append(falsy_list)
    return final_list

# option 2: nested list comprehension
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

# option 3: for loop
def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

# option 4:
def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]

# exercise 30:
def calculate(**kwargs):
    # defined a dictionary called operation_lookup  that maps a string like "add" to an actual mathematical operation involving the values of 'first' and 'second'
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    # create a boolean variable called is_float, which is True if kwargs contains 'make_float', otherwise it's false
    is_float = kwargs.get('make_float', False)
    # lookup the correct value from the operation_lookup dict using the operation that was specified in kwargs
    operation_value = operation_lookup[kwargs.get('operation', '')]
    # return a string containing either the specified message or the default 'The result is' string.
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

# exercise 31: write a lambda that accepts a single number and cubes it. Save it in a variable called cube.

cube = lambda n: n**3

# exercise 32: define the function decrement_list that accepts a list of nums and decrements each value by 1
    # hint: use a map that returns a list

def decrement_list(nums):
    return list(map(lambda n: n-1, nums))

# exercise 32: define the function using filter that takes a single list parameter and removes all the negatives from a list and returns a list

def remove_negatives(nums):
    positives = list(filter(lambda n : n >= 0, nums))
    return positives

# exercise 32: Implement your is_all_strings function below that checks that list of values only contains str data type

def is_all_strings(collection):
    return all([type(s) == str for s in collection])

# exercise 33: define extremes function that takes 1 arg and returns a tuple of min & max values
    # hint: tuples() only takes 1 arg

def extremes(values):
    return tuple([min(values), max(values)])

# exercise 34: write function that gets number with largest magnitude (farthest away from 0) from list
def max_magnitude(nums):
    abs_nums = [abs(n) for n in nums]
    return max(abs_nums)

# exercise 35: write sum_even_values function that accepts any number of arguments and if not arg list is not False, returns sum of list values

'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

def sum_even_values(*args):
    evens = [n for n in args if n % 2 == 0]
    if not evens: return 0

    return sum(evens)

# exercise 36: write sum_floats function that accepts any number of arguments that must be floats
    # if not arg list is not False, returns sum of list values else 0

'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

def sum_floats(*args):
    float_nums = [f for f in args if type(f) == float]
    if sum(float_nums) is False:
        return 0

    return sum(float_nums)

# exercise 37: use zip to get each student's highest grade

'''
data is respective to each other per position
'''

midterms = [80,91,78]
finals = [98,89,53]
students = ["dan", "ang", "kate"]

# option 1: list comprehension with zip()
final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades)

# option 2: dictionary comprehension with zip()
final_grades = {tup[0] : max(tup[1], tup[2]) for tup in zip(midterms, finals)}
print(final_grades) # {"dan": 98, "ang": 91, "kate": 78}

# option 3: map lambda with zip()
scores = list(
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)

student_scores = dict(
    zip(
        students,
        scores
    )
)

print(scores) # {"dan": 98, "ang": 91, "kate": 78}

# exercise 38: use zip to get interleave words
    # interleave('hi', 'no') = "hnio"

# option 1:
def interleave(word1, word2):
    w1_list = [letter for letter in word1]
    w2_list = [letter for letter in word2]
    z_list = list(zip(w1_list, w2_list))
    i_word = ""
    for t in z_list:
        i_word += "".join(t)

    # .strip() = removes whitespace
    return i_word.strip()

# option 2:
def interleave(str1,str2):
    # Zip the two strings together, which returns a list of tuples like: [('h','n'), ('i','o')]
    # First join the individual tuples into strings, which is what the first
    # Finally, join all the remaining strings into one large string

    return ''.join(''.join(x) for x in (zip(str1,str2)))

# exercise 39: write function that accepts a list filters out numbers divisible by 4 and returns a new list with each value tripled

'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

# option 1: filter(), lambdas, and .map()
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

# option 2: list comprhension
def triple_and_filter(nums):
    div_list = [n for n in nums if n % 4 == 0]
    return [value*3 for value in div_list]

# exercise 40: What type of error do you expect from this code?

def add(a,b):
  return a+b


add(1) # TypeError: the missing arg is interpreted as None

# exercise 41: Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples

    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"

def divide(num1, num2):
    try:
        result = num1/num2
    # except:
    #     print("blank except is not helpful")
    except TypeError as err:
        print(err)
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    else:
        # print("you have reached me, else")
        return result
    # finally:
    #     print("you have reached me, finally")

    # return result (commented out to showcase else block)

# exercise 41: Use math.sqrt() to find the square root of 15129 and save it to variable called answer:

import math

answer = math.sqrt(15129)
print(answer)

# exercise 42: using keyword module, write a function that takes any number of str arguments and returns True/False based on if any of the values are True
    # google search keyword module

from keyword import iskeyword as ikw

def contains_keyword(*args):

    # keywords = []
    # for a in args:

    #     if ikw(a):
    #         keywords.append(True)
    #     else:
    #         keywords.append(False)

    keywords = [ikw(a) for a in args]

    if any(keywords):
        return True

    return False

# exercise 42: pretend you are using two separate files exercise.py and helpers.py

# in the helpers.py, define a function in here called lucky_number that always returns 37
def lucky_number():
    return 37

# in the exercise.py, import your helpers module here.
    # Do not use the 'from' or 'as' syntax, just use a plain old 'import'
    # call the lucky_number function from your helpers module, and save the result to a variable called num

import helpers

num = helpers.lucky_number()

# exercise 43: What's the difference between these two import statements?

'''
1. import random
2. from random import *
'''

# once imports everything as an attribute on random, the other imports everything into the current namespace


# exercise 46: use termcolor and pyfiglet external modules to colorize user input text with simple error protection
    # hint: review module documentation

from pyfiglet import figlet_format as ff
from termcolor import colored

# help(figlet_format)
# help(termcolor)
    # available: red, green, yellow, blue, magenta, cyan, white

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

message = input("what message do you want to print? Python!!!!\n")
color = input("what color?\n")

def print_art(msg, color):
    if color not in valid_colors:
        color = "magenta"

    ascii_msg = ff(message)
    colored_ascii = colored(ascii_msg, color=color)

    print(colored_ascii)

print_art(message, color)

# exercise 44: Define the Comment class below with username, text, and likes that has a default of 0:

class Comment:

    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

# exercise 45: Define the BankAccount class that has an owner and balance with a get_balance, withdraw, and deposit method

class BankAccount:

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# exercise 46: Define the Pet class that only allows a set number of species

class Pet:

    allowed_species = ["cat", "dog", "fish", "rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed_species:
            raise ValueError(f"You cannot have a {species} pet")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed_species:
            raise ValueError(f"You cannot have a {species} pet")
        self.species = species

cat = Pet("blue", "cat")
dog = Pet("stone", "dog")

# exercise 47: use OOP inheritance to create instances of User class and Moderator class
    # moderators are essentially Users with some additional functionality

class User:
    # class variable
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

        # for each instance of User, increment active_users class variable
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        return f"{self.age}th, {self.first}"

class Moderator(User):
    # class variable
    total_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        return f"There are currently {cls.total_moderators} active moderators"

    def __init__(self, first, last, age, community):
        # since a User class is being created for every moderator, active_users class variable is automatically incremented for each moderator with super() inheritance
        super().__init__(first, last, age)
        self.community = community

        Moderator.total_moderators += 1

    def remove_post(self):
        # even though full_name() is defined in User parent class, Moderator child class still has access
        return f"{self.full_name()} removed a post from {self.community}."

print(User.display_active_users())

user_1 = User("Tom", "Garcia", 35)
print(User.display_active_users())

jay = Moderator("Jay", "Beal", 42, "Piano Community")
ben = Moderator("Ben", "Steel", 61, "Piano Community")
print(jay.full_name())
print(jay.community)
print(User.display_active_users())
print(Moderator.display_active_moderators())


# exercise 48: trace path of multiple inheritance

class Aquatic:
    def __init__(self, name):
        print("Aquatic init")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("Ambulatory init")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"

# since Ambulatory is 1st class argument, it takes precedence in inheritance order
class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("Penguin init")

        # when using multiple inheritance, its better to be explicit with the parent class
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)

        # super().__init__(name=name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_hook = Penguin("Captain Hook")

print(isinstance(captain_hook, Penguin)) # True
print(isinstance(captain_hook, Aquatic)) # True
print(isinstance(captain_hook, Ambulatory)) # True

print(captain_hook.swim())
print(captain_hook.walk())

# .greet() inherits from Ambulatory not Aquatic class due to class argument inheritance order
print(captain_hook.greet())

# exercise 48: Define your Mother, Father, Child classes that shows MRO (Method Resolution Order) and Mother is prioritized below:

class Mother:

    # def __init__(self, eye_color, hair_color, hair_type):
    #     super().__init__(eye_color, hair_color, hair_type)

    def __init__(self, eye_color="brown", hair_color="dark brown", hair_type="curly"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type

class Father:

    # def __init__(self, eye_color, hair_color, hair_type):
    #     super().__init__(eye_color, hair_color, hair_type)

    def __init__(self, eye_color="blue", hair_color="blond", hair_type="straight"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type

class Child(Mother, Father):
    pass
    # def __init__(self, eye_color, hair_color, hair_type):
    #     Mother.__init__(eye_color=eye_color, hair_color=hair_color, hair_type=hair_type)
    #     Father.__init__(eye_color=eye_color, hair_color=hair_color, hair_type=hair_type)

# exercise 49: create a class that demonstrates overriding built-in methods for a dictionary
    # magic built-in methods can be found in documentation
    # override __setitem__(), __repr__(), __missing__(), __contains__()

class GrumpyDict(dict):
    # we don't need to define our own __init__() because we can inherit the existing dict__init__()

    def __repr__(self):
        # return f"none of your business".upper()
        print("none of your business".upper())
        return super().__repr__()

    def __missing__(self, key):
        return f"you want a {key} that isn't here"

    def __setitem__(self, key, value):
        print("you want to change dictionary?".upper())
        print("fine!".upper())
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("nope it isn't here".upper())
        return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data["city"] = "Tokyo"
print(data['city'])

"city" in data # __contains__ overridden and will return False despite key being there

# exercise 48: Define the generator function week  which has a list of days.
    # Iterate over the days and yield each day. After "Sunday", the generator is exhausted. It does not start over.

# option 1:
def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day

# option 2:
'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

def week():
    day = 1
    while day <= 7:
        yield "Monday"
        day += day
        yield "Tuesday"
        day += day
        yield "Wednesday"
        day += day
        yield "Thursday"
        day += day
        yield "Friday"
        day += day
        yield "Saturday"
        day += day
        yield "Sunday"
        day += day

# exercise 48: yes_or_no loops forever (while True) and yields answer, and then toggles answer from yes to no, or vice versa.

# option 1:
def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

# option 2: inferior method

'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def inner_yes_or_no():
    count = 0

    while count <= 3:
        yield "yes"
        yield "no"
        yield "yes"
        yield "no"

def yes_or_no():
    return inner_yes_or_no()

# exercise 49: make_song takes a verses count and beverage parameter and returns a generator
    # the default verse count = 99 and the default bevergage is soda

'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(verses=99, beverage="soda"):

    # list that has number of specified verses, goes until -1, and starts at the end and goes backwards
    for num in range(verses, -1, -1):
        if num == 0:
            yield 'No more {}!'.format(beverage)
        elif num == 1:
            yield 'Only {} bottle of {} left!'.format(verses, beverage)
        else:
            yield '{} bottles of {} on the wall.'.format(verses, beverage)

        verses -= 1

# exercise 50: show how using generators versus a list saves computational processing when generating a fibonacci sequence
    # WARNING: using lists is generally superior unless you only need 1 variable at a time
    # fib sequence = [0,1,1,2,3,5,8,13]
        # to get next number, add previous 2 = a, b , a+b, b + (a+b)...

def fib_list(max):
    nums = []
    a, b = 0, 1

    while len(nums) < max:
        nums.append(b)
        # to get next number, add previous 2
        a, b = b, a+b
    return nums

def fib_generator(max):
    x = 0
    y = 1

    count = 0
    while count < max:
        # to get next number, add previous 2
        x, y = y, x+y
        yield x
        count += 1

for n in fib_list(1000000):
    print(n)

# exercise 51: produce the below for get_multiples()

'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(number=1, count=10):
    next_number = number

    while count > 0:
        yield next_number
        count -= 1
        next_number += number

# exercise 52: produce the below for get_unlimited_multiples()

'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)]
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

# !We just loop forever (while True) instead of checking to see how many times we've looped.

def get_unlimited_multiples(number=1):

    next_number = number
    while True:
        yield next_number
        next_number += number

# exercise 53: take decorator quiz

'''
1. Decorators are functions?
True or False?

    True, they are higher order functions, because they take functions as arguments.

2. To implement decorator functionality, you need to use the "@" symbol.
True or False?

    False! The "@" symbol is widely used, but it just syntactic sugar over some variable reassignment.

3. Why do you typically see *args  and **kwargs  inside of a decorator?

    You may not know how many arguments the function you're going to decorate requires.

4. What does functools wraps  do?

    functools wraps preserves the name and docstring of the function being decorated
'''

# exercise 54: build a speed-test decorator

# ! original speed-test code without decorator
'''
    import time

    start_time = time.time()
    sum([x for x in range(100)])
    total_time = time.time() - start_time

    sum(x for x in range(100))
'''

from functools import wraps
from time import time

def speed_test(fn):

    @wraps(fn) # wraps preserve "fn" metadata
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed: {end_time - start_time}")
        return result

    return wrapper

@speed_test
def sum_nums_generator():
    return sum(x for x in range(1000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(1000000)])

print(sum_nums_generator())
print(sum_nums_list())

'''
    Time Elapsed: 0.052384138107299805
    499999500000
    Time Elapsed: 0.07418513298034668
    499999500000
'''

# exercise 55: write a function called show_args that accepts a function and returns another function,
    # before invoking the function, show_args should be responsible for printing tow things:
        # a tuple of positional arguments, and a dictionary of keyword arguments

'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper

# exercise 56: This wrapper function simply runs the function, and returns a list containing the result twice

'''
@double_return
def add(x, y):
    return x + y

add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''

from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

# exercise 57: write a function which accepts a function and returns another function
    # the function passed to it should only be invoked if there are fewer than three positional arguments passed to it, otherwise return "Too many arguments!"

'''
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
'''

from functools import wraps

def ensure_fewer_than_three_args(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        if len(args) < 3:
            return fn(*args, **kwargs) # return any number of args and kwargs

        return "Too many arguments!"

    return wrapper

# exercise 58: write a function only_ints which accepts a function and returns another function
    # the function passed to it should only be invoked if all of the arguments passed to it are integers
        # otherwise return 'Please only invoke with integers.'

'''
@only_ints
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

# inferior option:

from functools import wraps

def only_ints(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        is_integers = []
        for v in args:
            if type(v) == int:
                is_integers.append(True)
            else:
                is_integers.append(False)

        if all(is_integers):
            return fn(*args, **kwargs)

        return "Please only invoke with integers."

    return wrapper

# superior option:

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner

# exercise 59: write a function that accepts a function and returns another function
    # the function passed to it should only be invoked if there exists a keword argument with a name of "role"  and a value of "admin"
        # otherwise return "Unauthorized"

'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

# inferior option:

from functools import wraps

def ensure_authorized(fn):

    @wraps(fn)
    def inner(*args, **kwargs):

        if kwargs.get("role") and kwargs["role"] == "admin":
            return fn(*args, **kwargs)

        return "Unauthorized"

    return inner

# superior option:

from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper


# exercise 60: write a function called delay which accepts a time and returns an inner function that accepts a function
    # when used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it
        # before starting the timer, delay will print a message to user notifying length of delay

'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(timer):

    def inner_decorator(fn):

        @wraps(fn) # @wraps preserves the metadata
        def wrapper(*args, **kwargs):

            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)

            return fn(*args, **kwargs)

        return wrapper

    return inner_decorator

# exercise 61: write a Robot class that utilizes a before test hook

# Robot.py
class Robot:
    def __init__(self, name, battery=100, skills=[]):
        self.name = name
        self.battery=battery
        self.skills = skills

    def charge(self):
        self.battery = 100
        return self

    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"I am {self.name}"
        return "low power. Please charge"

    def learn_skill(self, new_skill, cost_to_learn):
        if self.battery >= cost_to_learn:
            self.battery -= cost_to_learn
            self.skills.append(new_skill)
            return f"whoah! i know {new_skill}".upper()
        return "insufficient battery."


# RobotTests.py

import unittest
from robot import Robot

class RobotTests(unittest.TestCase):

    # with setUp, it re-runs the code so you wouldn't be using an already modified instance
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "I am Mega Man"
        )
        self.assertEqual(
            self.mega_man.battery,
            49
        )

if __name__ == "__main__":
    unittest.main()

# exercise 62: using TDD (test driven development) and unittest, write out deck of cards application

# exercise 63: file management quiz

'''
# ! what's the difference between file.readlines and file.read?

    file.readlines reads the file into memory as a list of strings, while file.read reads the file into memory as a single string

# ! what's one benefit to using a 'with' block statement to open files?

    you don't need to manually close the file

# ! what does the seek method do?

    it lets you move your cursor anywhere in an open file
'''

# exercise 64: copy() takes in a file name and a new file name and copies the contents of the first file to the second file

'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

# option 1: SUPERIOR

copy('story.txt', 'story_copy.txt') # None

# option 1: INFERIOR

def copy(file_name, new_file_name):

    # do not nest multiple open commands: open and close asynchronously for computational optimzation
    with open(file_name) as file_one:
        data = file_one.read()

    # w = override existing content
    with open(new_file_name, "w") as new_file:
        new_file.write(data)


# exercise 65: copy_and_reverse takes in a file name and a new file name and copies the reversed contents of the first file to the second file

'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(file_name, new_file_name):

    # do not nest multiple open commands: open and close asynchronously for computational optimzation
    with open(file_name) as original_file:
        data = original_file.read()

    # String reverse with Slices [from_start:from_end:backwards_direction_from_end_start]
        r = data[::-1]

    # w = override existing content
    with open(new_file_name, "w") as new_file:
        new_file.write(r)

# exercise 66: the statistics function takes in a file name and returns a dictionary with the num_lines, words, chars in the file

'''
statistics('story.txt')
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

# option 1:

def statistics(file_name):

    with open(file_name) as file:
        data = file.read()

    num_chars = len(data)
    num_words = len(data.split())
    num_lines = len(data.split("\n"))

    return {'lines': num_lines, 'words': num_words, 'characters': num_chars}

# option 2:

def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }


# exercise 67: replace all instances of the word in the file with the replacement word

'''
find_and_replace('story.txt', 'Alice', 'Colt')
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file_name, search_word, replacement_word):

    # "r+" = read and write in pre-existing file
    with open(file_name, "r+") as file:
        # read file content and store to data var
        data = file.read()
        # cursor seek beginning of file to prepare for write
        file.seek(0)
        # replace the searched_word with replacement_word
        updated_data = data.replace(search_word, replacement_word)
        # write the new content over the old content
        file.write(updated_data)
        # Truncate() method truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed.
        file.truncate()

 # exercise 65: file management quiz 2

'''
# ! what csv method lets you read csv rows into memory as lists?

    from csv import reader

    with open("example.csv") as file:
        csv_reader = reader(file)

# ! what csv method lets you read csv rows into memory as dictionaries?


    from csv import DictReader

    with open("example.csv") as file:
        csv_reader = DictReader(file)


# ! what is a delimiter?

    a character used to separate values

# ! what csv method creates an object that lets you take lists of data & write rows into a csv?

    from csv import writer

    with open("example.csv", "w") as file:
        csv_writer = writer(file)

# ! what csv method creates an object that lets you take dictionaries of data & write rows into a csv?

    from csv import DictWriter

    with open("example.csv", "w") as file:
        csv_writer = DictWriter(file)
'''

# exercise 68: with users.csv, write add_user function that replicates the below output

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

# superior solution:

# import external csv module
import csv

def add_user(first_name, last_name):

    # a - append to a file (previous content will NOT be removed)
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])

# inferior solution:

# import methods from external csv module
from csv import reader, writer

def add_user(first_name, last_name):

    f_column = "First Name"
    l_column = "Last Name"
    file_name = "users.csv"

    # read csv with reader_ojbect to get existing data, convert data into nested list, add new list/row
    with open(file_name) as file:

        csv_reader = reader(file)
        users = [user for user in csv_reader]
        users.append([first_name, last_name])

    # write to csv with writer_object by looping through the created reader list
    with open(file_name, "w") as file:

        csv_writer = writer(file)
        for user in users:
            csv_writer.writerow(user)

# exercise 69: with users.csv, write print_users function that replicates the below output

'''
print_users() # None
# prints to the console:
# Colt Steele
'''

# option 1: using lists

# import reader from external csv module
from csv import reader

def print_users():

    with open("users.csv") as file:
        csv_reader = reader(file)

        # skip headers row with next()
        next(csv_reader)
        # since user name is broken up by first and last in a list, need to format into full name string
        for user in csv_reader:
            print("{first_name} {last_name}".format(first_name=user[0], last_name=user[1]))

# option 2: using dictionaries with DictReader

from csv import DictReader

def print_users():
    with open("users.csv") as csvfile:
        csv_reader = DictReader(csvfile)
        for row in csv_reader:
            print("{} {}".format(row['First Name'], row['Last Name']))


# exercise 70: with users.csv, replicate the output below:

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

import csv

def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)

# exercise 71: with users.csv, replicate the output below:

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

# option 1:

# since you need to return and index, the collection needs to be an ordered list object
from csv import reader

def find_user(first_name, last_name):

    with open("users.csv") as file:
        csv_reader = reader(file)
        # next(csv_reader) # don't remove headers because it will mess up index sequence
        data = list(csv_reader)

    for user in data:
        if user[0] == first_name and user[1] == last_name:
            return data.index(user)

    # the not found return string needs to be outside the for loop
    return 'Not Here not found.'

# option 2:

import csv

def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)

# exercise 72: update_users takes an old first name, old last name, new first name, new last name
    # update_users updates the users.csv file so that nay user whose first and last names match the old first and last names are updated to the new first and last names.
    # the function should return a count of how many users were updated

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

# use csv module to import csv list reader & writer
from csv import reader, writer

def update_users(old_first, old_last, new_first, new_last):

    csv_file = "users.csv"
    count = 0

    # open csv_file to read data
    with open(csv_file) as file:
        csv_reader = reader(file)
        # convert csv as a nested list object/matrix that is accessible outside the scope of the open()
        data = list(csv_reader)

    # open new file and write/override existing data to it
    with open(csv_file, "w") as file:
        csv_writer = writer(file)
        # loop through list data aka the rows of the original csv_file
        for row in data:
            # use writer object to writerow() if current data matches old data
            if row[0] == old_first and row[1] == old_last:
                # since each row is itself a list, you need pass a list object into writer.writerow()
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                # otherwise override row with current row data
                csv_writer.writerow(row)

        return "Users updated: {}.".format(count)

 # exercise 73: delete_users takes an first name, last name
    # delete_users updates the users.csv file so that any user whose first and last names matches the inputs are removed.
    # the function should return a count of how many users were removed

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

# import csv mode for list reader, writer
from csv import reader, writer

def delete_users(first_name, last_name):

    csv_file = "users.csv"
    count = 0

    # open and use reader to read data
    with open(csv_file) as file:

        csv_reader = reader(file)
        # convert csv into a nested lists/matrix object that is accessible outside of open() scope
        rows = list(csv_reader)

    # open csv_file, remove rows first, than write/override to csv_file
    with open(csv_file, "w") as file:

        # prepare writer object with csv file
        csv_writer = writer(file)

        for row in rows:
            # row = ["Peter", "Parker"]
            # remove row if row data matches inputs
            if row[0] == first_name and row[1] == last_name:
                # rows.remove(row)
                count += 1
            else:
                # otherwise, simply override row with current row data
                csv_writer.writerow(row)

        return "Users deleted: {}.".format(count)

 # exercise 73: OOP Quiz

'''

# ! Say we have a class Pet, what is the best way to call the parent __init__ methods?

    class Pet(Animal, Friend):
        def __init__(self, name)
            self.name = name

In the init method, call super().__init__
Super is the preferred way to reference the parent since it follows MRO automatically

# ! what is MRO in python?

The order in which python looks up (aka resolves) methods on a class, influenced by inheritance

# ! what are three ways to look up MRO for the class Penguin?

Penguin.__mro__
Penguin.mro()
help(Penguin)

# ! why is it considered good OOP practice for Animal to raise a NotImplementedError?

    class Animal:

        def speak():
            raise NotImplementedError

It's impossible to generalize a sound that all animals make, therefore it's best left up to the subclasses to implement

# ! how does python know how to interpret the + operator differently in these cases?

    5 + 5 = 10
    "5" + "5" = "55"

The first argument has a special method that defines what to do with the + operator, python actually performs x.__add__(y)

# ! how can i make it so that len(cart) returns the count of items in my shopping cart, provided cart is an instance of ShoppingCart?

    class ShoppingCart:
        def __init__(self):
            self.items = []
            self.count = 0

implement the special/magic/dunder method __len__() which the builtin len calls.

in other words, add self.__len__(self) as a new method on ShoppingCart that returns self.count

'''

 # exercise 74: Regular Expressions (regex) Quiz

'''

# ! given the following regular expression (just focus on what is in between the slashes):

    /h/

Which of the following strings will have matches in them?

1. "hello world"
2. "I'm happy"
3. "Hi you!"
4. "apple juice"

answer:
    1 & 2: The regex matches any string containing a lowercase "h"

# ! What of the following does \w  NOT match?

    uppercase letters
    lowercase letters
    numbers 0-9
    spaces
    underscores

answer:
    whitespace: \w will match any letter number, dash, or underscore but NOT spaces!

# ! Given the following pattern:

    9\d\d

Which of the following contain matches?

1. "987"
2. "912345"
3. "Hello this is 911"
4. "My lucky number is 345"
5. "4567891111"

answer:
    options 1, 2, 3, and 5

# ! Given the following regex:

    7{3}

Which of the following contains a match:

1. "73"
2. "7-7-7"
3. "Your score is 777"
4. "1234567777789"

answer:
    options 3 and 4

# ! What does the following regular expression mean:

    hi{2,}

answer:
    a single 'h' and then 'i' repeated tow or more times! The {2,} only applies to the "i"

# ! Given the following regular expression:

    0?\d

Which of the following contain matches?

1. "00"
2. "9"
3. "0"
4. "03"

answer:
    all of the above

# ! What is an alternative way of writing \d

1. [0-9]
2. [0123456789]

answer:
    both options work

# ! What does the following regex match?

    [a-z0-9]{3}

answer:
    exactly three lowercase letters or digits

# ! What does the following regex mean?

    [^@$]

answer:
    any character that is NOT (specified by ^) a commercial at sign (@) or a dollar sign ($)
    The ^ applies to both characters in the brackets

# ! What does the $  character signify in a regex?

answer:
    denotes the end of a string

# ! Given the following regex:

    ^\d{3}$

Which of the following contains a match:

1. "aaa"
2. "23456"
3. "987"
4. "Yay I got 777"

answer:
    ^ = start of string
    \d{3} = exactly any 3 digits
    $ = end of string

    only option 3 fulfills the regex

# ! Given the following regex:

    Mr.|Mister Holmes

Which of the following CONTAIN matches? It's a little tricky!!

1. "Mr. Davis"
2. "Mister Holmes"
3. "Mr."
4. "Mister"

answer:
    Because of the lack of parens, this regex matches either "Mr." OR "Mister Holmes".

# ! Which regex would match both of the following strings

    "cat(s)"

AND

    "dog(s)"

answer:
    \w{3}\(s\)

    Remember, we have to escape parens with \


'''

# exercise 74:
    # use a regular expression module with python to validate phone numbers

# import regex module
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

# exercise 75:
 # Write a function called is_valid_time that accepts a single string argument.
 # It should return True; if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.
 # Note that times can start with a single number (2:30) or two (11:18).

# option 1:

''' Don't forget to import re!'''
import re

'''
^ = starts with
\d{2} = 2 digit number
| = or
\d{1} = 1 digit number
$ = ends with
'''
regex_time = r"^((\d{2})|(\d{1})):(\d{2})$"

'''Define is_valid_time below:'''
def is_valid_time(time):
    '''compile & define raw regex string'''
    pattern = re.compile(regex_time)
    '''search for a single match in a string with our regex'''
    match = pattern.search(time)

    if match:
        return True
    '''implied else statement'''
    return False

# option 2:

''' Don't forget to import re!'''
import re

'''
The regular expression I used is:

    ^\d\d?:\d\d$

The time must start with a digit, and there can be a second optional digit before the colon.  Then there's the colon and two mandatory digits.  I used ^ and $ to make sure the time was the only thing in the input string.
'''

def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False

# exercise 76: Write a function called parse_bytes that accepts a single string.
    # It should return a list of the binary bytes contained in the string.
    # Each byte is just a combination of eight 1's or 0's.

# don't forget to import re
import re
'''
My regex looks like this:

    '\b[10]{8}\b'

[10] = It consists of eight 1s or 0s
\b = surrounded by word boundaries on either side. Remember a word boundary is either a space or the start/end of a line.

I then used findall rather than search, to return a list of all matches.
'''
regex_bytes = r"\b[10]{8}"
# define parse_bytes below:
def parse_bytes(bstring):
    # compile & define regex pattern
    pattern = re.compile(regex_bytes)
    # find all pattern matches in arg and return as a list
    return pattern.findall(bstring)

# exercise 77:
    # Define a function called parse_date that accepts a single string Your code should check to see if the string matches a date format
    # We're going to use the format of "dd/mm/yyyy" but it should also work with "dd.mm.yyyy" and "dd,mm,yyyy".
    # However, rather than simply returning True or False if the string matches...you should instead return a dictionary containing the three parts of the date with the keys "d", "m" and "y" like so:
        # Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None

        # parse_date("01/22/1999") # {'d': '01', 'm': '22', 'y': '1999'}

#import re
import re
'''
    ^ = all matches start with
    () = character group
    \d\d or \d{2} = two digits ex: 01
    [/.,] = any one of the 3 chars in the brackets would suffice
    $ = all matches end with
    ?P<{label}> = access label
'''
# use labels to access individual components (d,m,y) of regex

# regex_date = r"(?P<d>^\d\d)[/.,](?P<m>\d\d)[/.,](?P<y>\d{4})"
regex_date = r"(?P<d>^\d{2})[/.,](?P<m>\d{2})[/.,](?P<y>\d{4})"

#define parse_date below
def parse_date(date):
    # compile & define raw regex pattern
    pattern = re.compile(regex_date)
    # search for matches in date parameter
    match = pattern.search(date)
    if match:
        # access regex label by passing defined label
        return {
            "d": match.group("d"),
            "m": match.group("m"),
            "y": match.group("y")
        }

# exercise 78: define a function called censor that accepts a single argument and censors any words that with "frack"

import re

'''
    \b = word boundary
    () = capture group
    \w* = letter, digit, or underscore zero or more times
    | = or
'''
# censor_regex = r"\b(frack|fracking|fracker)\b"
censor_regex = r"\b(frack\w*)\b"
CENSORED = "censored".upper()

def censor(text):
    # compile and define raw regex pattern that is case-insensitive
    pattern = re.compile(censor_regex, re.I)
    # substitute matches in text
    return pattern.sub(CENSORED, text)

# exercise 79: find and replace items in a given string with the following format
    # "1978 - Tales of the City"

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
