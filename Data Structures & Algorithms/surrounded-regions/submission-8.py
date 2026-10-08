class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        # we need to determine if an area is surrounded on all sides by xs
        # we can only replace the entire region if it is surrounded 


        # lets say we just naively iterate through all the rows and columns
        # if we find an O, it must be a region
        # we need to determine if it is surrounded
        # from the O, run DFS, keep a visited list. if we get to an edge, then return false, which cascades through

        visited = set()
        # def dfs(r, c):
            
        #     if (r == 0 or r == n - 1 or c == 0 or c == m-1) and board[r][c] == "O":
        #         visited.add((r, c))
        #         return False
            
        #     if (r, c) in visited or board[r][c] == "X":
        #         visited.add((r, c))
        #         return True
            
        #     visited.add((r, c))
            
        #     val_to_ret = True
        #     for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        #         if not dfs(r + dr, c + dc):
        #             val_to_ret = False
            
        #     # when we come back from the dfs, nothing is touching the edge. Therefore, we can replace everything with an X
        #     if val_to_ret:
        #         board[r][c] = "X"
        #     return val_to_ret
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r, c) not in visited:
                    region = []
                    frontier = [(r, c)]
                    surrounded = True
                    visited.add((r, c))

                    while frontier:
                        curr_r, curr_c = frontier.pop()
                        region.append((curr_r, curr_c))

                        if curr_r == 0 or curr_r == n - 1 or curr_c == 0 or curr_c == m - 1:
                            surrounded = False

                        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if nr in range(n) and nc in range(m):
                                if (nr, nc) not in visited and board[nr][nc] == "O":
                                    frontier.append((nr, nc))
                                    visited.add((nr, nc))
                    
                    if surrounded:
                        for surr_r, surr_c in region:
                            board[surr_r][surr_c] = "X"
                




