from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = 0

        frontier = deque([])
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    frontier.append((r, c))

        days_needed = 0
        while frontier and fresh > 0:
            level = len(frontier)
            

            need_day = False

            for _ in range(level):
                r, c = frontier.popleft()

                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if nr in range(n) and nc in range(m):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            frontier.append((nr, nc))
                            fresh -= 1
            days_needed += 1
        
        if fresh > 0:
            return -1
        
        return days_needed

                    



        