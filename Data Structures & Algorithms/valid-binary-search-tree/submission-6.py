# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(curr): # returns min, max of that side
            if not curr:
                return 
            # if not curr.left and not curr.right:
            #     return curr.val, curr.val, True

            is_left = True
            is_right = True
            min_left, min_right = curr.val, curr.val
            max_left, max_right = curr.val, curr.val

            if curr.left:
                min_left, max_left, is_left = is_valid(curr.left)
                if max_left >= curr.val or not is_left:
                    return 0, 0, False
            
            if curr.right:
                min_right, max_right, is_right = is_valid(curr.right)
                if min_right <= curr.val or not is_right:
                    return 0, 0, False

            
            return min(curr.val, min_left, min_right), max(curr.val, max_left, max_right), True
        
        return is_valid(root)[2]
        