class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxp = max(maxp, prices[j] - prices[i])
        return maxp

        # max_profit = 0
        # min_so_far = 0
        # max_so_far = 0 
        # for num in prices:
        #     min_so_far = min(min_so_far, num)
        #     max_so_far = max(max_so_far, num)

        #     if max_so_far - min_so_far > max_profit:
        #         max_profit = max_so_far - min_so_far
        
        # return max_profit
        