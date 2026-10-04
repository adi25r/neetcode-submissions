class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxp = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         maxp = max(maxp, prices[j] - prices[i])
        # return maxp

        max_profit = 0
        min_so_far = float('inf')
        for num in prices:
            if num - min_so_far > max_profit:
                max_profit = num - min_so_far
            min_so_far = min(min_so_far, num)
        
        return max_profit
        