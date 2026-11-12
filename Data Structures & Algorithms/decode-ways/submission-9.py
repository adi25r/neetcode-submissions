class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def helper(idx):
            if idx == len(s):
                return 1
            if int(s[idx]) == 0:
                return 0
            if idx in memo:
                return memo[idx]
            res = helper(idx + 1)

            if idx + 1 < len(s):
                if s[idx] == "1" or s[idx] == "2" and int(s[idx:idx+2]) <= 26:
                    res += helper(idx + 2)
            
            memo[idx] = res

            return res

        return helper(0)

        