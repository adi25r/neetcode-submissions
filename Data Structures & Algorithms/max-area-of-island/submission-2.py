from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return

        n, m = len(grid), len(grid[0])

        visited = set()

        def bfs(r, c):
            frontier = deque([(r, c)])
            visited.add((r, c))
            curr_size = 1

            while frontier:
                curr_r, curr_c = frontier.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = curr_r + dr, curr_c + dc

                    if nr in range(n) and nc in range(m):
                        if (nr, nc) not in visited and grid[nr][nc] == 1:
                            visited.add((nr, nc))
                            frontier.append((nr, nc)) 
                            curr_size += 1
            return curr_size
            
            


        max_size = 0
        for r in range(n):
            for c in range(m):
                if (r, c) not in visited and grid[r][c] == 1:
                    size = bfs(r, c)
                    max_size = max(size, max_size)
        return max_size

        