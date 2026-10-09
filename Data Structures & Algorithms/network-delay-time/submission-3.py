class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # uniform cost search, 

        adj_list = defaultdict(list)

        for u, v, t in times:
            adj_list[u].append((v, t))

        frontier = [(0, k)]
        visit = set()
        
        time = 0

        while frontier and len(visit) != n:
            t, u = heapq.heappop(frontier)
            
            if u in visit: continue
            
            time = t
            visit.add(u)

            for nv, nt in adj_list[u]:
                if nv not in visit:
                    heapq.heappush(frontier, (nt + time, nv))
        
        return time if len(visit) == n else -1
        