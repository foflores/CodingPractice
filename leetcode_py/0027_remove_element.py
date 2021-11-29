from typing import List


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		if len(nums) == 1 and nums[0] != val:
			return 1
		elif len(nums) < 2:
			return 0

		i = 0
		while i < len(nums):
			if nums[i] == val:
				nums.pop(i)
			else:
				i += 1

		return len(nums)
