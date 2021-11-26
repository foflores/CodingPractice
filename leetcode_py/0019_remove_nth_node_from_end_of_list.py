from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		node = head
		nodePrev = None
		nodeTarget = head

		if not head.next and n == 1:
			return None

		while node.next:
			if n == 1:
				node = node.next
				nodePrev = nodeTarget
				nodeTarget = nodeTarget.next

			else:
				node = node.next
				n -= 1
				continue

		if nodePrev:
			nodePrev.next = nodeTarget.next
		else:
			return head.next
		return head
