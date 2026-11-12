class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        we want the longest increasing subsequence
        at a given point, we can include a value, or not
        once we include a value, we need to go through rest of list with that as max
        otherwise, we skip and carry
        """

        memo = {}

        def dfs(i, carry):
            if (i, carry) in memo:
                return memo[(i, carry)]
            if i == len(nums):
                return 0

            # skip value
            max_len = dfs(i + 1, carry)

            # choose this value
            if nums[i] > carry:
                max_len = max(max_len, 1 + dfs(i + 1, nums[i]))

            memo[(i, carry)] = max_len
            return max_len

        return dfs(0, float("-inf"))



        