class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        we can only pass through the array linearly




        """
        snums = set(nums)
    
        max_len = 1
        curr_len = 1
        for num in nums:
            j = 1
            while True:
                if num + j in snums:
                    curr_len += 1
                    max_len = max(max_len, curr_len)
                    j += 1
                else:
                    curr_len = 1
                    break
            
        return max_len if len(nums) > 0 else 0

    


        # snums = sorted(nums)
        # print(snums)

        # max_count = 1
        # curr_count = 1
        # for i in range(1, len(nums)):
        #     if snums[i] != snums[i - 1] + 1 and snums[i] != snums[i - 1]:
        #         curr_count = 1
        #     elif snums[i] == snums[i - 1]:
        #         continue
        #     else:
        #         curr_count += 1
        #         if max_count < curr_count:
        #             max_count = curr_count
        
        # return max_count if len(nums) > 0 else 0
        