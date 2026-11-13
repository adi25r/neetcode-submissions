class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def helper(i, rem):
            if (i, rem) in memo:
                return memo[(i, rem)]
            if rem == 0 and i >= len(nums):
                return 1
            if i >= len(nums):
                return 0
            
            # either add or subtract
            memo[(i, rem)] = helper(i + 1, rem + nums[i]) + helper(i + 1, rem - nums[i])
            return memo[(i, rem)]
            
        return helper(0, target)