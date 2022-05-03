import unittest
from challenge_set_2 import find_the_duplicate, find_greater_numbers, letter_counter, is_odd_string, min_max_key_in_dictionary, mode, nth, reverse_vowels, reverse_swap_vowels, running_average, same_frequency, sum_up_diagonals, three_odd_numbers, two_oldest_ages, valid_parentheses

# python3 challenge_set_2_tests.py -v
class ChallengeSet2Tests(unittest.TestCase):

    def setUp(self):
        self.vowels = "aeiou"

    def test_true_same_frequency(self):
        """assert is truthy, returns True if they contain the same frequency of digits, else return False"""
        a = same_frequency(551122,221515) # True
        self.assertTrue(a)
        a = same_frequency(1212, 2211) # True
        self.assertTrue(a)

    def test_false_same_frequency(self):
        """assert is falsy, returns False if they don't contain the same frequency of digits, else return False"""
        a = same_frequency(321142,3212215) # False
        self.assertFalse(a)

    def test_nth(self):
        """assert a == b, returns the element at whatever index is the number in the list"""

        a = nth(['a', 'b', 'c', 'd'], 1)
        b = 'b'
        self.assertEqual(a, b)
        a = nth(['a', 'b', 'c', 'd'], -2)
        b = 'c'
        self.assertEqual(a, b)
        a = nth(['a', 'b', 'c', 'd'], 0)
        b = 'a'
        self.assertEqual(a, b)
        a = nth(['a', 'b', 'c', 'd'], -4)
        b = 'a'
        self.assertEqual(a, b)
        a = nth(['a', 'b', 'c', 'd'], -1)
        b = 'd'
        self.assertEqual(a, b)
        a = nth(['a', 'b', 'c', 'd'], 3)
        b = 'd'
        self.assertEqual(a, b)

    def test_find_the_duplicate(self):
        """assert a == b, returns the duplicate number or None"""
        a = find_the_duplicate([1,2,1,4,3,12])
        b = 1
        self.assertEqual(a,b)

        a = find_the_duplicate([6,1,9,5,3,4,9])
        b = 9
        self.assertEqual(a,b)

        a = find_the_duplicate([2,1,3,4])
        b = None
        self.assertEqual(a,b)

    def test_sum_up_diagonals(self):
        """assert a == b, returns a sum of the two main diagonals in the array"""
        test_one = [
            [1,2],
            [3,4]
        ]

        a = sum_up_diagonals(test_one)
        b = 10
        self.assertEqual(a,b)

        test_two = [
          [ 1, 2, 3 ],
          [ 4, 5, 6 ],
          [ 7, 8, 9 ]
        ]

        a = sum_up_diagonals(test_two)
        b = 30
        self.assertEqual(a,b)

        test_three = [
          [ 4, 1, 0 ],
          [ -1, -1, 0],
          [ 0, 0, 9]
        ]

        a = sum_up_diagonals(test_three) # 11
        b = 11
        self.assertEqual(a,b)

        test_four = [
          [ 1, 2, 3, 4 ],
          [ 5, 6, 7, 8 ],
          [ 9, 10, 11, 12 ],
          [ 13, 14, 15, 16 ]
        ]

        a = sum_up_diagonals(test_four) # 68
        b = 68
        self.assertEqual(a,b)

    def test_min_max_key_in_dictionary(self):
        test_one = {2:'a', 7:'b', 1:'c',10:'d',4:'e'}
        a = min_max_key_in_dictionary(test_one)
        print(a)
        b = [1,10]
        self.assertEqual(a,b)

        test_two = {1: "Ellie", 4:"Matt", 2: "Tim"}
        a = min_max_key_in_dictionary(test_two)
        b = [1,4]
        self.assertEqual(a,b)

    def test_find_greater_numbers(self):
        """assert a == b, returns the number of times a number is followed by a larger number across the entire list"""

        a = find_greater_numbers([1,2,3]) # 3
        b = 3
        self.assertEqual(a, b)

        a = find_greater_numbers([6,1,2,7]) # 4
        b = 4
        self.assertEqual(a, b)

        a = find_greater_numbers([5,4,3,2,1]) # 0
        b = 0
        self.assertEqual(a, b)

        a = find_greater_numbers([]) # 0
        b = 0
        self.assertEqual(a, b)

    def test_two_oldest_ages(self):
        """assert a == b,"""

        a = two_oldest_ages( [1, 2, 10, 8] )
        b = [8, 10]
        self.assertEqual(a, b)

        a = two_oldest_ages( [6,1,9,10,4] )
        b = [9,10]
        self.assertEqual(a, b)

        a = two_oldest_ages( [4,25,3,20,19,5] )
        b = [20,25]
        self.assertEqual(a, b)

    def test_truthy_is_odd_string(self):
        """assert is truthy,"""

        test_one = is_odd_string('a')
        self.assertTrue(test_one)

        test_two = is_odd_string('amazing')
        self.assertTrue(test_two)

        test_three = is_odd_string('veryfun')
        self.assertTrue(test_three)

    def test_falsy_is_odd_string(self):
        """assert is falsy,"""

        test_one = is_odd_string('aaaa')
        self.assertFalse(test_one)

        test_two = is_odd_string('veryfunny')
        self.assertFalse(test_two)

    def test_truthy_valid_parentheses(self):
        """assert is truthy,"""

        test_one = valid_parentheses("()")
        self.assertTrue(test_one)

        test_two = valid_parentheses("(())((()())())")
        self.assertTrue(test_two)

    def test_falsy_valid_parentheses(self):
        """assert is falsy,"""

        test_one = valid_parentheses(")(()))")
        self.assertFalse(test_one)

        test_two = valid_parentheses("(")
        self.assertFalse(test_two)

        test_three = valid_parentheses("))((")
        self.assertFalse(test_three)

        test_four = valid_parentheses("())(")
        self.assertFalse(test_four)

        test_five = valid_parentheses("()()()()())()(")
        self.assertFalse(test_five)

        test_six = valid_parentheses("")
        self.assertFalse(test_six)

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

    def test_correct_letter_counter(self):
        """assert a == b, returns frequency of letter in str from letter_counter function"""

        counter = letter_counter('Amazing')

        a = counter('a')
        b = 2
        self.assertEqual(a, b)

        a = counter('m')
        b = 1
        self.assertEqual(a, b)

        counter2 = letter_counter('This Is Really Fun!')
        a = counter2('i')
        b = 2
        self.assertEqual(a, b)

        a = counter2('t')
        b = 1
        self.assertEqual(a, b)

    def test_incorrect_letter_counter(self):
        """assert a == b, returns frequency of letter in str from letter_counter function"""
        counter = letter_counter('Amazing')

        a = counter('a')
        b = 10
        self.assertNotEqual(a, b)

if __name__ == "__main__":
    unittest.main()
