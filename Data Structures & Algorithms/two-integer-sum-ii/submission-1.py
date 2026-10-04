class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        x = numbers[l] + numbers[r]
        while x != target:
            if x < target:
                l += 1
            else:
                r -= 1
            x = numbers[l] + numbers[r]
        
        return [l + 1, r + 1]
        