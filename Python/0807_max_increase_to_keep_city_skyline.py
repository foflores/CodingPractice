from typing import List


class Solution:
	def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
		maxRow = []
		maxCol = []
		output = 0

		for i in range(len(grid)):
			currentMaxRow = 0
			currentMaxCol = 0
			for j in range(len(grid)):
				currentMaxRow = max(currentMaxRow, grid[i][j])
				currentMaxCol = max(currentMaxCol, grid[j][i])
			maxCol.append(currentMaxCol)
			maxRow.append(currentMaxRow)

		for i in range(len(grid)):
			for j in range(len(grid)):
				minOfMax = min(maxRow[i], maxCol[j])
				newHeight= max(grid[i][j], minOfMax)
				output += newHeight - grid[i][j]

		return output
