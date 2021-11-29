from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if not head or not head.next or k == 1:
			return head

		start = None
		prevNode = None
		currentNode = head
		nextNode = head.next
		counter = 0
		firstLoop = True
		keepGoing = True

		while True:
			temp = currentNode
			tempCounter = k
			while temp and tempCounter > 0:
				temp = temp.next
				tempCounter -= 1
			if tempCounter != 0:
				break

			if counter == 0:
				currentNode.next = None
				counter += 1

			while counter < k:
				prevNode = currentNode
				currentNode = nextNode
				nextNode = nextNode.next
				currentNode.next = prevNode
				counter += 1

			if firstLoop:
				head = currentNode
				firstLoop = False
			else:
				start.next = currentNode

			while currentNode.next:
				currentNode = currentNode.next

			currentNode.next = nextNode

			if not nextNode:
				break

			start = currentNode
			currentNode = nextNode
			nextNode = nextNode.next
			counter = 0
		return head

lst = ListNode(1,ListNode(2))
test = Solution()
print(test.reverseKGroup(lst,2))
