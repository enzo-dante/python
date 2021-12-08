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