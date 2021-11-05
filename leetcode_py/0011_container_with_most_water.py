# Source: Leetcode
# Difficulty: Medium

from typing import List

class Solution:
	def maxArea(self, height: List[int]) -> int:
		maxArea = 0
		i = 0
		j = len(height)-1
		while i < j:
			minHeight = min(height[i], height[j])
			maxArea = max(maxArea, minHeight*(j-i))
			if height[i] <= height[j]:
				i += 1
			else:
				j -= 1
		return maxArea
