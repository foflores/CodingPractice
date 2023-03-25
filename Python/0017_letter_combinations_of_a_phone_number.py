from typing import List


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		letterMappings = {
			2 : "abc", 3 : "def",
			4 : "ghi", 5 : "jkl",
			6 : "mno", 7 : "pqrs",
			8 : "tuv", 9 : "wxyz",
		}
		return self.combinationsHelper(digits, letterMappings)

	def combinationsHelper(self, digits, mappings):
		output = []

		if len(digits) == 1:
			letters = mappings[int(digits[0])]
			for let in letters:
				output.append(let)

		elif len(digits) > 1:
			output2 = self.combinationsHelper(digits[1:], mappings)

			letters = mappings[int(digits[0])]
			for let in letters:
				for combo in output2:
					output.append(let+combo)

		return output
