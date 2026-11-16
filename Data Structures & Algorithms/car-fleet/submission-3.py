class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        d = r t

        need to figure out, for each, when they meet? 

        easiest way -- simulate time?

        sort the cars by position and speed

        for each, caculate time to target

        the value in the stack represents the time to the target of the car ahead of it. If that value is more (>=) than my time, then I will get stuck behind. Therefore, that is the bottleneck, and I will keep it on the stack
        if that value is <, then I am the bottleneck. just add me to the stack
        """
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        pairs.sort(reverse=True)
        stack = []

        for position, speed in pairs:
            target_time = (target - position) / speed
            if not stack or target_time > stack[-1]:
                stack.append(target_time)
            
        return len(stack)
    


        