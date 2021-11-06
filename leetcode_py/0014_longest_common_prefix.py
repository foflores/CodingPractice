from typing import List

class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		index = 0
		prefix = ""
		keepGoing = True
		while keepGoing:
			currentLetter = ""
			for i in range(len(strs)):
				if index < len(strs[i]):
					if i == 0:
						currentLetter = strs[i][index]
					elif currentLetter != strs[i][index]:
						keepGoing = False
						break
				else:
					keepGoing = False
					break
			if keepGoing:
				prefix += strs[0][index]
				index += 1
		return prefix
