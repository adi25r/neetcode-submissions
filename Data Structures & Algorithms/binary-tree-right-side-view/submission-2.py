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
            size = len(frontier)
            curr_list = []

            for _ in range(size):
                curr = frontier.popleft()

                curr_list.append(curr.val)

                if curr.left: frontier.append(curr.left)
                
                if curr.right: frontier.append(curr.right)
            
            res.append(curr_list[-1])
        
        return res
        