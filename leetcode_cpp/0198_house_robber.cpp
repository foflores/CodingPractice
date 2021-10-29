//Given by professor
class Solution
{
public:
    int rob (vector<int>& nums)
    {
        //[2,7,9,3,1]
        //[2,7,11,11,12] max haul for the first a-houses
        //1+11 vs 11
        
        if (nums.size()==0)
            return 0;
        else if (nums.size()==1)
            return nums[0];
        
        vector<int> util(nums.size());
        util[0] = nums[0];
        util[1] = max(nums[0], nums[1]);
        
        for (int a{2}; a < util.size(); a++)
            util[i] = mac(nums[a] + util[a-2], util[a-1]);
        
        return util[util.size()-1];
    }
}

//Also given by profesor
class Solution
{
public:
    int rob (vector<int>& nums)
    {
        if (nums.size()==0)
            return 0;
        else if (nums.size()==1)
            return nums[0];
        
        int util0{nums[0]};
        int util1{max(nums[0], nums[1])};
        int result{max(util0, util1)};
        
        for (int a{2}; a<nums.size(); a++)
        {
            result = max(nums[a]+util0, util1);
            util0 = util1;
            util1 = result;
        }
        return result;
    }
}
