# dynamic typing in python

python is highly flexible about reassigning variables to different types, unlike other programming languages

ex) 

a = 'test'
a = 5

# assigning multiple variables simultaneously

a, b, c = 5, 10.2, 'test'

a is now assigned the int value 5
b is now assigned the float value 10.2
c is now assigned the string value 'test'

**generally, you only assign vars simultaneously if they are related in functionality**

# naming restrictions

1. variable names must START a letter or underscore in python

good) '_test' or 'person'

bad) '2tests'

2. variable names can only consist of letters, numbers, and underscores

good) '_person1'

bad) test@home

3. names are case-sensitive

CATS != cats

Cats != cats

4. python uses snake_case and NOT camelCase for variables

good) hard_test

bad) hardTest

5. normal variables should all be lowercase

ex) gym_rat

6. CONSTANTS should be all capitalized

ex) PI = 3.14

7. only use camelCase to refer to a class

8. dunders (double underscores) are to be private and left alone

ex) '_off_limits_'

# data types

bool = true or false
ex) on_fire = false

int = integer
ex) a = 2

str = string (can use single or double quotes, just be consisten)
ex) name = 'test'

list = ordered sequence
ex) a = [0, 1, 2]

dict = a collection of key-value pairs
ex) person = {'name': 'test', 'age': 2}

# NONE special value

NONE = null

# quotes in str

use double quotes in single quotes

test = 'neo asks: "Is this the matrix?"'


