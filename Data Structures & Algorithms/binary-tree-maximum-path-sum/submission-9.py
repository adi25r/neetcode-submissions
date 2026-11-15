# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # paths can only go through a node once
        # at each node, the best path either goes through itself, or is from its left or right subchild
        # each helper returns max left straight sum, max right straight sum, sum if it were the inflection point

        self.max_sum = -float('inf')
        
        def helper(curr: Optional[TreeNode]):
            if not curr:
                return 0
            
            l_val = max(helper(curr.left), 0)
            r_val = max(helper(curr.right), 0)

            self.max_sum = max(self.max_sum, l_val + curr.val + r_val)
            
            return curr.val + max(l_val, r_val)
        
        helper(root)
        return self.max_sum

        