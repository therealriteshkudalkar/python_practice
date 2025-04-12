from unittest import TestCase
from problem3.problem3 import Solution

class TestSolution(TestCase):
    def test_search_insert(self):
        solution = Solution()

        # Test 1
        assert 2 == solution.search_insert([1, 3, 5, 6], 5)

        # Test 2
        assert 1 == solution.search_insert([1, 3, 5, 6], 2)

        # Test 3
        assert 4 == solution.search_insert([1, 3, 5, 6], 7)

        # Test 4
        assert 0 == solution.search_insert([1, 3, 5, 6], 0)

        # Test 5
        assert 0 == solution.search_insert([1, 3], 0)

        # Test 6
        assert 2 == solution.search_insert([1, 3], 4)
