# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # the current node is the i+1 smallest value, where i is the number of nodes in the left subtree

        def recurse(curr, num_smaller):
            if not curr:
                return 0, False, 0
            
            left_size = 0
            found = False
            left_size, found, found_val = recurse(curr.left, 0)
            if found:
                return 0, True, found_val
            
            curr_size = left_size + 1 + num_smaller

            if curr_size == k:
                return 0, True, curr.val
                # return this value
            
            right_size, found, found_val = recurse(curr.right, curr_size)
            if found:
                return 0, True, found_val
            
            total_size = left_size + 1 + right_size
            return total_size, False, 0
        
        return recurse(root, 0)[2]
            


        