class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # return list of all unique combinations where sum to target

        res = []

        nums.sort(reverse=True)

        curr_list = []
        def backtrack(i, curr_total):
            if curr_total == target:
                res.append(curr_list.copy())
                return
            if i >= len(nums) or curr_total > target:
                return
            
            curr_list.append(nums[i])
            backtrack(i, curr_total + nums[i])
            curr_list.pop()

            # skip this number
            backtrack(i + 1, curr_total)

                
                
        backtrack(0, 0)
        return res




        