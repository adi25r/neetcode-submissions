class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the courses form a directed graph

        # we can just do bfs on the graph (since its finite, it must terminate) and see if we can take all the cours

        adj_list = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False

            if adj_list[crs] == []:
                return True
            
            visitSet.add(crs)
            for prereq in adj_list[crs]:
                if not dfs(prereq): return False
            
            visitSet.remove(crs)
            adj_list[crs] = []
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True



        