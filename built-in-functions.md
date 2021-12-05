# lambdas()

> a single line anonymous functions
>
> syntax: lambda {parameters}: {automatically_returned_single_expression}
>
> lambdas are used to pass a function into another function

lambda a,b: a + b # adds the parameters a and b together on call of lambda

__lambdas can be stored in a variable, but that is uncommon__

cube = lambda n: n**3

# map()

> a function that accepts at least 2 arguments, a function and an iterable, and runs the lambda for each value in the iterable & returns a map object which can be converted into another data structure

nums = [2,4,6,8,10]

doubles = map(lambda x : x*2, nums) # map this lambda to the nums list by calling the lambda on every item in nums

__returned map objects can only be iterated over once, like converting the map into a list__

doubles = list(map(lambda x : x*2, nums))

letters = ["a", "b", "c", "d"]

peeps = map(lambda letter: letter.upper(), letters) # ["A", "B", "C", "D"]

# filter()

> a function that uses a lambda that takes a collection as an argument and filter out specific values based on a boolean expression
>
> if possible, use list comprehension over filter & map w/ a lambda

__list comprehension is simplified easy-to-read code in python__

names = ["Lassie", "Colt", "Rusty"]

[f"Your instructor is {name}" for name in names if len(name) < 5]

> make sure to convert the filter object into a list afterward

ex:
nums = [1,2,3]
evens = list(filter(lambda n: n % 2 == 0, nums))
evens # [2,4]

ex:
names = ["angel", "ben", "ally"]

__lambda that takes n as an arg, if the first index of n arg is a lowercase "a" -- evaluating True -- for each value in the collection names, than return in filter object converted into a list__

a_names = list(filter(lambda n: n[0] == "a", names))

ex:
users = [
    {"username": "sam", "tweets": ["I love cake", "I love my cat"]},
    {"username": "gary", "tweets": []},
    {"username": "ben", "tweets": ["I hate cookies", "I adore alone time"]}
]

option 1:

__filter with a lambda that will access every user in users list and check if tweets is empty, if empty is True, return in filter object that is converted into a list__

inactive_users = list(
    filter(lambda u: len(
        u["tweets"]
    )) == 0, users
)

option 2:

__not u["tweets"] = not True__

inactive_users = list(
    filter(lambda u: not u["tweets"], users)
)

BEST option 3: list comprehension

inactive_users = [user for user in users if not user["tweets"]]

> combining filter and map

names = ["Lassie", "Colt", "Rusty"]

__filter for names shorter than 5 characters, than map that new filtered list of names to sentences in map object that is converted into a list__

sentences = list(
    map(
        lambda name : f"Your instructor is {name},
        filter(
            lambda value: len(value) < 5, names
        )
    )
)

# all()

> return True if all elements of the iterable are truthy (or if the iterable is empty)

all([0,1,2,3]) # False because 0 is Falsy

__each character in the string "eio" is in "aeiou" is True__

all([char for char in "eio" if char in "aeiou"]) # True

ex:

people = ["Charlie", "Casey", "Cody"]

__each name in people list starts with "C"__

all([name[0] == "C" for name in people]) # True

# any()

> return True if any element of the iterable is truthy; if the iterable is empty, return False

all([0,1,2,3]) # True even though 0 is Falsy

# sorted()

> returns a new sorted list from the items in the iterable (not just a list)

more_numbers = [6,1,8,2]

sorted(more_numbers) # [1,2,6,8] copy
print(more_numbers) = [6,1,8,2]

> change direction of sorted with sorted(list, reverse=True)

nums = (1,2,3)

sorted(nums, reverse=True) # [3,2,1] (a list is returned, not just a tuple)

> key={sort_by_type}

ex:
users = [
    {"username": "sam", "tweets": ["Love cake", "happy family"]},
    {"username": "ben", "tweets": [], "num": 10, "pw": "save"},
    {"username": "sam", "tweets": ["Not again", "where is food"], "color": "red"}
]

__sort users by length of keys__

sorted(users, key=len)

__sort by username with lambda__

sorted(users, key=lambda user: user["username"])

__sort by length of user tweets__

sorted(users, key=lambda user: len(user["tweets"]), reverse=True)

# max() & min()

> max() returns largest item in an iterable or the largest of two or more arguments

max(3,67,99) # 99
max("c", "d", "a") # d

nums = [1,2,3]

max(nums) # 3
min(nums) # 1

max("world") # w
min((2,5,7)) # 2

> min/max with generator expression

names = ["stone", "mojo"]

min(len(name) for name in names) # 4
[len(name) for name in names] # [5,4]

> min/max with lambdas

__lambda that returns list of name lengths in names and max pulls out the name with the most chars__

max(names, key=lambda n : len(n))

# reversed()

> returns a reversed iterator

__reverse() and reversed() are not the same__

nums = [1,2,3,4]

nums.reverse()
nums # [4,3,2,1]

list(reversed(nums)) # [1,2,3,4]

for char in "Hello world":
    print(char) # "dlrow olleh"

# len()

> return length of argument
>
> in the background, len() is actually calling object.__len__()

len("test") # 4

# abs()

> return the absolute value of an integer or floating point number

abs(-5) # 5

# math.fabs()

> return the absolute value of an integer or floating point number, but treats the arg as a float

math.fabs(-5) # 5.0

# sum(iterable, optional_start)

> takes an iterable and optional start and returns the sum of start and the items of an iterable from let to right and returs the total

__default start is 0__

sum([1,2,3]) # 6

sum([1,2,3], 10) # 16

# round(number, digit_percision)

> return rounded to ndigits precision after the decimal point, if ndigits is omitted or is None, it returns the nearest integer to its input

round(10.2) # 10
round(10.2, None) # 10

round(6.8) # 7

round(1.212121, 2) # 1.21

# zip()

> pairs up two numbers from two different lists in sequential order respective of index position in each list

__if lists have different length, zip will stop once there are no more pairs to zip__

nums1 = [1,2,3]
nums2 = [5,6]

list(zip(nums1, nums2)) # [(1,5), (2,6)]

__order matter in respective list, left to right__

first_zip = zip([1,2,3], [4,5,6]) # returns zip object

__convert zip object into a list or dictionary__

list(first_zip) # [(1,4), (2,5), (3,6)] 
dict(first_zip) # {1:4, 2:5, 3:6}

> use * operator on zipped object to unpack a zipped list (essentially reverse zip)

my_list = [(0,1), (5,2), (6, 4)]

list(zip(*my_list)) # [(0,5, 6), (1,2,4)]