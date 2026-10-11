# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        frontier = deque([])
        frontier.append(root)

        depth = 0
        while frontier:
            size = len(frontier)
            for _ in range(size):
                curr = frontier.popleft()
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)


            depth += 1
        
        return depth

        