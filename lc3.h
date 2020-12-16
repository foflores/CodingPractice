/*
 Given a string s, find the length of the longest substring without repeating
 characters.

 *************************
 Time Complexity: O(n)
 *************************
 */

#include <string>
#include <set>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int out{0}, l{0};
        std::set<char> substr;
        for (int a{0}; a < s.size(); a++){
            while (substr.count(s[a]) == 1){
                substr.erase(s[l]);
                l++;
            }
            substr.insert(s[a]);
            out = std::max(out, (int) substr.size());
        }
        return out;
    }
};

