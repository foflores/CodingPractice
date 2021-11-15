from typing import List


class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		output = nums[0] + nums[1] + nums[2]
		for i in range(len(nums)):
			l = i+1
			r = len(nums)-1
			while l < r:
				distance = abs(target - output)
				currentSum = nums[i] + nums[l] + nums[r]

				if currentSum <= target:
					l += 1
				else:
					r -= 1

				if abs(target-currentSum) < distance:
					output = currentSum
		return output
