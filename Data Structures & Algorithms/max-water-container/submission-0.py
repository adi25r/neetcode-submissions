class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        trivial solution:
        take any 2 pairs, then find max
        """
        max_area = 0
        curr_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                curr_area = min(heights[i], heights[j]) * (j - i)
                max_area = max(max_area, curr_area)
        
        return max_area
        