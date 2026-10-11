# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        frontier = deque([root])
    
        while frontier:
            curr_list = []
            size = len(frontier)
            for _ in range(size):
                curr = frontier.popleft()
                
                curr_list.append(curr.val)

                if curr.left:
                    frontier.append(curr.left)
                
                if curr.right:
                    frontier.append(curr.right)
            
            res.append(curr_list.copy())
        
        return res
                



        