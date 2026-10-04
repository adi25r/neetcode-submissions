class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        
        trapped_water = 0
        for i in range(1, len(height) - 1):
            curr_height = min(maxLeft[i], maxRight[i]) - height[i]
            if curr_height > 0:
                trapped_water += curr_height
        return trapped_water
        


        