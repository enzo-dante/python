# higher order functions

> higher order functions = functions that return a function or accepts 1 or more functions as an argument

def sum(num, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total

def square(x):
    return x*x

print(sum(3, square)) # 0 + 1 + 4 = 5

> we can nest functions inside one another

from random import choice as c

def greet(person):

    def get_mood():
        msg = c(("Hello ", "Go Away ", "Love "))
        return msg

    result = get_mood() + person
    return result

print(greet("Toby"))

> we can return a function from other functions

from random import choice as c

def make_laugh_func():

    def get_laugh():
        l = c(("haha", "lol", "tehehe"))
        return l

    return get_laugh # return entire get_laugh function

laugh = make_laugh_func()

print(laugh()) # when executing laugh(), it returns choice of get_laugh returned function

> inner functions can access outer function scope using closure

from random import choice

def make_laugh_at_func(person):

    def get_laugh():
        laugh = choice(("haha", "lol", "tehe"))
        return f"{laugh} {person}" # person is defined outside the scope of get_laugh using closure

    return get_laugh

laugh_at = make_laugh_at_func("Linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())

# decorators

> a decorator is a higher order function that wraps other functions and enhance their behavior using @ syntax
>
> logic when we write:
> @decorator
> def func(*args, **kwargs):
>   pass
>
> logic t
__decorator that does not use @ syntax__

def be_polite(fn):

    def wrapper():
        print("what a pleasure to meet you")
        fn()
        print("Have a great day!")

    return wrapper

def greet():
    print("My name is Colt.")

def rage():
    print("i hate you".upper())

greet = be_polite(greet)
    # what a pleasure to meet you
    # My name is Colt.
    # Have a great day!

polite_rage = be_polite(rage)
    # what a pleasure to meet you
    # I HATE YOU
    # Have a great day!

__decorator that does use @ syntax__

def be_polite(fn):

    def wrapper():
        print("what a pleasure to meet you!")
        fn()
        print("Have a nice day!")

    return wrapper

__by using @be_polite, we don't need to set 'greet = be_polite(greet)' because greet() is automatically being passed into be_polite(fn) as fn__

@be_polite
def greet():
    print("My name is Matt")
    # what a pleasure to meet you
    # My name is Matt.
    # Have a great day!

# decorators with different signatures needs flexability

__BROKEN: the problem with the below is that the decorator has varying number of arguments being passed into it__

def shout(fn):

    def wrapper(name):
        return fn(name).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please"

print(greet("Todd"))

> the standard decorator pattern that uses *args and **kwargs

def my_decorator(fn):

    def wrapper(*args, **kwargs):
        # do something with fn(*args, **kwargs)
        pass

    return wrapper

def shout(fn):

    def wrapper(*args, **kwargs):
        return fn(name).upper()

    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please"

@shout
def lol():
    return f"lol"

__shows flexibility__
print(greet("Todd"))
print(order("burger", "fries"))
print(lol())

# preserving a function's metadata with functools @wraps

from functools import wraps

def log_function_data(fn):

    @wraps(fn) # preserve that "fn" metadata
    def wrapper(*args, **kwargs):

        '''I am a WRAPPER FUNCTION'''
        print(f"you are about to call {fn.__name__}")
        print(f"here is the documentation: {fn.__doc__}")

        return fn(*args, **kwargs) # function call

    return wrapper

@log_function_data
def add(x,y):

    '''adds two numbers together'''
    return x + y

print(add(10,30))
    # print(add.__doc__)
    # print(add.__name__)
    # help(add)

# enforce restrictions on arguments with decorators

from functools import wraps

def ensure_no_kwargs(fn):

    @wraps(fn) # preserve fn metadata
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed due to decorator restriction")

        return fn(*args, **kwargs)

    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hello {name}")

greet("Tony") # 'Hello Tony'

greet(name="Tony") # ValueError: No kwargs allowed due to decorator restriction

# decorators that take an argument

> when we write:
>
>       @decorator_with_args(arg)
>       def func(*args, **kwargs):
>           pass
>
> we're really doing is passing two things:
>
>       func = decorator_with_args(arg)(func)

from functools import wraps

def ensure_first_arg_is(val):

    def inner(fn): # inner accepts function arguments

        @wraps(fn)
        def wrapper(*args, **kwargs):

            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)

        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_foods(*args):
    print(args)

# enforce argument types with a decorator

def enforce(*types):

    def decorator(fn):

        def new_func(*args, **kwargs):
            # convert args into something mutable
            new_args = []
            for (a, t) in zip(args, types):
                new_args.append(t(a))
            return fn(*newargs, **kwargs)

        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a, b):
    print(a/b)
    return a/b

__without @enforce, code would break because it would try and loop with string x number of times instead of an int__

repeat_msg("hello", "3")

__without @enforce, code would break because it would try and divide with strings a and b__ 

divide('1', '2')
