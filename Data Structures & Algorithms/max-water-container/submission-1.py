class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        trivial solution:
        take any 2 pairs, then find max
        """
        l = 0
        r = len(heights) - 1

        max_area = 0
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, curr_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

        # max_area = 0
        # curr_area = 0
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         curr_area = min(heights[i], heights[j]) * (j - i)
        #         max_area = max(max_area, curr_area)
        
        # return max_area
        