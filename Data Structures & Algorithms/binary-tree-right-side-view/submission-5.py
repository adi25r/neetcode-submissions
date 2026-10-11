# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # what does it mean to be the right most view?
        # in a level order traversal, we want the rightmost element in each level
        if not root:
            return []
        res = []
        frontier = deque([root])
        while frontier:
            rightSide = None
            size = len(frontier)

            for _ in range(size):
                curr = frontier.popleft()
                rightSide = curr

                if curr.left: frontier.append(curr.left)
                
                if curr.right: frontier.append(curr.right)
            
            if rightSide: res.append(rightSide.val)
        
        return res
        