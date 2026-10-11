class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we want to permute all the numbers 
        # either add the num to the front or the back? 

        def backtrack(arr):
            print(arr)
            if len(arr) == 0:
                return [[]]
            
            curr_res = backtrack(arr[1:])
            new_perms = []
            for l in curr_res:
                for i in range(len(l) + 1):
                    tmp = l.copy()
                    tmp.insert(i, arr[0])
                    new_perms.append(tmp)
            
            return new_perms
        
        return backtrack(nums)

    
        # if len(nums) == 0:
        #     return [[]]
        
        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1): 
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)

        # return res

        