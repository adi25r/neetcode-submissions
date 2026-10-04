class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        brute force -- consider every substring
        """
        """
        sliding window -- how can we optimize?
        if we have a substring that wokr
        """
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while r - l + 1 > k + maxf:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res



        # def calcmostfreq(l: list) -> int:
        #     max_index = 0
        #     max_count = l[0]
        #     for m in range(len(l)):
        #         if l[m] > max_count:
        #             max_count = l[m]
        #             max_index = m
        #     return max_count

        # res = 0
        # l = 0
        # r = 0
        # freq = [0] * 26
        # freq[ord(s[r]) - ord('A')] += 1
        # while r < len(s):
        #     max_count = calcmostfreq(freq) 
        #     while r - l + 1 > max_count + k:
        #         freq[ord(s[l]) - ord('A')] -= 1
        #         l += 1
            
        #     freq[ord(s[r]) - ord('A')] += 1
        #     r += 1
                
        
        #     res = max(res, r - l + 1)
        # return res

        # res = 0
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s) + 1):
        #         freq = [0] * 26
        #         for char in s[i:j]:
        #             freq[ord(char) - ord('A')] += 1

        #         max_index = 0
        #         max_count = freq[0]
        #         for m in range(1, 26):
        #             if freq[m] > max_count:
        #                 max_count = freq[m]
        #                 max_index = m
                
        #         if max_count + k >= j - i:
        #             res = max(res, j - i)

                    
        
        return res
                
            


