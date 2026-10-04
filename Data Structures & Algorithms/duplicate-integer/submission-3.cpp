#include <iostream>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> my_set;
        for (const int& elem : nums) {
            if (my_set.contains(elem)) {
                return true;
            }
            else 
                my_set.insert(elem);
        }
        return false;
    }
};