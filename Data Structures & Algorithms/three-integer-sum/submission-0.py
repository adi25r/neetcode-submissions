class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        take any 2 pair, then find a third to fit the pattern?
        make a set? no, lose whether or not we've chosen it

        trivial baseline n^3 sol
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        
        return res
        