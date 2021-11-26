from typing import List, Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self) -> str:
			return f"{self.val}, {self.next}"


class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		mergedLists = []
		mergedList = []
		head = None
		while len(lists) > 1:
			for i in range(len(lists)//2):
				l1, l2 = lists[i*2], lists[i*2+1]

				if l1 == l2 == None:
					continue
				if l1 is None:
					mergedLists.append(l2)
					continue
				if l2 is None:
					mergedLists.append(l1)
					continue

				if l1.val < l2.val:
					head = l1
					mergedList = l1
					l1 = l1.next
				else:
					head = l2
					mergedList = l2
					l2 = l2.next

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
				mergedLists.append(mergedList)
				mergedList = []
			if len(lists)%2 == 1:
				mergedLists.append(lists[len(lists)-1])
			lists = mergedLists
			mergedLists = []
		if lists == []:
			return None
		return lists[0]
