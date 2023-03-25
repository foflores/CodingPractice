from typing import List


class Solution:
	def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
		arr = []
		for i, j in enumerate(nums):
			arr.append([j, i])

		arr.sort()

		for i in range(len(arr)):
			for j in range(i+1, len(arr)):
				print(f"{i}, {j}")
				if abs(arr[i][0] - arr[j][0]) > t:
					break
				if abs(arr[i][1] - arr[j][1]) > k:
					continue
				return True
		return False

nums = [1,5,9,1,5,9]
test = Solution()
print(test.containsNearbyAlmostDuplicate(nums, 2, 3))
