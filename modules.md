# module benefits

only import what you need to keep codebase lean

modules are well documented so looking for specific functionality -- instead of having to remember everything -- is easy

modules allow us to import functionality that we might not be able to code ourselves or code that is not often used

modules are external python files that allow our codebase to remain small via reusability across multiple files

# built-in modules

> optional functionality that can be imported on-demand to keep python light

import random

__random needs to be imported and included with method with standard syntax__

random.choice(["apple", "banana", "cherry"]) # random choice from arg list

random.randint(range(1,100)) # return random number from 1-99

__use 'as' to make an alias for an imported module that has a long name__

import random as r

r.shuffle(["apple", "banana", "cherry"])

# import parts of a module

> only import what you need with the "from" keyword
>
> from {module} import {method}, {method}...

__when using "from", the module name won't be defined anymore since we are directly importing the methods__

from random import choice, shuffle

print(random.choice(["apple", "banana"])) # NameError

print(choice(["apple", "banana"])) # successful compilation

# custom modules

> Importing from a module looks the same, no matter what type of module is being imported from.

__the example below shows how to import your own python file into another python file__

file1.py

def test():
    return "test some stuff"

def other_test():
    return "other stuff being tested"

file2.py

import file1

file1.test() # 'test some stuff'

# external modules

> external modules that exist online on a server can be installed via pip (package management system for python that is included with python 3.4+)
>
> python3 -m pip install {package_name}

ex:

in terminal, execute: python3 -m pip install termcolor

import termcolor

text = termcolor.colored("hi there".upper(), color="magenta", on_color="on_green", attrs=["blink"])
print(text)

__help(termcolor) = help() gets documentation for arg package__

# autopep8 terminal command

> python3 -m pip install autopep8

__autopep8 is a terminal linter command that will remove whitespace and simplify boolean logic__

autopep8 --in-place -a --aggressive {file_name}

# __name__

> the value of the __name__ variable in a python file will be equal to __main__ when you run the file directly, otherwise it would be the file name

__ignorning code with __name__ when you want to prevent a block of code from running on an import__

if __name__ == "__main__":
    # this code will only run

