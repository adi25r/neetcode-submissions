class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        for src, dst in tickets: # O(E)
            adj_list[src].append(dst)
        
        for src in adj_list: # O(VlogV)
            adj_list[src].sort(reverse=True)

        result = []
        frontier = ["JFK"]
        
        # multiple flights from diff airports can go to the same vertex

        while frontier: # the next_node only goes through as many edges as they are, this, each time, adds at most one vertex of which to visit next. O(E)
            curr = frontier[-1]

            if not adj_list[curr]:
                result.append(frontier.pop())

            if adj_list[curr]:
                next_node = adj_list[curr].pop()
                frontier.append(next_node)
        
        return result[::-1]









        
        # stack = ["JFK"]
        # res = []

        # while stack:
        #     curr = stack[-1]
        #     if adj_list[curr]:
        #         next_node = adj_list[curr].pop()
        #         stack.append(next_node)
        #     else:
        #         res.append(stack.pop())
        
        # return res[::-1]


        # res = ["JFK"]
        # def dfs(src):
        #     if len(res) == len(tickets) + 1:
        #         return True
        #     if src not in adj_list:
        #         return False
            
        #     temp = list(adj_list[src])
        #     for i, neigh in enumerate(temp):
        #         adj_list[src].pop(i)
        #         res.append(neigh)
        #         if dfs(neigh): return True
                
        #         adj_list[src].insert(i, neigh)
        #         res.pop()
        #     return False

        # dfs("JFK")
        # return res


        
        