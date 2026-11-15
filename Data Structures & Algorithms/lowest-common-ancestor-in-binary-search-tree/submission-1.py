# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        u, v = min(p.val, q.val), max(p.val, q.val)

        if root is None:
            return None

        if root.val > v:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < u:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        



        