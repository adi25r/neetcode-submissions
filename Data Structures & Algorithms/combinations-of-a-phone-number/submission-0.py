class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n_to_l = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        print(n_to_l)

        res = []

        def dfs(i, curr_res):
            if i >= len(digits):
                res.append(curr_res)
                return
            for option in n_to_l[digits[i]]:
                new_res = curr_res + option
                dfs(i + 1, new_res)
            
        
        dfs(0, "")
        return res
        