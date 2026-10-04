using namespace std; 

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for (const auto& str : strs) {
            string copy = str;
            sort(copy.begin(), copy.end());
            anagrams[copy].push_back(str);
        }
        vector<vector<string>> sol;
        for (const auto [anagram, corr_list] : anagrams) {
            sol.push_back(corr_list);
        }
        return sol;
    }
};
