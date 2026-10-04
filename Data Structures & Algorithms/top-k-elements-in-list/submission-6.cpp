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
            sol.push_back(freq_heap.top().second);
            freq_heap.pop();
        }

        return sol;

    }
};
