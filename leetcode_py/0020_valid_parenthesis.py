class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		counter = 0
		braces = {
			')':'(',
			'}':'{',
			']':'['
		}
		for paren in s:
			if paren in ['(', '{', '[']:
				stack.append(paren)
				counter += 1

			elif stack != [] and stack[len(stack)-1] == braces[paren]:
				stack.pop()
				counter -= 1

			else:
				return False
		return counter == 0
