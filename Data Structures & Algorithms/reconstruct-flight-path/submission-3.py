class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        tickets.sort()
        for src, dst in tickets:
            adj_list[src].append(dst)
        
        for src in adj_list:
            adj_list[src].sort(reverse=True)


        # just dfs from jfk, append when we can't go somewhere anymore
        result = []
        frontier = ["JFK"]
        
        while frontier:
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


        
        