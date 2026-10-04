from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i, string in enumerate(strs):
            sort_string = "".join(sorted(string))
            hashmap[sort_string].append(i)
        
        result = []
        for key, values in hashmap.items():
            temp_list = []
            for value in values:
                temp_list.append(strs[value])
            
            result.append(temp_list)
        
        return result

