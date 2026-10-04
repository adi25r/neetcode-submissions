class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> hashmap_s; 
        for (const char& ch : s) {
            if (hashmap_s.find(ch)  == hashmap_s.end()) 
                hashmap_s[ch] = 1;
            else
                hashmap_s[ch] += 1;
        }

        std::unordered_map<char, int> hashmap_t;
        for (const char& ch : t) {
            if (hashmap_t.find(ch)  == hashmap_s.end()) 
                hashmap_t[ch] = 1;
            else
                hashmap_t[ch] += 1;
        }

        return hashmap_s == hashmap_t;
        
    }
};
