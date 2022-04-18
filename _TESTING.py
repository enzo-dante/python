"""
    ! Test Driven Development (TDD)
        writing code that tests your other code to ensure a level of performance quality when your app is in production.
        TDD makes refactoring and collaboration safer and bug-free

    ! TDD STEPS

        * 1. development BEGINS by writing RED failing tests

        * 2. once tests are written, write the MINIMUM amount of GREEN code necessary to make tests pass

        * 3. refactor = clean up the code, while ensuring that tests still pass

        * 4. once tests pass, a feature is considered complete
"""

"""
    ! unittest.Testcase

        * unit testing is when you test smallest parts of an application in isolation and is the most popular and easiest method for testing

    ! common types of assertions

        self.assertEqual(x,y)
        self.assertNotEqual(x,y)

        self.assertTrue(x)

            assertTrue(x, "optional fail msg") tests for Truthy values and can have an optional message

        self.assertFalse(x)

            assertFalse(x, "optional fail msg") tests for Falsy values and can have an optional message

        self.assertsNone(x)
        self.assertIsNotNone(x)

        self.assertIn(x,y)
        self.assertNotIn(x,y)

            self.assertIn(
                laugh(),
                ("lol", "haha", "tehehe")
            )
"""

# ? STEP 1: setup unittest.Testcase infrastructure in file.py

def eat(foot, is_healthy):
    pass


# ? STEP 2: import unittest module and method you want to test into test.py

import unittest
from activities import eat

class ActivityTests(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()

# ? STEP 3: write tests that you expect to FAIL

import unittest
from activities import eat

class ActivityTests(unittest.TestCase):

    # for precision, write an instance method for each test case
    # since the tests are instance methods of ActivityTests, you need to use 'self'
    def test_eat_healthy(self):
        """assert if a == b, eat healthy should have positive message"""
        self.assertEqual(
            # execute functionality with target input
            eat("broccoli", is_healthy=True),
            # define expected output
            "I'm eating broccoli, because my body is a temple."
        )

if __name__ == "__main__":
    unittest.main()

# ? STEP 4: run verbose FAILING tests in terminal

"""
python3 tests.py -v

    expected behavior due to missing implementation:
    FAILED (failures=4)
"""

# ? STEP 5: write method implementation in file.py

def eat(food, is_healthy):

    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple."

    return f"I'm eating {food}, {ending}"

# ? STEP 6: individually run implemented functions until all failing tests resolved in tests.py

"""
python3 tests.py -v

    Ran 4 tests in 0.000s
    OK
"""