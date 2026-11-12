class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # at each point, if its in the dict, seperate and try rest
        wordSet = set(wordDict)
        memo = {}

        def helper(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            j = i
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    if helper(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
            # while j < len(s):
            #     # find a word that matches
            #     while  s[i:j+1] not in wordSet and j < len(s):
            #         j += 1
            #     # if we didn't hit the length limit
            #     if s[i:j+1] in wordSet:
            #         # call helper
            #         if helper(j+1):
            #             memp[i] = True
            #             return True
            # memo[i] = False
            # return False
        
        return helper(0)


        