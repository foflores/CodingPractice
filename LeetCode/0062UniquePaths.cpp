/*
 A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

 The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the
 grid (marked 'Finish' in the diagram below).

 How many possible unique paths are there?
 */

class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 0 || n == 0)
            return 0;
        else if (m == 1 || n == 1)
            return 1;
        
        std::vector< std::vector<int> > util(m);
        for (int a{0}; a < m; a++)
        {
            util[a].resize(n);
            util[a][0] = 1;
        }
        for (int& b : util[0])
            b = 1;
        
        for (int a{1}; a < m; a++)
            for (int b{1}; b < n; b++)
                util[a][b] = util[a-1][b] + util[a][b-1];
        
        return util[m-1][n-1];
    }
};
