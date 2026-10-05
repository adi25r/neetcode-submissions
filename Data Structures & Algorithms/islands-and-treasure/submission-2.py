from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])

        frontier = deque([])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    frontier.append((r, c))
        
        while frontier:
            r, c = frontier.popleft()

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if nr in range(n) and nc in range(m):
                    if grid[nr][nc] > grid[r][c] + 1:
                        grid[nr][nc] = grid[r][c] + 1
                        frontier.append((nr, nc))




        # def bfs(r, c):
        #     # make the queue
        #     frontier = deque([((r, c), 0)])
        #     while frontier:
        #         # get the first item in the queue
        #         coords, level = frontier.popleft()
        #         curr_r, curr_c = coords[0], coords[1]
        #         # depth of the tree from that starting point
        #         grid[curr_r][curr_c] = level

        #         for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        #             nr, nc = curr_r + dr, curr_c + dc

        #             if nr in range(n) and nc in range(m):
        #                 # we can expand this way, and its better than what another bfs gave us
        #                 if grid[nr][nc] != -1 and level + 1 < grid[nr][nc]:
        #                     frontier.append(((nr, nc), level + 1))



        # for r in range(n):
        #     for c in range(m):
        #         if grid[r][c] == 0:
        #             # when we see a 0, we branch out everywhere
        #             bfs(r, c)

        