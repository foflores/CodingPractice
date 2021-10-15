# Source: Leetcode
# Difficulty: Medium

class Solution:
	def myAtoi(self, s: str) -> int:
		s = s.lstrip()
		neg = False
		output = ""

		if s == "":
			return 0

		if s[0] in ['-','+']:
			if s[0] == '-':
				neg = True
			s = s[1:]

		for i in s:
			if not i.isdigit():
				break
			output += i

		if output == "":
			return 0

		output = int(output)
		if neg:
			output *= -1

		if output < -2**31:
			output = -2**31
		elif output > (2**31)-1:
			output = (2**31)-1

		return output
