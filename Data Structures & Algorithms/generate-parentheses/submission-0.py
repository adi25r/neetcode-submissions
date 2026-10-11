class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        # at any point, we can either 
        # 1) add a new opening parenthesis or 
        # 2) close an existing parenthesis

        
        def backtrack(o, c, curr_str):
            if o == c and c == n:
                res.append(curr_str)
            
            # add an opening 
            if o != n:
                backtrack(o + 1, c, curr_str + "(")
            
            if c != n and c < o:
                backtrack(o, c + 1, curr_str + ")")
        
        backtrack(0, 0, "")
        return res
            


        