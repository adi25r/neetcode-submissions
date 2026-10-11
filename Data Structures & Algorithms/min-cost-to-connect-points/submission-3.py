class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        rank = [0] * n
        par = [i for i in range(n)]

        def union(n1, n2):
            root1, root2 = find(n1), find(n2)
            if root1 == root2:
                return False
            
            if rank[root1] > rank[root2]:
                par[root2] = n1
            elif rank[root2] > rank[root1]:
                par[root1] = root2
            else:
                par[root1] = root2
                rank[root2] += 1
            return True
        
        def find(n1):
            if par[n1] != n1:
                par[n1] = find(par[n1])
            
            return par[n1]
        
        def man_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i in range(n):
            points[i] = tuple(points[i])

        edges = []
        # you can have an edge between any 2 points
        for i in range(n):
            for j in range(i+1, n):
                p1, p2 = points[i], points[j]
                if i == j:
                    continue
                heapq.heappush(edges, (man_dist(p1, p2), (i, j)) )
        # run kruskal's
        curr_cost, num_connected = 0, 0

        while num_connected < n - 1:
            dist, edge = heapq.heappop(edges)
            
            if union(edge[0], edge[1]):
                num_connected += 1
                curr_cost += dist
    
        return curr_cost





        