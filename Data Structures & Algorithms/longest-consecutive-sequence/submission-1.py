class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        we can only pass through the array linearly




        """
        snums = sorted(nums)
        print(snums)

        max_count = 1
        curr_count = 1
        for i in range(1, len(nums)):
            if snums[i] != snums[i - 1] + 1 and snums[i] != snums[i - 1]:
                curr_count = 1
            elif snums[i] == snums[i - 1]:
                continue
            else:
                curr_count += 1
                if max_count < curr_count:
                    max_count = curr_count
        
        return max_count if len(nums) > 0 else 0
        