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