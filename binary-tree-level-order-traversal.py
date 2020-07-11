from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        path = []
        result = []
        queue.append([root]) # [3]

        while queue:
            nodes = queue.popleft() # [15, 7]
            path.append(nodes) # [[3], [9, 20], [15, 7]]

            child = []
            for node in nodes: # 20
                if node.left: # 15
                    child.append(node.left) # 15
                
                if node.right: # 7
                    child.append(node.right) # 7
            
            if child:
                queue.append(child) # [15, 7]
        
        for nodes in path: # [9, 20]
            level = []

            for node in nodes: # 9
                level.append(node.val)
        
            result.append(level) 

        return result

