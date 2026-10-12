# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # requires in order, post order traversal
            
        self.preorder = []
        def preorder_traversal(curr):
            if not curr:
                self.preorder.append("#")
                return
            self.preorder.append(str(curr.val))
            l_val = preorder_traversal(curr.left)
            r_val = preorder_traversal(curr.right)

        preorder_traversal(root)

        res = ",".join(self.preorder)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        self.i = 0
        def build():
            curr = vals[self.i]
            if curr == "#":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = build()
            node.right = build()
            return node
        
        return build()

        

        




