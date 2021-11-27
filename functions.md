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

__parameters are limited to the scope of the function__

def square(num):
    return num**2

print(square(4)) # 16

> a function can have multiple parameters

__use semantic names for readability__

def multiply(first_number, second_number):
    return first_number * second_number

multiply(2, 5)

> optional default parameter values

__when defining parameters, optionally set the parameter to default value with an equal sign__

def exponent(num=7, power=2):
    return num ** power

print(exponent(2,3)) #8
print(exponent()) # 49



