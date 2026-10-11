# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max number edges between any 2 nodes
        # naive solution: take every 2 pair of nodes, find the distance between them?
        self.res = 0
        # returns the height
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            self.res = max(self.res, left + right)
            
            return max(left, right) + 1

        helper(root)
        return self.res



        