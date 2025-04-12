from unittest import TestCase

from problem1.problem1 import Solution


class TestSolution(TestCase):
    def test_max_coins(self):
        solution = Solution()

        # Test 1
        assert 167 == solution.max_coins_recursive([3, 1, 5, 8], 0, 0)

        # Test 2
        assert 10 == solution.max_coins_recursive([1, 5], 0, 0)

        # Test 3
        assert 123 == solution.max_coins_recursive([7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3], 0, 0)
