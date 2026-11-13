class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # at any point, you can use any 1 of the coins 

        memo = {}

        def helper(i, rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 1
            if (i, rem) in memo:
                return memo[(i, rem)] 
            
            count = 0
            # I can either use the current coin, or use others
            for j in range(i, len(coins)):
                # use coin again
                if coins[j] <= rem:
                    count += helper(j, rem - coins[j])
            memo[(i, rem)] = count
            return count
        
        return helper(0, amount)



        