from unittest import TestCase

from problem4.problem4 import Solution

class TestSolution(TestCase):
    def test_is_palindrome(self):
        solution = Solution()

        # Test 1
        assert solution.is_palindrome("A man, a plan, a canal: Panama")

        # Test 2
        assert not solution.is_palindrome("race a car")

        # Test 3
        assert solution.is_palindrome(" ")

        # Test 4
        assert solution.is_palindrome(",.")
