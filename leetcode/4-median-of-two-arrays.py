'''
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n
respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
'''

from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        before_last_number = 0
        last_number = 0

        for i in range(int(total_length / 2) + 1):
            before_last_number = last_number
            if len(nums1) and len(nums2) and (nums1[0] < nums2[0]):
                last_number = nums1.pop(0)
            elif len(nums2):
                last_number = nums2.pop(0)
            elif len(nums1):
                last_number = nums1.pop(0)

        if total_length % 2 == 0:
            return (last_number + before_last_number) / 2
        else:
            return last_number
