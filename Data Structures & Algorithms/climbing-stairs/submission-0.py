class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        arr = [0] * (n+1)

        arr[0] = 0
        arr[1] = 1
        arr[2] = 2

        for i in range(3, n+1):
            arr[i] = arr[i - 1] + arr[i - 2]
        
        return arr[n]
            
        