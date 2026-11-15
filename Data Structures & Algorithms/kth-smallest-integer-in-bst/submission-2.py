# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # curr node is i+1 smallest val, where i is the numberof nodes in the left subtree. 
        # recurse into the left subtree. we need the size of the left subtree. if we find the value in the left subtree, then we don'tneed to continue looking

        def dfs(curr, num_smaller):
            if not curr:
                return 0, float('-inf')
            left_size = 0
            found_val = float('-inf')
            left_size, found_val = dfs(curr.left, 0)
            
            if found_val != float('-inf'):
                return 0, found_val
            
            curr_entry = left_size + 1 + num_smaller

            if curr_entry == k:
                return 0, curr.val
            
            right_size, found_val = dfs(curr.right, curr_entry)
            if found_val != float('-inf'):
                return 0, found_val
            
            total_size = left_size + 1 + right_size
            return total_size, float('-inf')
        
        return dfs(root, 0)[1]
