class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the courses form a directed graph

        # we can just do bfs on the graph (since its finite, it must terminate) and see if we can take all the cours

        adj_list = {i:[] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            adj_list[crs].append(prereq)

        visitedSet = set()
        def dfs(crs):
            if crs in visitedSet:
                return False
            
            if adj_list[crs] == []:
                return True
            
            visitedSet.add(crs)
            
            for prereq in adj_list[crs]:
                if not dfs(prereq): return False
            
            visitedSet.remove(crs)
            adj_list[crs] = []
            return True
        

        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
