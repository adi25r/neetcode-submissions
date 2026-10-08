class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # keep a list of sets? each set represents a connected component
        # start at a node, do dfs, build the connected component (ignore cycles, )


        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        components = []
        curr_component = set()

        def dfs(node, prev):
            if node in curr_component:
                return
            
            curr_component.add(node)
            
            for neigh in adj[node]:
                if neigh == prev:
                    continue
                dfs(neigh, node)
            
            return

        
        for i in range(n):
            skip_num = False
            for component in components:
                if i in component:
                    skip_num = True
                    break
                
            if not skip_num:
                dfs(i, None)
                components.append(curr_component.copy())
                curr_component = set()
        
        return len(components)
        