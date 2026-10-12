# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:



        self.max_sum = -float('inf')

        # at each step, return the value we get if we don't split
        # but, if we do split, then we can update our result
        def dfs(curr):
            if not curr:
                return 0
            
            l_val = dfs(curr.left)
            r_val = dfs(curr.right)

            # no point 
            if l_val <= 0 and r_val <= 0:
                self.max_sum = max(self.max_sum, curr.val)
                return curr.val
            
            curr_sum = curr.val
            if l_val > 0:
                curr_sum += l_val
            if r_val > 0:
                curr_sum += r_val

            self.max_sum = max(self.max_sum, curr_sum)
            
            # if we don't split, choose one or the other
            return curr.val + max(l_val, r_val)
        
        dfs(root)
        return self.max_sum


        