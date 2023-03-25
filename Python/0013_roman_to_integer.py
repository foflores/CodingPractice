class Solution:
	def romanToInt(self, s: str) -> int:
		output = 0
		while s != "":
			if s[0] == 'M':
				output += 1000
				s = s[1:]
			elif s[0] == 'D':
				output += 500
				s = s[1:]
			elif s[0] == 'C':
				if len(s) > 1:
					if s[1] == 'D':
						output += 400
						s = s[2:]
					elif s[1] == 'M':
						output += 900
						s = s[2:]
					else:
						output += 100
						s = s[1:]
				else:
					output += 100
					s = s[1:]
			elif s[0] == 'L':
				output += 50
				s = s[1:]
			elif s[0] == 'X':
				if len(s) > 1:
					if s[1] == 'L':
						output += 40
						s = s[2:]
					elif s[1] == 'C':
						output += 90
						s = s[2:]
					else:
						output += 10
						s = s[1:]
				else:
					output += 10
					s = s[1:]
			elif s[0] == 'V':
				output += 5
				s = s[1:]
			elif s[0] == 'I':
				if len(s) > 1:
					if s[1] == 'V':
						output += 4
						s = s[2:]
					elif s[1] == 'X':
						output += 9
						s = s[2:]
					else:
						output += 1
						s = s[1:]
				else:
					output += 1
					s = s[1:]
		return output
