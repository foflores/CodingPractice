# Source: Leetcode
# Difficulty: Hard

from typing import List

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		totalLen = len(nums1) + len(nums2)
		isEven = totalLen % 2 == 0
		midpoint = totalLen//2

		i = 0
		j = 0
		num1 = 0
		num2 = 0
		for k in range(midpoint+1):
			num2 = num1
			if i < len(nums1) and j < len(nums2):
				if nums1[i] <= nums2[j]:
					num1 = nums1[i]
					i += 1
				else:
					num1 = nums2[j]
					j += 1
			elif i < len(nums1):
				num1 = nums1[i]
				i += 1
			else:
				num1 = nums2[j]
				j += 1

		if isEven:
			return (num1+num2)/2
		else:
			return num1
