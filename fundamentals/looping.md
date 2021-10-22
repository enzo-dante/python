# for loop with ranges

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

while loops continue to execute while a certain condition is truthy

while <boolean>
    # executed code block

ex:

user_res = None
while user_res != 'please':
    user_res = input('you didn't say the magic word...\n')

# break

the keyword break gives us the ability to exit a while or for loop on command

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
