class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # return all subsets of nums

        # for each number, you can either include it or not

        res = []
        nums.sort()

        curr_subset = []
        def backtrack(i):
            if i == len(nums):
                res.append(curr_subset.copy())
                return
            
            # choose number
            curr_subset.append(nums[i])
            backtrack(i + 1)
            curr_subset.pop()

            # skip number
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(j)
        
        backtrack(0)
        return res
            

        