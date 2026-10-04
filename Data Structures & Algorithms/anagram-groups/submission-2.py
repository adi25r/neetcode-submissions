from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashtable version
        result = defaultdict(list)
        for i, string in enumerate(strs):
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            
            result[tuple(freq)].append(strs[i])
        
        return list(result.values())

        # hashmap = defaultdict(list)
        # for i, string in enumerate(strs):
        #     sort_string = "".join(sorted(string))
        #     hashmap[sort_string].append(strs[i])
        
        # return list(hashmap.values())

