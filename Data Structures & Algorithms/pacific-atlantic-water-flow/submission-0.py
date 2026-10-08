from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        # naive bfs from each cell

        # frontier = deque([])

        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight): 
            if (r, c) in visited or r not in range(n) or c not in range(m) or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        for row in range(n):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, m - 1, atl, heights[row][m - 1])
        

        for col in range(m):
            dfs(0, col, pac, heights[0][col])
            dfs(n - 1, col, atl, heights[n-1][col])

        return list(pac.intersection(atl))