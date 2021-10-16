class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		if len(p) == 0:
			if len(s) == 0:
				return True
			else:
				return False

		elif len(p) == 1:
			if len(s) == 1 and (p[0] == '.' or p[0] == s[0]):
				return True
			else:
				return False

		else:
			if p[1] == '*':
				if len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
					return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
				else:
					return self.isMatch(s, p[2:])

			elif len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
				return self.isMatch(s[1:], p[1:])
			else:
				return False
