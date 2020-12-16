/*
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Definition for singly-linked list:

struct ListNode {
   int val;
   ListNode *next;
   ListNode() : val(0), next(nullptr) {}
   ListNode(int x) : val(x), next(nullptr) {}
   ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
 *************************
 Time Complexity: O(n)
 *************************
*/

struct ListNode {
   int val;
   ListNode *next;
   ListNode() : val(0), next(nullptr) {}
   ListNode(int x) : val(x), next(nullptr) {}
   ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry{0}, sum{0};
        ListNode *output{new ListNode()}, *temp{output};
        
        while (l1 != nullptr || l2 != nullptr){
            if (l1 != nullptr){
                sum += l1->val; 
                l1 = l1->next;
            }
            
            if (l2 != nullptr){
                sum += l2->val;
                l2 = l2->next;
            }

            temp->val = sum % 10;
            sum = sum / 10;
            if (l1 != nullptr || l2 != nullptr || sum != 0)
                temp = temp->next = new ListNode(sum);
        }
        
        return output;
    }
};

