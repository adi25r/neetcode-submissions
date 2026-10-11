class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # split string s into palindrome

        # suppose we are at index i, and everything be

        # aab
        # we can choose to take a
        # then, remaining is ab
        # choose a
        # then choose b

        # then backtrack backtrack
        # choose aa instead
        # then we just choose b
        res = []

        # inclusive of j
        def is_palindrome(i, j):
            l = i
            r = j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        curr_res = []
        def dp(i):
            if i >= len(s):
                res.append(curr_res.copy())
            # choose each palindrome starting at i, then 
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    curr_res.append(s[i:j+1])
                    dp(j + 1)
                    curr_res.pop()
                
        dp(0)
        return res







        