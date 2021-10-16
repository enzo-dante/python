# assigning multiple variables simultaneously

a, b, c = 5, 10.2, 'test'

a is now assigned the int value 5
b is now assigned the float value 10.2
c is now assigned the string value 'test'

**generally, you only assign vars simultaneously if they are related in functionality**

# input() 

the input() will prompt user and store the str result to a variable

answer = input('What is your favorite show?:\n')
print('Your favorite show is ' + answer)

# conditionals 

if statements allow for a program to execute different paths based on comparison inputs

use an equality operator (==) because one equal sign (=) assigns a variable

> direct equality (==)

if name == 'Heisenberg':
	print('I am the one that knocks on the door')
elif name == 'Jon Snow':
	print('I know nothing')
else:
	print('Do you not have a name?')

> NOT direct equality (!=)

ex:

a = 'the'
b = 'The'

a != b // True

ex:

a = 1

if a != 0:
	print('I am the zero that knocks on the door')
elif a == 1:
	print('I know one thing')
else:
	print('Do you not have a number?')

> comparison operators

1. greater than
2. less than
3. greater than or equal to
4. less than or equal to

> truthiness & falsiness

expressions return either True or False(booleans are always capitalized), which can be formatted as:

x = 1
x is 1 // True
x is 0 // False

in python, the variables below are inherently false

a = ''
b = NONE
c = 0
d = {}

conditionals without an equality sign can test for truthiness

ex:

name = input('Enter name\n')

# conditional to validate is True
if name:
    print('Your name is ' + name)
else:
    print('You didn\'t respond!')


