/*
 Given an array of integers nums and an integer target, return indices of the
 two numbers such that they add up to target.

 You may assume that each input would have exactly one solution, and you may
 not use the same element twice.

 You can return the answer in any order.
 
 *************************
 Time Complexity: O(n)
 *************************
 */


#include <vector>
#include <map>

class Solution
{
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target){
        std::vector<int> output;
        std::map<int,int> util;
        for (int a{0}; a < nums.size(); a++){
            if (util.count(target - nums[a]) != 0){
                output.push_back(util[target - nums[a]]);
                output.push_back(a);
                break;
            }
            util.insert({nums[a], a});
                
        }
        return output;
    }
};
