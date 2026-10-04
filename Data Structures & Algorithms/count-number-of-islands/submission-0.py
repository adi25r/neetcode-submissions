from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island_bfs(i, j, grid, vis_so_far):
            frontier = deque([(i, j)])
            vis_so_far.add((i, j))
            while frontier:
                curr_row, curr_col = frontier.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = curr_row + dr, curr_col + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if (nr, nc) not in vis_so_far and grid[nr][nc] == "1":
                            vis_so_far.add((nr, nc))
                            frontier.append((nr, nc))
            


        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    island_bfs(i, j, grid, visited)   
                    islands += 1

        
        return islands
