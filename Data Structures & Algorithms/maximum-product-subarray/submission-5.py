class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # at each point, we either multiply by ourselves w previous, or start new
        # track min and max at each pos

        res = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
            tmp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(tmp, num * currMin, num) 
            res = max(res, currMax)
        return res





        