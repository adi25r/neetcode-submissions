class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        # cannot rob 2 adjacent houses

        # let dp[i] = max amount at house i
        # if I rob the current house, then I must skip a house
        # otherwise, if I don't rob the current house, I couldhave robbed the last house
    
    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)

        dp[0]  = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]
        

        