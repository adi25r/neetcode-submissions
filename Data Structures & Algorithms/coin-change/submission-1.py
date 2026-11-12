class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # recurse here. Try using largest coin 
        memo = {}

        def helper(rem):
            if rem == 0:
                return 0
            
            # no way forward
            if rem < min(coins):
                return float('inf')
            
            if rem in memo:
                return memo[rem]

            min_so_far = float('inf')
            for coin in coins:
                if min_so_far > helper(rem - coin) + 1:
                    min_so_far = helper(rem - coin) + 1
            
            memo[rem] = min_so_far
            
            return min_so_far
        
        return helper(amount) if helper(amount) < float('inf') else -1
            

        