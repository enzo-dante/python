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

