from typing import List


class Solution:
	def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
		groups = {}
		output = []

		for i, j in enumerate(groupSizes):
			if j not in groups:
				groups[j] = [i]
			else:
				groups[j].append(i)

		for i in groups:
			chunks = [groups[i][j:j+i] for j in range(0,len(groups[i]), i)]
			output.extend(chunks)

		return output
