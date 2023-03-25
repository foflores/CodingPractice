from typing import List


# Attempt 1: O(n^2)
class Solution:
	def minOperations(self, boxes: str) -> List[int]:
		output = [0] * len(boxes)

		for i in range(len(boxes)):
			for j in range(len(output)):
				if boxes[i] == "1":
					output[j] += abs(i-j)

		return output

# Attempt 2: O(n^2)
# Improved performance using list comprehension
class Solution2:
	def minOperations(self, boxes: str) -> List[int]:
		output = [0] * len(boxes)

		for i in range(len(boxes)):
			if boxes[i] == "1":
				arr = [j for j in range(i,-1, -1)]
				arr.extend([j for j in range(1,len(boxes)-i)])
				output = [j+k for j,k in zip(arr,output)]

		return output

# Attempt 3: O(n)
# Calculated answer to the first index in linear time and then used sliding window to calculate
# the answer to each next index in constant time. Resulting in overall linear time complexity.
class Solution3:
	def minOperations(self, boxes: str) -> List[int]:
		output = []
		l = 0
		r = 0
		current = 0
		for i, j in enumerate(boxes):
			if j == "1":
				r += 1
				current += i

		for i, j in enumerate(boxes):
			if i == 0:
				output.append(current)
			if j == "1":
				l += 1
				r -= 1
			current += l - r
			output.append(current)

		return output[0:-1]
