class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        count = d - 1
        if d == 1:
            new_node = TreeNode(v, root) # assign the root only to left child
            return new_node
        queue = deque()
        queue.append([(root)])
        count -= 1
        nodes = []
        while queue:
            nodes = queue.popleft()
            if count == 0:
                break
            neighbors = []
            for node in nodes:
                if node.left:
                    neighbors.append((node.left))
                if node.right:
                    neighbors.append((node.right))
            queue.append(neighbors)
            count -= 1    
        for node in nodes:
            node.left = TreeNode(v, node.left, None)
            node.right = TreeNode(v, None, node.right)
        return root
