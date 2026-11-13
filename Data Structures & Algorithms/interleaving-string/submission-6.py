class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # at any given point in the string s3, we choose one of s1 or s2
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def helper(s1i, s2i):
            # track the index of s3 we are making, along with where we are in s1 and s2
            if (s1i, s2i) in memo:
                return memo[s1i, s2i]

            if s1i + s2i >= len(s3) and s1i == len(s1) and s2i == len(s2):
                return True
            
            if s1i < len(s1) and s1[s1i] != s3[s1i + s2i] and s2i < len(s2) and s2[s2i] != s3[s1i + s2i]:
                return False
                
            val = False
            if s1i < len(s1) and s1[s1i] == s3[s1i + s2i]:
                if helper(s1i + 1, s2i):
                    val = True
            
            if s2i < len(s2) and s2[s2i] == s3[s1i + s2i]:
                if helper(s1i, s2i + 1):
                    val = True

            memo[s1i, s2i] = val
            return val
        
        return helper(0, 0)
            

        
        