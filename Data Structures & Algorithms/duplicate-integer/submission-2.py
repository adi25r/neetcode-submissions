class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = set()
        for val in nums:
            if val in curr:
                return True
            curr.add(val)
        
        return False
        