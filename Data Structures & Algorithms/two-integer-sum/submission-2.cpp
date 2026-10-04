#include <iostream>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> diff_set;
        for (int i = 0; i < nums.size(); i++) {
            if (diff_set.find((target - nums[i])) != diff_set.end())
                return {diff_set[target - nums[i]], i};
            else
                diff_set[nums[i]] =  i;
        }
        return {0, 0};
            
        
    }
};
