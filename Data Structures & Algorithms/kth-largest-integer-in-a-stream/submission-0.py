class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for i in range(len(nums)):
            heapq.heappush(self.heap, nums[i])
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        val = heapq.heappop(self.heap)
        heapq.heappush(self.heap, val)
        return val 
        
