# Source: Leetcode
# Difficulty: Medium

class Solution:
	def longestPalindrome(self, s: str) -> str:
		if len(s) < 2:
			return s
		output = ""
		for i in range(len(s)-1):
			substr = s[i]
			j = i-1
			k = i+1
			while 0 <= j and k < len(s) and s[j] == s[k]:
				substr = s[j] + substr + s[k]
				j -= 1
				k += 1
			if len(output) < len(substr):
				output = substr

			if s[i] == s[i+1]:
				substr = s[i:i+2]
				j = i-1
				k = i+2
				while 0 <= j and k < len(s) and s[j] == s[k]:
					substr = s[j] + substr + s[k]
					j -= 1
					k += 1
				if len(output) < len(substr):
					output = substr
		return output
