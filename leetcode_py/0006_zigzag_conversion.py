# Source: Leetcode
# Difficulty: Medium

class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if len(s) <= numRows or numRows == 1:
			return s

		output = ""
		for i in range(numRows):
			gap1 = (numRows-1-i)*2
			gap2 = i*2
			j = i

			if i == 0:
				while j < len(s):
					output += s[j]
					j += gap1

			elif i == numRows-1:
				while j < len(s):
					output += s[j]
					j += gap2

			else:
				toggle = True
				while j < len(s):
					output += s[j]
					if toggle:
						j += gap1
						toggle = False
					else:
						j += gap2
						toggle = True

		return output
