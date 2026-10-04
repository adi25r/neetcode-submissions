#include <vector>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (const int& num : nums)
            counts[num]++;

        priority_queue<pair<int, int>> freq_heap;
        for (const auto& pair : counts)
            freq_heap.push({pair.second, pair.first});

        vector<int> sol;
        for (int i = 0; i < k; i++) {
            pair<int, int> top_val = freq_heap.top();
            freq_heap.pop();
            sol.push_back(top_val.second);
        }

        return sol;

    }
};
