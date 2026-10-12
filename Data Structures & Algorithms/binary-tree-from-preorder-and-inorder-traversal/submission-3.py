# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre order -- visit current, then left, then rigght
        # in order -- left, current, right

        # get the root from pre order. find it in inorder, everything to its left must be left child

        # everything else to the right must be right child

        # repeat

        # base case: nothing to the left/right --> make a node and return

        if not preorder or not inorder:
            return
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        self.curr_idx = 0
        def dfs(l, r):
            if l > r:
                return
            root_val = preorder[self.curr_idx]
            root = TreeNode(root_val)
            self.curr_idx += 1
            mid = inorder_map[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)
        
        # root = TreeNode(preorder[0])
        # root_loc = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:1+root_loc], inorder[:root_loc])
        # root.right = self.buildTree(preorder[1+root_loc:], inorder[root_loc + 1:])

        

        # return root