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