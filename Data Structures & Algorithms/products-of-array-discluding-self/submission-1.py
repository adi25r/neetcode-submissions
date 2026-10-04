class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z_cnt = 0
        for num in nums:
            if num == 0:
                z_cnt += 1
        if z_cnt > 1:
            return [0] * len(nums)
        # division solution
        mult = 1
        for num in nums:
            if num != 0:
                mult *= num
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                if z_cnt == 1:
                    res[i] = 0
                else:
                    res[i] = mult // nums[i]
            else:
                res[i] = mult
        return res
        
        
        
        # trivial solution - do all the multiplications for each
        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != i:
        #             res[i] *= nums[j]     
        # return res
        