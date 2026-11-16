class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        for each value, we want to figure out where the next value greater than it is in the array
        
        keep a stack of values
        when next value comes, pop until not greater

        """
        sol = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                val, idx = stack.pop()
                sol[idx] = i - idx
            stack.append((temp, i))
    
        return sol



