/*
 A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

 The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the
 grid (marked 'Finish' in the diagram below).

 Now consider if some obstacles are added to the grids. How many unique paths would there be?

 An obstacle and space is marked as 1 and 0 respectively in the grid.
 
 Notes:
 - incomplete, error on input {{0,1}}, should return 0;
 */

class Solution {
public:
    int uniquePathsWithObstacles(std::vector< std::vector<int> >& obstacleGrid) {
        if (obstacleGrid.size() == 0 || obstacleGrid[0].size() == 0)
            return 0;
        else if ((obstacleGrid.size() == 1 || obstacleGrid[0].size() == 1) && obstacleGrid[0][0] == 1)
            return 0;
        else if ((obstacleGrid.size() == 1 || obstacleGrid[0].size() == 1) && obstacleGrid[0][0] == 0)
            return 1;
        
        std::vector< std::vector<int> > util(obstacleGrid.size());
        
        bool obs{false};
        for (int a{0}; a < obstacleGrid.size(); a++)
        {
            util[a].resize(obstacleGrid[a].size());
            if (obstacleGrid[a][0] == 1)
                obs = true;
            if (!obs)
                util[a][0] = 1;
            else
                util[a][0] = -1;
        }
        
        obs = false;
        for (int a{0}; a < util[0].size(); a++)
        {
            if (obstacleGrid[0][a] == 1)
                obs = true;
            if (!obs)
                util[0][a] = 1;
            else
                util[0][a] = -1;
        }

        
        for (int a{1}; a < util.size(); a++)
            for (int b{1}; b < util[a].size(); b++)
            {
                if (obstacleGrid[a][b] == 1)
                    util[a][b] = -1;
                else if (util[a-1][b] == -1)
                    util[a][b] = util[a][b-1];
                else if (util[a][b-1] == -1)
                    util[a][b] = util[a-1][b];
                else
                    util[a][b] = util[a-1][b] + util[a][b-1];
            }
        
        if (util[util.size()-1][util[0].size()-1] == -1)
            return 0;
        else
            return util[util.size()-1][util[0].size()-1];
    }
};
