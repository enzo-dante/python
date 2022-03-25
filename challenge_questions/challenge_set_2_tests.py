import unittest
from challenge_set_2 import get_letter_r, print_four_expressions, vowel_count

class ChallengeSet2Tests(unittest.TestCase):
    
    def print_four_expressions_test(self):
        """should return 100"""
        self.assertEqual(print_four_expressions(), 100)

    def get_letter_r_test(self):
        """should return 'r' letter"""
        self.assertEqual(get_letter_r(), "r")
    
    def vowel_count_test(self):
        """should returns a dictionary with the key as vowels & values as the count of times that vowel appears in the str"""
        awesome = "awesome"
        target = {'a': 1, 'e': 2, 'o': 1}

        self.assertEqual(vowel_count(awesome), target)

# python3 challenge_set_2_tests.py -v

if __name__ == "__main__":
    unittest.main()
    