
from typing import List

class Solution:
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        mid = 0
        while lb < ub:
            mid = int((lb + ub) / 2)
            if nums[mid] < target:
                lb = mid + 1
            elif nums[mid] > target:
                ub = mid - 1
            else:
                return mid

        if ub == lb:
            if ub == len(nums) - 1:
                return ub + 1 if target > nums[ub] else ub - 1
            elif ub == 0:
                return ub if target < nums[ub] else ub + 1
        return mid