import unittest
from challenge_set_2 import mode, reverse_vowels, reverse_swap_vowels, running_average, three_odd_numbers

# python3 challenge_set_2_tests.py -v
class ChallengeSet2Tests(unittest.TestCase):

    def setUp(self):
        self.vowels = "aeiou"

    def test_reverse_swap_vowels(self):
        """assert a == b, returns string with swapped vowels & incremented & decremented indices"""
        a, i, j = reverse_swap_vowels(list(self.vowels), 0, len(self.vowels) - 1)
        b = "ueioa"

        self.assertEqual("".join(a), b)
        self.assertEqual(i, 1)
        self.assertEqual(j, 3)

    def test_reverse_vowels(self):
        """assert a == b, returns string with reverse only vowels"""

        a = reverse_vowels(self.vowels)
        b = "uoiea"
        self.assertEqual(a, b)

    def test_reverse_uppercase_vowels(self):
        """assert a == b, returns reverse vowel string that preserves casing"""

        a = reverse_vowels("Reverse Vowels In A String") 
        b = "RivArsI Vewols en e Streng"
        self.assertEqual(a, b)

    def test_truthy_three_odd_numbers(self):
        """assert True, returns True if any three consecutive numbers sum to an odd number"""

        numbers = [1,2,3,4,5]
        is_truthy = three_odd_numbers(numbers)
        self.assertTrue(is_truthy, "consecutive numbers sum is NOT odd")

        is_truthy = three_odd_numbers([0,-2,4,1,9,12,4,1,0])
        self.assertTrue(is_truthy, "consecutive numbers sum is NOT odd")


    def test_falsy_three_odd_numbers(self):
        """assert False, returns False if any three consecutive numbers sum to an odd number"""

        numbers = [5,2,1]
        is_falsy = three_odd_numbers(numbers)
        self.assertFalse(is_falsy, "consecutive numbers sum is NOT odd")

    def test_mode(self):
        """assert if a == b, mode should return most frequent number in the list"""
        nums = [2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]

        a = mode(nums)
        b = 4

        self.assertEqual(a, b)

    def test_incorrect_mode(self):
        """assert if a != b, mode should NOT return most frequent number in the list"""
        nums = [2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]

        a = mode(nums)
        b = 1

        self.assertNotEqual(a, b)

    def test_running_average(self):
        """assert a == b, running average increments"""
        rAvg = running_average()
        rAvg(1)

        a = rAvg(3)
        b = 2

        self.assertEqual(a, b)

    def test_incorrect_running_average(self):
        """assert a != b, running average increments incorrectly"""
        rAvg = running_average()
        rAvg(1)

        a = rAvg(2)
        b = 2

        self.assertNotEqual(a, b)

if __name__ == "__main__":
    unittest.main()
    