from typing import List

class Solution:

    def max_coins_recursive(self, nums: List[int], index: int, profit: int) -> int:
        if index == len(nums) or len(nums) == 0:
            return profit

        # Choice 1: Pop the balloon at the current index
        less_index_value = 1
        if index > 0:
            less_index_value = nums[index - 1]
        greater_index_value = 1
        if index < len(nums) - 1:
            greater_index_value = nums[index + 1]

        popped_balloon = nums.pop(index)
        choice_1 = self.max_coins_recursive(nums, 0, profit + less_index_value * greater_index_value * popped_balloon)

        # Choice 2: Reinsert the popped balloon and skip the current balloon at current index
        nums.insert(index, popped_balloon)
        choice_2 = self.max_coins_recursive(nums, index + 1, profit)

        return max(choice_1, choice_2)

    def max_coins(self, nums: List[int]) -> int:
        return self.max_coins_recursive(nums, 0, 0)
