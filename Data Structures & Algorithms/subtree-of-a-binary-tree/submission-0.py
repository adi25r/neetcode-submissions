# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        # compare any 2 trees
        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            
            if n1.val != n2.val:
                return False
            
            if not dfs(n1.left, n2.left) or not dfs(n1.right, n2.right):
                return False
            
            return True
        
        # explores the nodes, if the value matches subtree root check if they are the same
        def explore_root(curr):
            if not curr:
                return False
            
            if curr.val == subRoot.val:
                if dfs(curr, subRoot):
                    return True
            
            if explore_root(curr.left) or explore_root(curr.right):
                return True
            
            return False

            
        return explore_root(root)
        

        