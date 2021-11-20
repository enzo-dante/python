# for loop with ranges

Python ranges start at zero by default and count up to, but not including, the end number.

ranges are generate ordered sequences of numbers

to view range in python3, save range to var and list(var)

- printing range does not print out all the numbers in the range.

ex:

iterate over a set of number (1 through 7 but not including 8)

for number in range(1, 8):
	print(number)

ex:

numbers = range(3)
list(numbers) # [0, 1, 2]

ex:

> add up all odd numbers between 10 and 20
> store the result in x:
x = 0

for number in range(11, 20, 2):
    x += number

alternative solution:

> add up all odd numbers between 10 and 20
> store the result in x:
x = 0

for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n

# range() types

__range will start at 0 and go up to (but not including) 3__
range(3): gives you integers from 0, 1, 2

range(1,8): gives you integers from 1-7

__3rd param = step/how many to skip and up or down count with +/-__
range(1, 10, 2): will give you odds from 1-10

range(7, 0, -1): will give you integers from 7 to 1

ex:

The 3rd argument(step) indicates that range should work backwards from 8, moving 2 numbers at a time.

range(8,0,-2)

# for loop with strings

iterate over each character in a string

for letter in 'coffee':
	print(letter)

# while loops

while loops are more flexible than for loops since you explicitly set the start and end conditions, but they require more setup than for loops

while loops continue to execute while a certain condition is truthy

while <boolean>
    # executed code block

ex:

user_res = None
while user_res != 'please':
    user_res = input('you didn't say the magic word...\n')

# break

break is the fastest way to get out of a loop -- it won't run any code after the break

ex:

while True:
    command = input('Type exit, to exit:\n')
    if command.lower() == 'exit':
        break

ex 2:

times = int(input('How many times do I have to tell you to clean your room?'))

for time in range(times):
    print('clean your room')
    if time >= 4:
        print('do you even listen anymore')
        break

# lists

a collection of items, that can be different data types, generally the same though

ex:

tasks = ['install python', 'learn python', 'take a break']

# list(range(a, b)) = create list of defined indices of numbers

demo_list = list(range(1, 4))

# list access = lists are organized by indices that always start at 0

ex:

colors = ['teal', 'purple', 'red']

colors[0] = teal

# list[-n] = negative numbers in a list start backwards

colors = ['teal', 'purple', 'red']
colors[-1] = red

# len(list) = get number of items in list

length starts at 1 not 0

tasks = ['install python', 'learn python', 'take a break']

len(tasks) = 3

# var in list = check if value is in list

__capitalization matters__

colors = ['teal', 'purple', 'red']
'ashley' in colors # false

# access all values IN a list simultaneously

__use a loop__

ex:

numbers = [1, 2, 3]

for num in numbers:
    print(num*2)

ex:

```
index = 0 

while index < len(numbers):
    print(numbers(i))
    i += 1
```

# [].extend() = add multiple items to a list that are on the same level (not a nested list) at the end of a list

data = [1,2, 3]
data.extend([10, 5, 21]) # [1, 2, 3, 10, 5, 21]

# [].append() = add 1 item of any data type to a list at the end of a list

data = [1,2, 3]
data.append(5) # [1, 2, 3, 5]

# [].insert(index, variable) = specific placement in a list

colors = ['red', 'yellow', 'white']

colors.insert(3, 44) # ['red', 'yellow', 'white', 44]

__inferior alternative to place at end__

nums = [1, 2, 3, 4]
nums.insert(len(nums), 99)

# clear = remove all items at once

ex:

nums = [1, 2, 3, 4]
nums.clear()

# pop() = captures and remove item at specific index or last item

ex:

nums = [1, 2, 3, 4]
captured_item = nums.pop() # [1, 2, 3]
print(captured_item) # 3

ex:

nums = [1, 2, 3, 4]
captured_item = nums.pop(1) # [1, 3]
print(captured_item) # 3

ex:

Given a list numbers = [1,2,3] what would the result of numbers.pop(5) be?

IndexError

# remove(variable) = checks for first match variable in a list and removes or throws error if passed argument is not in the list

__does not return removed value__

ex:

nums = [1, 2, 3, 4, 2]
nums.remove(2)
print(nums) # [1,3,4,2] 

# index(variable) 

> returns the index of the specified item in the list

nums = [5,6,7,8,9,10]

nums.index(6) # 1
nums.index(9) # 4

> can also return the index of the specified item after a specified start

nums = [5,5,6,7,5,8,8,9,10]

numbers.index(5, 1) # 1
numbers.index(5, 2) # 4 

# [].count(x)

> return the number of times x appears in the list and will return 0 if not in the list

nums = [5,5,6,7,5,8,8,9,10]
nums.count(5) # 3

# [].reverse()

> reverse the elements of the list (in-place)

first_list = [1, 2, 3, 4]
first_list.reverse() # [4,3,2,1]

# [].sort()

> sort the items of the list (in-place)

another_list = [6,5,4,3,2,1]
another_list.sort() # [1,2,3,4,5,6]

# " ".join(var)

> String method that takes an iterable argument and concatenates the base String between each item of the iterable

words = ["coding","is","fun!"]

" ".join(words) # "coding is fun"

# Slicing

> make new list using slices of the old list
>
> syntax: some_list[start:end:step]
>
> Slicing always requires the use of a colon (:) even if only using 1 argument 

__start: what index to start slicing from until the end__

> if you pass start a non-existent index, it will return an empty list

first_list = [1,2,3,4]

first_list[1:] # [2,3,4]
first_list[3:] # [4]

first_list[-1:] # [4] 
first_list[-3:] # [2,3,4] 

copy_of_first_list = first_list[0:]

first_list == copy_of_first_list # False

__end: the index to copy up to (exclusive counting meaning not includes provided)__

first_list = [1, 2, 3, 4]

> [:2] = implied start at index 0 and slice until index 2, but not include index 2

first_list[:2] # [1,2]
first_list[:4] # [1,2,3,4]

> [:2] = start at index 1 and slice until index 3, but not include index 3 (value 4)

first_list[1:3] #[2,3]

> [:-1] = how many items to exclude from end with indexing counting backwards

first_list[:-1] # [1,2,3]
first_list[1:-1] # [2,3]

__step: in Python, the number to count/skip at a time (like in range)__

first_list = [1,2,3,4,5,6]

> [1::2] = start at index 1: iterate until the end: a step of 2 counts every other number

first_list[1::2] # [2,4,6] 

> [::2] = start at index 0: iterate until the end: a step of 2 counts every other number

first_list[::2] # [1,3,5]

> [1::-1] = start at index 1: iterate until the end: a step that goes backwards direction in list from start index 1

first_list[1::-1] # [2,1]

> [:1:-1] = start at index end (because step = -1): iterate until index 1: a step that goes backwards direction in list from end of list

first_list[:1:-1] # [6,5,4,3]

> [2::-1] = start at index 2: iterate until the end: a step that goes backwards direction in list from start index 2

first_list[2::-1] # [3,2,1]

> String reverse with Slices

string = "This is fun!"

string[::-1] # "!nuf si sihT"

numbers = [1,2,3]

numbers[::-1] # [3,2,1]

__modify portions of a list by setting with Slices__

numbers = [1,2,3,4,5]

numbers[1:3] = ["a", "b", "c] # [1,"a","b","c",4,5]

__chain Slices together__

colors = ["red","blue","yellow"]

> [2][::-1] = access value at index 2 in list and then reverse step value (String in example)

colors[2][::-1] # "wolley"

# Swapping Values

> swap values in a list when shuffling, sorting (in-place and not a new list), algorithms.

names = ["James","Michelle"]

names[0], names[1] = names[1], names[0] # ["Michelle","James"]

# list comprehension syntax

list comprehension functions like a normal for loop, but in a single line:

> [__ for __ in ___]
>
> EXPLANATION: [LOGIC for EACH_VARIABLE in PROVIDED_LIST]

__numbers example__

nums = [1,2,3]

[x*10 for x in nums] # [10,20,30]

__str example__

name = "enzo"

[char.upper() for char in name] # ["E", "N", "Z", "O"]

__str example__

friends = ["enzo", "stone", "mojo"]

[friend[0].upper()+friend[1::] for friend in friends] # ['Enzo', 'Stone', 'Mojo']

__truthy example__

test = [0, [], ""]

[bool(val) for val in test] # [false, false, false]

__data type conversion/casting example__

numbers = [1, 2, 3, 4, 5]

string_numbers_list = [str(num) for num in numbers]

print(string_numbers_list) # ["1", "2", "3", "4", "5"]

# list comprehension conditional logic

__if example__

numbers = [1, 2, 3, 4, 5]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

__if/else example__

numbers = [1, 2, 3, 4, 5]

[n for n in numbers if n % 2 == 0 else n/2 for n in numbers] # [0.5, 4, 1.5, 8, 2.5, 12]

__check in str example__

> if char is not in string list "aeiou", than return to list and then join chars in new list to form new str

with_vowels = "This is so much fun!"

"".join(char for char in with_vowels if char not in "aeiou") # "Ths s s mch fn!"

# nested lists/multi-dimensional list

> one or more lists within a list, which is very common in data science

nested_list = [[1,2,3], [4,5,6], [7,8,9]]

nested_list[0][1] # 2

nested_list[1][-1] # 6

> use multiple for loops to iterate a nested list

nested_list = [[1,2,3], [4,5,6], [7,8,9]]

for list in nested_list:
    for val in list:
        print(val)

> nested list comprehension

nested_list = [[1,2,3], [4,5,6], [7,8,9]]

[[print(val) for val in list] for list in nested_list]

board game ex: 

board = [[num for num in range(1,4)] for val in range(1,4)]

print(board) # [[1,2,3],[1,2,3]],[1,2,3]]

> nested list comprehension with conditional logic

[["x" if num % 2 != 0 else "o" for num in range(1,4)] for val in range(1,4)] # [["x", "o", "x"]["x", "o", "x"]["x", "o", "x"]]