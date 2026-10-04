from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i, j):
            frontier = deque([(i, j)])
            visited.add((i, j))
            while frontier:
                curr_row, curr_col = frontier.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = curr_row + dr, curr_col + dc

                    if 0 <= nr < n and 0 <= nc < m:
                        if (nr, nc) not in visited and grid[nr][nc] == "1":
                            visited.add((nr, nc))
                            frontier.append((nr, nc))
            

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)   
                    islands += 1

        
        return islands
