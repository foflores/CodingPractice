# Source: Leetcode
# Difficulty: Medium

class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		cache = {}
		def subseq(i, j) -> int:
			if i >= len(text1) or j >= len(text2):
				return 0

			if text1[i] == text2[j]:
				if (i+1,j+1) not in cache:
					cache[(i+1,j+1)] = subseq(i+1, j+1)
				return 1 + cache[(i+1,j+1)]
			else:
				if (i+1,j) not in cache:
					cache[(i+1,j)] = subseq(i+1, j)
				if (i,j+1) not in cache:
					cache[(i,j+1)] = subseq(i, j+1)
				return max(cache[(i+1,j)], cache[(i,j+1)])
		return subseq(0,0)

test = Solution()
print(test.longestCommonSubsequence("oxcpqrsvwf","shmtulqrypy"))
# "abcde"
# "ace"


# "ezupkr"
# "ubmrapg"
# # set1: e z p k r
# # set2: b m r a
# # count: 2
# # index = (2,0)

# arr:list = [1]
# arr.p
