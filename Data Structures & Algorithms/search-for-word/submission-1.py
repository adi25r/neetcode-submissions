class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # try from every starting letter
        # for every starting layer, do dfs? 
        if not word:
            return True
        n, m = len(board), len(board[0])

        visit = set()

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i not in range(n) or j not in range(m) or board[i][j] != word[idx] or (i, j) in visit:
                return False
            visit.add((i, j))
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = i + dr, j + dc
                if dfs(nr, nc, idx + 1):
                    return True
            visit.remove((i, j))
        
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False




        
        