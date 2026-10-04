class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        keep a set and a length tracker
        if item already in set, start again from curr position
        """
        hashmap = {}



        m_cnt = 0
        count = 0
        for i, char in enumerate(s):
            if char in hashmap:
                prev_loc = hashmap[char]

                for key, value in list(hashmap.items()):
                    if value <= prev_loc:
                        del hashmap[key]
                        count -= 1

                count += 1
                hashmap[char] = i
            else:
                hashmap[char] = i
                count += 1
                m_cnt = max(m_cnt, count)
            
        return m_cnt
        