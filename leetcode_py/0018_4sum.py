from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums.sort()
		output = set()
		if len(nums) < 4:
			return []
		for i in range(len(nums)-3):
			for j in range(i+1, len(nums)-2):
				k = j+1
				m = len(nums)-1
				while k < m:
					nums2 = [nums[i], nums[j], nums[k], nums[m]]
					if sum(nums2) == target:
						nums2.sort()
						output.add(tuple(nums2))
						k += 1
					elif sum(nums2) < target:
						k += 1
					else:
						m -= 1

		return list(output)
