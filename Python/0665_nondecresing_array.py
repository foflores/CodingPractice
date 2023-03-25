from typing import List


class Solution:
	def checkPossibility(self, nums: List[int]) -> bool:
		count = 0
		if len(nums) <= 2:
			return True
		for i in range(len(nums)):
			if i == 0:
				continue
			if nums[i-1] > nums[i]:
				count += 1
				if i != 1 and i != len(nums)-1:
					if nums[i-1] <= nums[i+1]:
						nums[i] = nums[i-1]
						count += 1
					else:
						nums[i-1] = nums[i]
						count += 1
						if nums[i-2] > nums[i-1]:
							return False

			if count >= 2:
				return False

		return True

test = [1,5,4,6,7,10,8,9]
sol = Solution()
print(sol.checkPossibility(test))
