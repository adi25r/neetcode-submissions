class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            print(x, y)

            if x == y:
                continue
            elif x > y: 
                heapq.heappush(max_heap, -(x-y))
            else:
                heapq.heappush(max_heap, -(y-x))
        
        return -max_heap[0] if len(max_heap) == 1 else 0
        