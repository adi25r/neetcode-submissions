class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        n = len(nums)
        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res
        
         
        # z_cnt = 0
        # for num in nums: # O(n)
        #     if num == 0:
        #         z_cnt += 1
        # if z_cnt > 1:
        #     return [0] * len(nums)
        # # division solution
        # mult = 1
        # for num in nums: # O(n)
        #     if num != 0:
        #         mult *= num
    
        # res = [0] * len(nums)
        # for i in range(len(nums)): # O(n)
        #     if nums[i] != 0:
        #         if z_cnt == 1:
        #             res[i] = 0
        #         else:
        #             res[i] = mult // nums[i]
        #     else:
        #         res[i] = mult
        # return res
        
        
        
        # trivial solution - do all the multiplications for each
        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != i:
        #             res[i] *= nums[j]     
        # return res
        