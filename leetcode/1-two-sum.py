'''
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
'''

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        past = {}
        for i in range(0, len(nums)):
            if nums[i] in past.keys():
                return[past[nums[i]], i]
            past[target - nums[i]] = i
        return []


solution = Solution()

assert(solution.two_sum([2, 7, 11, 15], 9) == [0, 1])
assert(solution.two_sum([3, 2, 4], 6) == [1, 2])
assert(solution.two_sum([3, 3], 6) == [0, 1])
