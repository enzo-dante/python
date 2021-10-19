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

if num % 2 > 0:
    print("odd")
else:
    print("even")

ex:

a = 'the'
b = 'The'

a != b // True

ex:

a = 2

if a != 0:
	print('I am the zero that knocks on the door')
elif a == 1:
	print('I know one thing')
elif a == 2:
	print('Two for algorithms enter a bar')
elif a == 3:
	print('Three cats on the prowl')
else:
	print('Do you not have a number?')

> comparison operators

1. greater than
2. less than
3. greater than or equal to
4. less than or equal to

ex:

if num % 2 > 0:
    print("odd")
else:
    print("even")

# modulo even odd comparison

modulo return the remaineder value

111 % 7 returns 6

modulo is often used to find if a number is even or odd when dividing by 2

13 % 2 returns 1(has remainder)

16 % 2 returns 0(no remainder and thus even)

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

ex:

Is the following expression truthy or falsy?

x = 0
y = None
x or y  # this expression

ANSWER: falsy, because 0 and NONE are both falsy values

ex:

Harder question. Is the following expression truthy or falsy?

a = -1
not a  # this expression

ANSWER: Negative numbers are just like regular numbers, so not (True) is false

# conditional to validate is True

if name:
    print('Your name is ' + name)
else:
    print('You didn\'t respond!')

# logical operators

logical operators can be used to make boolean logic comparisons or statements

__and = truthy if a AND b are True__

ex:

if a and b:
	print(c)

__or = truthy if either a OR b is True__

ex:

if am_tired or is_bedtime:
	print('go to sleep')

__not = truthy if the oppoisite of a is True__

ex:

if not is_weekend:
	print('go to work')

ex:

> 2-8 $2
> 65 $5
> $10 for everyone else

__not False = True__

age = 21

if not ((age >= 2 and age <=8) or age >= 65):
	print('you are not a child or a senior citizen')
else:
	print('you are a child or a senior citizen')

# is vs "=="

a == b returns True
a is b returns False 

"==" checks if the value is the same
"is" checks if variables are stored in the same place in memory

__"is" is only truthy if the variables reference the same item in memory__
