# Source: Leetcode
# Difficulty: Medium

from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		num = 0
		count = 0
		while l1 or l2:
			if l1:
				num += l1.val * (10**count)
				l1 = l1.next
			if l2:
				num += l2.val * (10**count)
				l2 = l2.next
			count += 1

		output = ListNode()
		node = output
		while num > 0:
			node.val = num % 10
			num //= 10
			if num > 0:
				node.next = ListNode()
				node = node.next

		return output
