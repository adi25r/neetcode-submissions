class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []

        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(closest, (-dist, [x, y]))
            if len(closest) > k:
                heapq.heappop(closest)
        res = []
        for dist, coord in closest:
            res.append(coord)
        
        return res
        