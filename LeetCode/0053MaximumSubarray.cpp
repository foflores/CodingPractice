/*
 Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
 sum and return its sum.

 Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
 approach, which is more subtle.
 */

class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        
        std::vector<int> util(nums.size());
        util[0] = nums[0];
        int max{nums[0]};
        
        for (int a{1}; a < nums.size(); a++)
        {
            util[a] = util[a-1] + nums[a];
            if (max < util[a])
                max = util[a];
        }
        for (int a{0}; a < util.size(); a++)
            for (int b{a+1}; b < util.size(); b++)
            {
                if (max < util[b] - util[a])
                    max = util[b]-util[a];
            }
        
        return max;
    }
};
