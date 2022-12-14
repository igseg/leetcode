# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

import numpy as np

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, elem in enumerate(nums):

            aux_nums = nums[idx+1:]

            condition = (np.array(aux_nums) == (target - elem))

            if np.sum(condition) == 0:
                continue

            idx_2 = np.where(condition)[0][0]

            return [idx, idx_2+1+idx]
