class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at each state, I can buy or wait.
        # if i sell, then I need to wait for a cooldown
        # can only sell once I buy

        dp = {}

        def helper(i, buying): 
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if not buying:
                # either buy
                buy = helper(i + 1, not buying) - prices[i]
                cooldown = helper(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = helper(i + 2, not buying) + prices[i]
                cooldown = helper(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        

        return helper(0, False)

        