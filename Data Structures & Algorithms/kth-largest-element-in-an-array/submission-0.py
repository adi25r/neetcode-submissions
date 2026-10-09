class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        val = heapq.heappop(min_heap)
        return val
        