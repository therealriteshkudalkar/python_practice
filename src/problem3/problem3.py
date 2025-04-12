
from typing import List

class Solution:
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        while lb < ub:
            mid = int((lb + ub) / 2)
            if nums[mid] < target:
                lb = mid + 1
            elif nums[mid] > target:
                ub = mid - 1
            else:
                return mid

        if ub == lb:
            return ub + 1 if target > nums[ub] else ub

        # lb > ub
        if lb >= 0:
            return lb if target < nums[lb] else lb + 1
        if ub < len(nums):
            return ub + 1 if target > nums[ub] else ub
        return 0