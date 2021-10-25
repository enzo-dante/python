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

__*3rd param = step/how many to skip and up or down count with +/-__
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

while loops are more flexible than for loops since you explicitely set the start and end conditions, but they require more setup than for loops

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

# list(range(a, b)) = create list of defined indecies of numbers

demo_list = list(range(1, 4))

# list access = lists are organized by indecies that always start at 0

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

# access all values in a list simultaneously

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

# remove(variable) = checks for first match variable in a list and removes or throws error

__does not return removed value__

ex:

nums = [1, 2, 3, 4, 2]
nums.remove(2)
print(nums) # [1,3,4,2] 
