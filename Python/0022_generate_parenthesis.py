from typing import List


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		output = []
		return self.genParenthesisHelper(n, n, output, "")

	def genParenthesisHelper(self, l, r, output, current):
		if l == r == 0:
			output.append(current)

		elif l == 0:
			output = self.genParenthesisHelper(l, r-1, output, current+')')

		elif r in [0, l]:
			output = self.genParenthesisHelper(l-1, r, output, current+'(')

		else:
			output = self.genParenthesisHelper(l-1, r, output, current+'(')
			output = self.genParenthesisHelper(l, r-1, output, current+')')

		return output
