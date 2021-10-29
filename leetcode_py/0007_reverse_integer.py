# Source: Leetcode
# Difficulty: Medium

class Solution:
	def reverse(self, x: int) -> int:
		x2 = x
		reverse = 0
		neg = False
		if abs(x) != x:
			neg = True
			x2 = -x

		count = 0
		while x2:
			digit = x2 % 10
			x2 //= 10
			if (reverse * 10) + digit >= (2**31)-1:
				return 0
			reverse = (reverse * 10) + digit

		if neg:
			reverse = -reverse

		return reverse


test = Solution()
print(test.reverse(12397))
