class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        # graph, each edge is the max height of the 2 edges

        # let's say im at a node 0
        # i can move to either 1 or 9
        # the cost would be min(abs(1-0), abs(9-0))
        # record a max time so far. everything else is accessible after that max time
        # so the cost would be = 0 if < max, abs(max - curr) otherwise
        # ucs(djikstras)

        # just use djikstra

        frontier = [(grid[0][0], 0, 0)]
        dist = [[float("inf") for _ in range(n)] for _ in range(n)]
        dist[0][0] = grid[0][0]

        while frontier:
            curr_elev, r, c = heapq.heappop(frontier)

            if r == n-1 and c == n-1:
                return dist[r][c]

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if nr in range(n) and nc in range(n):
                    cost = max(curr_elev, grid[nr][nc])
                    if dist[nr][nc] > cost:
                        dist[nr][nc] = cost
                        heapq.heappush(frontier, (cost, nr, nc))
            
        return 0




        # frontier = [(grid[0][0], 0, 0)]
        # visit = set()
        # visit.add((0, 0))
        # while frontier:
        #     elevation, r, c = heapq.heappop(frontier)

        #     if r == n - 1 and c == n-1:
        #         return elevation
            
        #     for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        #         nr, nc = r + dr, c + dc
        #         if nr in range(n) and nc in range(n) and (nr, nc) not in visit:
        #             visit.add((nr, nc))
        #             new_elev = max(elevation, grid[nr][nc])
        #             heapq.heappush(frontier, (new_elev, nr, nc))
            
        # return 0
