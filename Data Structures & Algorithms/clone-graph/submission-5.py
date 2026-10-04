"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        old_to_new = {}

        # frontier = [node]
        new_node = Node(val=node.val)
        old_to_new[node] = new_node

        def dfs(node):
            if node not in old_to_new:
                new_node = Node(val=node.val)
                old_to_new[node] = new_node
            for neighbor in node.neighbors:
                if neighbor not in old_to_new:
                    dfs(neighbor)
                old_to_new[node].neighbors.append(old_to_new[neighbor])
            return old_to_new[node]
        
        return dfs(node)

        # while frontier:
        #     curr_node = frontier.pop()
        
        #     for neighbor in curr_node.neighbors:
        #         if neighbor not in old_to_new:
        #             frontier.append(neighbor)
        #             new_node = Node(val=neighbor.val)
        #             old_to_new[neighbor] = new_node
        #         old_to_new[curr_node].neighbors.append(old_to_new[neighbor])
        
        # return old_to_new[node]

        