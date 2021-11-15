from typing import List

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		output = set()
		for i in range(len(nums)):
			l = i+1
			r = len(nums)-1
			while l < r:
				if nums[i] + nums[l] + nums[r] == 0:
					output.add((nums[i], nums[l], nums[r]))
					l += 1
				elif nums[i] + nums[l] + nums[r] < 0:
					l += 1
				else:
					r -= 1
		return list(output)
