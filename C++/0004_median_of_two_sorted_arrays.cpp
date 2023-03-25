/*
 Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

 Follow up: The overall run time complexity should be O(log (m+n)).
 
 Notes:
 - Solved 39/2000~ cases
 - Memory error
 */
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (num1.size() == 0 && nums2.size() == 0) return 0;
        else if (num1.size() == 1 && nums2.size() == 0) return nums1[0];
        else if (num1.size() == 0 && nums2.size() == 1) return nums2[0];

        
    }
};


