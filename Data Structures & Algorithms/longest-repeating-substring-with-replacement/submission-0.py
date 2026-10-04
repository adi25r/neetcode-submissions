class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        brute force -- consider every substring
        """
        res = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                freq = [0] * 26
                for char in s[i:j]:
                    freq[ord(char) - ord('A')] += 1
                max_index = 0
                max_count = freq[0]
                for freq_idx in range(1, 26):
                    if freq[freq_idx] > max_count:
                        max_index = freq_idx
                        max_count = freq[freq_idx]
                
                if j - i <= k + max_count:
                    res = max(res, j - i)
        
        return res
                
            


