from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if list1 and list2:
			l1, l2 = list1.next, list2
			output = list1
			head = list1
			if list2.val < list1.val:
				l1, l2 = list1, list2.next
				output = list2
				head = list2
		elif list1:
			return list1
		else:
			return list2

		while l1 and l2:
			if l1.val < l2.val:
				head.next = l1
				l1 = l1.next
			else:
				head.next = l2
				l2 = l2.next
			head = head.next

		if l1:
			head.next = l1
		if l2:
			head.next = l2
		return output
