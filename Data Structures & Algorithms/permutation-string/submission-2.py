class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for char in s1:
            s1_freq[char] = 1 + s1_freq.get(char, 0)
        
        for i in range(len(s2) - len(s1) + 1):
            s2_freq = {}
            for j in range(i, i + len(s1)):
                s2_freq[s2[j]] = 1 + s2_freq.get(s2[j], 0)
            
            if s1_freq == s2_freq:
                return True
        
        return False

        