# python error documenation

https://docs.python.org/3/library/exceptions.html

# Error types

> SyntaxError: when python encounters incorrect syntax (can't parse)

def first: # SyntaxError due to no parenthesis
    return 1

> NameError: when variable is not defined

print(test) # NameError: name 'test' is not defined

> TypeError: when a function applied to the wrong datatype (can't interpret)

len(5) # TypeError: object of type 'int' has no length

> IndexError: when user tries to access an element in a list using an invalid index (outside of range of the list or string)

my_list = [11, 56]
my_list[2] # IndexError: list index out of range since only using 0 and 1 index

name = "enzo"
name[7] # IndexError

my_tup = (3,4,5)
my_tup[8] # IndexError

> ValueError: built-in operation or function receives correct type but inappropriate value

int("foo") # ValueError

> KeyError: occurs when a dictionary does not have a specific key

my_d = {1: "a", 2:"b"}
my_d[1] # KeyError

> AttributeError: occurs when a variable does not have an attribute

[1,2,3].hello() # AttributeError since list has no hello method

# raise {your_own_exceptions}

> we can raise/throw our own errors using the raise keyword

raise ValueError("invalid value")

> raise our own specific Exception

def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")

    if type(text) is not str:
        raise TypeError("text must be instance of str")

__instead of combining errors, its better to raise error types one at a time to better identify culprit__

    if type(color) is not str:
        raise TypeError("color must be instance type of str")

__better to be specific when raise an error instead of all Exceptions to better identify the culprit__

    if color not in colors:
        # raise Exception
        raise ValueError("color is not valid color in colors")

    print(f"Printed {text} in {color}")

colorize("hello", "chicken")

colorize(34, "red") # will raise/throw an Exception type

# try/except blocks: handling errors

> be specific when handling errors, do not use a blank except

try:
    foobar
except NameError as err:
    print(err) # name 'foobar' is not defined

> try/except blocks with a dictionary

def get_key(d, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "dante"}
print(get_key(d, "name")) # 'dante'

print(get_key(d, "city")) # None

> try/except with optional else

__else block will run when except block does not run__

try:
    num = int(input("enter number"))
except ValueError as err:
    print("input is not a number!")
else:
    print("we are in the else block")

> try/except with optional finally

__finally will run no matter what other code blocks exist in the try/except__

try:
    num = int(input("enter number"))
except ValueError as err:
    print("input is not a number!")
else:
    print("we are in the else block")
finally:
    print("runs no matter what happens")

> it's common to use try/except blocks in a while loop

__always have a break in a while loop even if using a try/except block__

while True:
    try:
        num = int(input("enter number"))
    except ValueError as err:
        print("input is not a number!")
    else:
        print("we are in the else block")
        break
    finally:
        print("runs no matter what happens")

print("continue with remaining code logic")

> a try/except block can handle multiple types of Exception

def divide(a,b):
    try:
        result = a/b
    # except:
        # print("something went wrong and blank except is not helpful")
    except ZeroDivideError:
        print("don't divie by zero!")
    except TypeError as err:
        print("a and b must be int or floats data type")
        print(err)
    else:
        print(f"the resulting quotient is {result}")
    finally:
        print("you finally reached the end of the divide()")

print(divide(1,2))
print(divide(1,0))

# pdb debugging

> import pdb (python debugger) to identify bugs in code

import pdb

> pdb.set_trace() will only run on executed functions if place in that scope
import pdb

def add_nums(a,b):
    pdb.set_trace()
    return a+b

add_nums(1,2) # pdb.set_trace() will pause execution for step-through now since function was called

> wherever pdb.set_trace() is placed in code, it will pause execution to step through 1 line at time for value interaction

import pdb

first = "first"
second = "second"

'''
common pdb commands:
    l (list)
    n (next line is most common command since it allows for stepping through)
    p (print)
    c (continue - finishes debugging)
'''

pdb.set_trace()

'''
can explore already defined values while in pdb viewer

first = 'first'

third = NameError: name 'third' has not been defined
'''

result = first + second

third = "third"
result += third
print(result)
