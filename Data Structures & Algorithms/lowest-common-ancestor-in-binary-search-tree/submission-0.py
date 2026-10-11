# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None
        def explore(curr):
            u, v = min(p.val, q.val), max(p.val, q.val)
            if not curr:
                return 
            if curr.val < u:
                explore(curr.right)

            if curr.val > v:
                explore(curr.left)
            
            else:
                if self.lca == None:
                    self.lca = curr
                    return
        
        explore(root)
        return self.lca
