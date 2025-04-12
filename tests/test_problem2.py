from unittest import TestCase
from problem2.problem2 import Solution, ListNode

class TestSolution(TestCase):
    def test_swap_pairs(self):
        solution = Solution()

        # Test 1
        list_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result_1 = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
        assert f"{solution.swap_pairs(list_1)}" == f"{result_1}"

        # Test 2
        list_2 = ListNode(1, ListNode(2, ListNode(3)))
        result_2 = ListNode(2, ListNode(1, ListNode(3)))
        assert f"{solution.swap_pairs(list_2)}" == f"{result_2}"

        # Test 3  [2,5,3,4,6,2,2] [5,2,4,3,2,6,2
        list_3 = ListNode(2, ListNode(5, ListNode(3, ListNode(4, ListNode(6, ListNode(2, ListNode(2)))))))
        result_3 = ListNode(5, ListNode(2, ListNode(4, ListNode(3, ListNode(2, ListNode(6, ListNode(2)))))))
        assert f"{solution.swap_pairs(list_3)}" == f"{result_3}"
