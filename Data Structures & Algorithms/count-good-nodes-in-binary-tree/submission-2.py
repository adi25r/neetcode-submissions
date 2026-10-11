# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for every node x, path is good if we never come across something greater from the root

        # keep track of max so far in each path

        self.count = 0
        def traverse(curr, max_so_far):
            if not curr:
                return 
            
            if curr.val >= max_so_far:
                self.count += 1
            
            traverse(curr.left, max(max_so_far, curr.val))
            traverse(curr.right, max(max_so_far, curr.val))

        traverse(root, -float("inf"))
        return self.count


        