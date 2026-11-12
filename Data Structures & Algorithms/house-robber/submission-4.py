class Solution:
    def rob(self, nums: List[int]) -> int:
        # let dp[i] maximum amount of money at house i
        # at each house, I could have either robbed myself, and
        # robbed 2 houses before, or skip myself
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[len(nums) - 1]


        