# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def depth(curr):
            if not curr:
                return 0
                
            left = depth(curr.left)
            right = depth(curr.right)

            if abs(left - right) > 1:
                self.balanced = False

            return max(left, right) + 1

        depth(root) 
        return self.balanced
        