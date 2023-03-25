from typing import List

class Solution:
	def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
		x = len(mat)
		y = len(mat[0])

		for i in range(x):
			temp = []
			m = i
			n = 0
			while m < x and n < y:
				temp.append(mat[m][n])
				m += 1
				n += 1
			temp.sort()
			m = i
			n = 0
			while m < x and n < y:
				mat[m][n] = temp.pop(0)
				m += 1
				n += 1

		for j in range(1,y):
			temp = []
			m = 0
			n = j
			while m < x and n < y:
				temp.append(mat[m][n])
				m += 1
				n += 1
			temp.sort()
			m = 0
			n = j
			while n < len(mat[0]) and m < len(mat):
				mat[m][n] = temp.pop(0)
				m += 1
				n += 1
		return mat

test = Solution()
print(test.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
# [1,2,3,4],
# [3,4,5,6],
# [5,6,7,8]]
