# why test driven development in python

writing code that tests your other code to ensure a level of performance quality when your app is in production.

it makes refactoring and collaboration safer and bug-free

# test driven development (TDD)

1. development begins by writing tests
2. once tests are written, write code to make tests pass
3. once tests pass, a feature is considered complete

> red, green, refactor TDD process

1. red = writes a test that fails
2. green = write the minimum amount of code necessary to make tests pass
3. refactor = clean up the code, while ensuring that tests still pass

# assertions (inferior)

> assertion statements (not a function) will assert that certain expressions must be True else raise an AssertionError
>
> there are superior methods to running tests than using assert like unit tests
>
> assertions warning = if a python file is run with the -O flag, assertions will not be evaluated

def add_positive_numbers(x,y):

__you cannot depend on assert statements because they can be ignored with an -O flag__

    assert x > 0 and y > 0, "Both numbers must be positive"
    return x + y

add_positive_numbers(1,1) # 2
add_positive_numbers(1,-1) # AssertionError: Both numbers must be positive

# doctests (inferior)

> doctest allow you to write tests for functions inside of the docstring, that uses triple quotes with triple greater sign
>
> MAJOR PROBLEM: syntax has to be exact like when expecting an Error, no trailing whitespaces, dictionary order is important, or comparing strings (must use single quotes)

def add(a, b):
    """
__the triple greater sign is the test__
    >>> add(2,3)
__5 is the expectation of that test__
    5
__the triple greater sign is the test__

    >>> add(100, 200)
__300 is the expectation of that test__
    300
    """
    return a+b

> to execute doctest directly, run:

python3 -m doctest -v file_name.py

# unittest built-in module

> unit testing is when you test smallest parts of an application in isolation and is the most popular and easiest method for testing

> STEP 1: setup testing infrastructure

__with TDD approach, first write tests in test.py before implementing method logic in activities.py__

> activities.py

def eat(food, is_healthy):
    pass

def nap(num_hours):
    pass

> tests.py

__import unittest module and functionality you want to test__

import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()

> STEP 2: write tests that you expect to FAIL

> tests.py

import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):

__for precision, write an instance method for each test case__

__since the tests are instance methods of ActivityTests, you need to use 'self'__

__add docstring to test functions to clarify purpose__

    def test_eat_healthy(self):

        """assert if a == b, eat healthy should have positive message"""
        self.assertEqual(
            # execute functionality with target input
            eat("broccoli", is_healthy=True),
            # define expected output
            "I'm eating broccoli, because my body is a temple."
        )

    def test_eat_unhealthy(self):

        """assert if a == b, eat unhealthy should have blase message"""
        self.assertEqual(
            # execute functionality with target input
            eat("pizza", is_healthy=False),
            # define expected output
            "I'm eating pizza, because YOLO!"
        )

    def test_short_nap(self):

        """assert if a == b, short naps should be refreshing"""
        self.assertEqual(
            # execute functionality with target input
            nap(1),
            # define expected output
            "I'm feeling refreshed after my 1 hour nap."
        )

    def test_long_nap(self):

        """assert if a == b, short naps should be discouraging"""
        self.assertEqual(
            # execute functionality with target input
            nap(3),
            # define expected output
            "Ugh I overslept. I didn't mean to nap for 3 hours."
        )

__run verbose tests: python3 tests.py -v__

expected behavior due to missing implementation:
FAILED (failures=4)

> STEP 3: write method implementation in activities.py and individually run tests

> activities.py

def eat(food, is_healthy):
    ending = "because YOLO!"
    return f"I'm eating {food}, {ending}"

__run tests and expect 1 less failure: python3 tests.py -v__

expected behavior due to missing implementation:
FAILED (failures=3)

__modify implementation with conditional logic to modify ending__

def eat(food, is_healthy):

    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple."

    return f"I'm eating {food}, {ending}"

__run tests and expect 2 less failure: python3 tests.py -v__

expected behavior due to missing nap implementation:
FAILED (failures=2)

__add nap implentation to nap method in activities.py -v__

def nap(num_hours):

    if num_hours >= 2:
        return f"Ugh I overslept.I didn't meant to nap for {num_hours}!"

__run tests and expect 3 less failure: python3 tests.py -v__

expected behavior due to missing nap implementation:
FAILED (failures=1)

def nap(num_hours):

    if num_hours >= 2:
        return f"Ugh I overslept.I didn't meant to nap for {num_hours}!"
    return "I'm feeling refreshed after my {num_hours} hour nap"

__run tests and expect 4 successful tests: python3 tests.py -v__

expected behavior due to missing nap implementation:

Ran 4 tests in 0.000s
OK

# unittests: Common Types of Assertions

self.assertEqual(x,y)
self.assertNotEqual(x,y)

self.assertTrue(x)
self.assertFalse(x)

self.assertsNone(x)
self.assertIsNotNone(x)

self.assertIn(x,y)
self.assertNotIn(x,y)

> STEP 1: setup testing infrastructure

> activities.py

def is_funny(person):
    pass

def laugh():
    pass

> tests.py

import unittest
from activities import is_funny, laugh

class ActivityTests(unittest.TestCase):

    def test_is_funny_tim(self):
        pass

    def test_is_funny_anyone_else(self):
        pass

    def test_laugh(self):
        pass

> STEP 2: write tests that you expect to FAIL

> tests.py

import unittest
from activities import is_funny, laugh

class ActivityTests(unittest.TestCase):

    def test_is_funny_tim(self):
        """tim should be funny"""

        self.assertEqual(
            is_funny("tim"),
            False
        )

__assertFalse(x) tests for Falsy values and can have an optional message__

        self.assertFalse(
            is_funny("tim"), "optional message"
        )

    def test_is_funny_anyone_else(self):
        """anyone else but tim should be funny"

__assertTrue(x) tests for Truthy values and can have an optional message__

        self.assertTrue(
            is_funny("blue"),
            "optional message"
        )

    def test_laugh(self):
        """check if the result of laugh is in tuple"""

        self.assertIn(
            laugh(),
            ("lol", "haha", "tehehe")
        )

> STEP 3: write method implementation in activities.py and individually run tests

> activities.py

from random import choice

def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    return choice(("lol", "haha", "tehehe"))

# unittests: testing for errors

__example 1__

import unittest

class SomeTests(unittest.TestCase):

    def testing_for_error(self):
        """testing for an error"""

        # pass in expected error type to be raised
        with self.assertRaises(IndexError):
            my_list = [1,2,3]
            my_list[100] # IndexError

__example 2__

> STEP 1: define infrastructure

> activities.py

def eat(food, is_healthy):
    pass

> tests.py

class ActivityTests(unittest.TestCase):

    def test_eat_healthy_boolean(self):
        pass

> STEP 2: write failing tests

> tests.py

class ActivityTests(unittest.TestCase):

    def test_eat_healthy_boolean(self):
        """is_healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

> STEP 3: implement logic and individually run tests

> activities.py

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean!")

    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"

__execute: python3 test.py -v__

# unittests: before and after hooks

setUp is a shared state that is run before each test method

tearDown is a function that removes a state after each test
- adding/removing data from a test database
- creating instances of a class

import unittest

class SomeTests(unittest.TestCase):

    def setUp(self):
        # do setup here
        pass

    def test_first(self):
        # setUp runs before
        # tearDown runs after
        pass

    def tearDown(self):
        # do teardown here
        pass