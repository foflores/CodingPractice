class Solution:
	def isPalindrome(self, x: int) -> bool:
		numStr:str = str(x)
		return numStr == numStr[::-1]
