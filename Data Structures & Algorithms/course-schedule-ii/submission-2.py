from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # must take course b before course a

        # want ORDERING of courses to finish all courses, can return any ordering

        adj_list = defaultdict(list)

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        
        cycle, done = set(), set()
        result = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in done:
                return True
    

            cycle.add(crs)
            
            for prereq in adj_list[crs]:
                if not dfs(prereq): return False
            
            cycle.remove(crs)
            result.append(crs)
            done.add(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return result

