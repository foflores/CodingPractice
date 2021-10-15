# Source: Leetcode
# Difficulty: Medium

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s) == 1:
			return 1
		seen = []
		maxCount = 0
		count = 0
		for i in s:
			if i in seen:
				index = seen.index(i)
				seen = seen[seen.index(i)+1:]
				count -= index+1
			seen.append(i)
			count += 1
			maxCount = max(maxCount, count)
		return maxCount
