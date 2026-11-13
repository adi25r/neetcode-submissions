class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        at each number, I can assign to subset 1, or subset 2
        """

        memo = {}

        def helper(i, sum1, sum2):
            # either choose first, or second sum
            if i == len(nums):
                return sum1 == sum2
            
            if (i, sum1, sum2) in memo:
                return memo[(i, sum1, sum2)]

            # add to first sum1
            if helper(i + 1, sum1 + nums[i], sum2) or helper(i + 1, sum1, sum2 + nums[i]):
                memo[(i, sum1, sum2)] = True
                return True
            memo[(i, sum1, sum2)] = False
            return False
        
        return helper(0, 0, 0)
        