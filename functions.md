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

# *args = (pronounced star_args), a special operator we can pass to functions to gather ANY NUMBER of remaining arguments as a tuple

> conventional approach is limited by number of parameters defined

def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3

print(sum_all_nums(4,6,9)) # 19

__*args is just another parameter that can called on-demand__

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num

    return total

print(sum_all_nums(4,6)) # (4,6)

> *args has to come after other named parameters

def sum_all_nums(num1, *args):
    print(num1)

    total = 0
    for num in args:
        total += num

    return total

__note that *args does not include 4, since that is the named parameter in the example which is why the total is 29__

print(sum_all_nums(4,6,9,4,10)) # (4, 29)

> *args can be used with conditional logic

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"

__note the use of an implied short circuit "else" with the second return which exemplifies simplified cleaner code__

    return "Not sure who you are"

print(ensure_correct_info()) # 'Not sure who you are'

__since "Colt" and "Steel" are both present in the arguments, *args conditional logic will return 'Welcome back Colt!'__

print(ensure_correct_info(1, "Colt", True, "Steele"))


# **kwargs = (pronounced QWARGS), a special operator we can pass to functions to gather ANY NUMBER of key words as a dictionary

> **kwargs represents an infinite number of arguments as key-value pairs in a dictionary

def fav_colors(**kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")

fav_colors(colt="purple", ruby="red", ethel="teal") # {"colt":"purple, "ruby":"red", "ethel":"teal}

> **kwargs can be used with conditional logic

david = "David"
special = "special"
no_idea = "Not sure who this is..."

def special_greeting(**kwargs):
    if david in kwargs and kwargs[david] == special:
        return f"{special} greeting {david}!"
    elif david in kwargs:
        return f"{kwargs[david]} for you, {david}!"

    return no_idea

print(special_greeting(David="Hello")) # Hello for you, David!
print(special_greeting(Bob="oh no")) # Not sure who this is...
print(special_greeting(David="special")) # special greeting David!

__per function definition, it doesn't matter to **kwargs if other key-value arguments are found__

print(special_greeting(Gary="hello", David="special")) # special greeting David!

# function parameter order matters

> you need to use all four types of parameters when defining a function

1. named parameters
2. *args
3. default parameters
4. **kwargs

def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a,b,args, instructor, kwargs]

print(display_info(1,2,3, last_name="Steel", job="Instructor"))

> a - 1
> b - 2
> args - (3,) aka single item tuple
> instructor - "Colt"
> kwargs - {"last_name": "Steel", "job": "Instructor"}

# * as an argument = tuple unpacking values

> conventional approach

def sum_all_values(*args):
    total = 0
    for n in args:
        total += n
    print(total)

    return total

sum_all_values(1,30,2,5,6) # 44

> tuple unpacking to split values to pass as individual args

__* as an argument works with both tuples and lists__

def sum_all_values(*args):
    print(args) # (1, 30, 2, 5, 6)
    total = 0
    for n in args:
        total += n
    print(total)

    return total

sum_all_values(1,30,2,5,6) # 44

__adding a * = take collection and iterate over & pass as seperate argument__

nums = (1,2,3,4,5,6)
sum_all_values(*nums) # 21

# ** as an argument = dictionary key-value unpacking

> pass ** as an argument to unpack the key-value pairs of a dictionary

def display_names(first, last):

    print(f"{first} says hello to {second}")
    return f"{first} says hello to {second}"

names = {"first": "Colt", "second": "Rusty"}

display_names(first="Charlie", second="Sue") # "Charlie says hello to Sue"

display_names(**names) # "Colt says hello to Rusty"

> **dictionary with **kwargs

def add_and_multiply_nums(a,b,c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF...")
    print(kwargs)

data = dict(a=1,b=2,c=3, name="Enzo", favorite_number=77.7)

__this also shows that you can pass other named parameters with **dictionary__

add_and_multiply_nums(**data, cat="Blue")
