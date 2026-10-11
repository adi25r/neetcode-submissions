class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        res = []

        curr_res = ["." * n for _ in range(n)]

        def can_place(r, c):
            # iterate through rows, check if any in same column
            for i in range(n):
                if curr_res[i][c] == "Q":
                    return False

            nr, nc = r - 1, c - 1
            while nr in range(n) and nc in range(n):
                if curr_res[nr][nc] == "Q":
                    return False
                nr, nc = nr - 1, nc - 1
            
            nr, nc = r - 1, c + 1
            while nr in range(n) and nc in range(n):
                if curr_res[nr][nc] == "Q":
                    return False
                nr, nc = nr - 1, nc + 1
            
            return True


        # place it row by row, backtrack if we can't place
        def backtrack(i):
            if i >= n:
                res.append(curr_res.copy())
                return 
            
            # which col (j) can we place a queen for row i
            for j in range(n):
                if can_place(i, j):
                    curr_res[i] = "." * j + "Q" + "." * (n - j - 1)
                    # backtrack
                    backtrack(i + 1)
                    curr_res[i] = "." * n
        
        backtrack(0)
        return res


        