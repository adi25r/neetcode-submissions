from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i, string in enumerate(strs):
            sort_string = "".join(sorted(string))
            hashmap[sort_string].append(strs[i])
        
        return list(hashmap.values())

