'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two
numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode()
        head = result

        while l1 or l2 or carry:
            sum_nodes = 0
            if (l1 and l2):
                sum_nodes = l1.val + l2.val
            elif l1:
                sum_nodes = l1.val
            elif l2:
                sum_nodes = l2.val

            if carry:
                sum_nodes += carry
                carry = 0

            if sum_nodes >= 10:
                carry = 1
                sum_nodes -= 10

            result.val = sum_nodes

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 or l2 or carry:
                result.next = ListNode()
                result = result.next

        return head
