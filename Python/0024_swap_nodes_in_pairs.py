from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head and head.next:
			output = head.next
		else:
			return head

		prevHead = head
		head = head.next
		while head:
			prevHead.next = head.next
			head.next = prevHead

			if prevHead.next:
				head = prevHead.next
				if prevHead.next.next:
					prevHead.next = head.next
					prevHead = head
					head = head.next
				else:
					break
			else:
				break
		return output

lst = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
test = Solution()
print(test.swapPairs(lst))
