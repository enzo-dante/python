# lambdas: a single line anonymous functions

> syntax: lambda {parameters}: {automatically_returned_single_expression}
>
> lambdas are used to pass a function into another function

lambda a,b: a + b # adds the parameters a and b together on call of lambda

__lambdas can be stored in a variable, but that is uncommon__

cube = lambda n: n**3

# map:

> a function that accepts at least 2 arguments, a function and an iterable, and runs the lambda for each value in the iterable & returns a map object which can be converted into another data structure

nums = [2,4,6,8,10]

doubles = map(lambda x : x*2, nums) # map this lambda to the nums list by calling the lambda on every item in nums

__returned map objects can only be iterated over once, like converting the map into a list__

doubles = list(map(lambda x : x*2, nums))

letters = ["a", "b", "c", "d"]

peeps = map(lambda letter: letter.upper(), letters) # ["A", "B", "C", "D"]

# filter: a function that uses a lambda that takes a collection as an argument and filter out specific values

__make sure to convert the filter object into a list afterward__

ex:
nums = [1,2,3]
evens = list(filter(lambda n: n % 2 == 0, nums))
evens # [2,4]

ex:
names = ["angel", "ben", "ally"]
a_names = list(filter(lambda n: n[0] == "a", names)) # filters out all names that start with 'a'