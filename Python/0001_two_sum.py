# Source: Leetcode
# Difficulty: Easy

from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		seen = dict()
		for i in range(len(nums)):
			if nums[i] in seen:
				return (seen[nums[i]], i)
			else:
				seen[target-nums[i]] = i
