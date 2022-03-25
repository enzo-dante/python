# dynamic typing in python

python is highly flexible about reassigning variables to different types, unlike other programming languages

Dynamic-typing just refers to the ability for variables to flexibly learn their types during assignment.

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

4. python uses lower_snake_case and NOT camelCase for variables

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

str = string (can use single or double quotes, just be consistent)
ex) name = 'test'

list = ordered sequence
ex) a = [0, 1, 2]

dict = a collection of key-value pairs
ex) person = {'name': 'test', 'age': 2}

# converting data types

string interpolation implicitly converts data types into strings
you can explicitly convert by using the builtin type as a function

ex:

decimal = 12.2
integer = int(decimal) # 12

# NONE special value

NONE = null

# quotes in str

use double quotes in single quotes

test = 'neo asks: "Is this the matrix?"'

# string escape characters

metacharacters that get interpreted by python to do something special:

https://www.w3schools.com/python/gloss_python_escape_characters.asp

ex:

> Set the message variable equal to any string containing a new-line escape sequence
message = "Hello \n goodbye"

> Add a string to the mountains variable that when printed results in: /\/\/\
> You will need to use an escape sequence more than once!

mountains = "/\\/\\/\\"

> Set the quotation variable to any string that contains an escaped double quotation mark
quotation = "My cat said \"meow\""

# string concatenation

concatenates multiple only strings together

ex:

str_one = 'hello'
str_two = 'world!'

str_four = str_one + ' ' + str_two

> += operator with string concatenation

str_one = 'breaking'
str_one = ' bad'

print(str_one) // breaking bad

# string interpolation

python 3.6+ uses f-strings

ex:

x = 10
formatted = f'You have already asked {x} times!'

python 2 and python 3.5 and earlier uses .format()

ex:

first, last = 'Enzo', 'Vernon'

formatted = "First Name: {}, Last Name: {}".format(first, last)

# strings and indices

each string has a number associated and be accessed via the index

ex:

text = 'lol'

text[0] = 'l'
text[1] = 'o'
text[2] = 'l'

if you pass a negative number, the accessed index starts at the end

ex:

text = 'help'
text[-1] = 'p'

# input()

the input() will prompt user and store the str result to a variable

answer = input('What is your favorite show?:\n')
print('Your favorite show is ' + answer)

# str and foreign languages

if it's Unicode, it's a valid str

# .lower() or .upper()

return string is converted to all lower or upper case which is helpful for error handling

# String reverse with Slices

string = "This is fun!"

string[::-1] # "!nuf si sihT"


# .strip() = removes whitespace