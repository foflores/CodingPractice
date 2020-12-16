/*
 Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is
 1000.
 */

#include <string>
#include <vector>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        if (s.length() == 0)
            return "";
        else if (s.length() == 1)
            return s;
        
        vector<std::string> palindromes;
        for (int a = 0; a < s.length(); a++){
            for (int b = 1; b < s.length()-a; b++){
                double mid{b/2.0};
                bool in_vector{false};
                std::string temp{""};
                for (int c = 0; c < palindromes.size(); c++){
                    if (temp == palindromes[c]){
                        in_vector = true;
                        break;
                    }
                }
                if (in_vector = false)
                    palindromes.push_back(temp);
            }
        }
    }
};
