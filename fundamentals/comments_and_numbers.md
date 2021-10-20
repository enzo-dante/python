# types of numbers in python

integer: a whole number
ex) -4

floating point: a decimal
ex) -4.1

complex and long are the 2 other python types that are rarely used

you can verify type of variable with function:
type(var)

# integer and float python calculations

1.0 + 4 = 5.0

Whenever doing math with both floats and ints together, the result is a float. Otherwise, we would lose any of the data after the float's decimal point.

ex) 

6 / 2 = 3.0

ex)

1/2 * 2 # + 1

By default, division in Python results in floats, not an int
- in this case 1/2 is 0.5 
- Multiplying 0.5 * 2 results in 1.0 not 1, because a float is involved. 
- The latter part of the line is ignored because of the '#' comment.

only when using // will dividing return an int;
- integer division is floored in Python, meaning it chops off the decimal point and returns the integer remaining.

16 // 6 = 2

# math operators

+ = addition
- = subtraction
* = multiplication
/ = division that always returns a float
** = exponents
% = modulo(get remainder)
// = integer division (will return only an integer even if return is a float)

modulo return the remaineder value

111 % 7 returns 6

modulo is often used to find if a number is even or odd when dividing by 2

13 % 2 returns 1(has remainder)

16 % 2 returns 0(no remainder and thus even)

# pemdas = order of operations

p = paranthesis
e = exponents
m = multiplication
d = division
a = addition
s = subtraction

ex:
1 + 9 * 10 = 91
(1 + 9) * 10 = 100

# round(variable, num_decimal_positions)

The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

https://www.w3schools.com/python/ref_func_round.asp

# randint(a, b)

generate a random number between a and b inclusive

ex)

import random

random.randint(0, 2) # random integer between 0, 1, or 2
