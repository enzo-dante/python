# documenting functions

> syntax:
>   """ <message> """

def say_hello():
    """A function that returns the string hello"""

    return "Hello!"

> function.__doc__ returns a defined message describing the function

say_hello.__doc__ # 'A function that returns the string hello'

# defining functions

> a function = lines of code packaged together for on-demand reusability that returns an output in relation to the input

def name_of_function(optional_parameters):
    # indented code block to be executed

name_of_function() # execution call

__a method is special type of function attached to a class object__

> functions maintain DRY easy-to-read clean code: DONT REPEAT YOURSELF (tech debt)

__functions help reduce bugs and error by minimizing duplication & organizing the code__

def say_hi():
    print("Hi")

say_hi() # 'Hi'

# returning values as functions outputs

> return exits the function
>
> return pops the function off of the call stack

__return a tuple to return multiple items__

def square_seven():
    return 7**2

result = square_seven()
print(result)

> common function return mistakes

__the indentation of return matters in terms of scope and can prematurely exit function if it were in for loop scope__

def sum_odd_numbers(numbers):
    total = 0

    for n in numbers:
        if n % 2 != 0:
            total += n

    return total

__simplify code as much as possible by removing unnecessary code__

def is_odd_number(num): # unnecessary else
    if num % 2 != 0:
        return True
    else:
        return False

print(is_odd_number(4))
print(is_odd_number(9))

# function/method parameters & arguments

> functions can take optional arguments as input to modify the outputs
>
> parameters = variables in method definition/declaration
> arguments = data passed into method's parameters

def full_name(first="A", last="Test"):
    return f"Your name is {first} {last}"

full_name("Swift", "Ben") # Swift Ben
full_name() # A test

> parameters are limited to the scope of the function:
>
> where are variables can be accessed

__global scope: variables that can be accessed from anywhere (limit use in code)__

instructor = "test" # global scope
total = 0

def say_hello():
    # using global keywords for simply getting their values requires no additional code other than calling the variable

    return f"Hello {instructor}

def increment():
    # use global keyword to update global variable inside function scope

    global total;
    total += 1

    return total

say_hello() # 'Hello test'

__limited function scope__

def say_hello():
    instructor = 'Only Available Inside say_hello'
    return f"Hello {instructor}

say_hello() # 'Hello Only Available Inside say_hello'

print(instructor) # NameError

__nonlocal = modify a parent's variable in a child (nested) function (rarely used)__

def outer():
    count = 0

    def inner():
        # nonlocal specifies variables not defined in global or inner scope, but parent scope

        nonlocal count
        count += 1

        return count

    return inner()

> a function can have multiple parameters

__use semantic names for readability__

def multiply(first_number, second_number):
    return first_number * second_number

multiply(2, 5)

> optional default parameter values

__when defining parameters, optionally set the parameter to default value with an equal sign at the end of the parameters list__

def exponent(num=7, power=2):
    return num ** power

print(exponent(2,3)) #8
print(exponent()) # 49

__default parameters can be anything like functions, lists, dictionaries, strings, booleans etcs__

def add(a,b):
    return a+b

def math(a, b, fn=add): # add function default parameter
    return fn(a,b)

def subtract(a,b):
    return a-b

math(2,2) # 4

math(2,2, subtract) # 0

> keyword arguments allow you to reorder arguments and provide flexibility

full_name("Swift", "Ben") # Swift Ben
full_name(first="Dante", last="Test") # Dante Test
full_name(last="Smith", first="Karen") # Karen Smith

__keyword arguments set the values of the parameters and not the same as using default parameters__

def full_name(first="A", last="Test"):
    return f"Your name is {first} {last}"

full_name() # 'A Test'
full_name(last="Santa", first="Bad")
