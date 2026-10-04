class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = {}
        for i in range(len(nums)):
            if target - nums[i] in curr:
                return [curr[target - nums[i]], i]
            else:
                curr[nums[i]] = i