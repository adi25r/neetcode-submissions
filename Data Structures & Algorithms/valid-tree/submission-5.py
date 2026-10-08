from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # just run dfs, detect a cycle, return false?

        adj_list = defaultdict(list)

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        cycle = set()
        def dfs(node, prev):
            # print(cycle)
            if node in cycle:
                return False

            cycle.add(node)
            for neigh in adj_list[node]:
                if neigh == prev:
                    continue
                elif not dfs(neigh, node): return False
            return True
        
        return dfs(0, None) and len(cycle) == n
        